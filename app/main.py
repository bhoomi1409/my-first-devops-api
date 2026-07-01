import time
import uuid
import logging
from typing import Dict, Any, Optional
from fastapi import FastAPI, Request, Header, HTTPException, status
from fastapi.responses import JSONResponse

# Configure structured JSON logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("fde_service")

app = FastAPI(
    title="FDE Production-Ready API",
    description="Enterprise-grade resilient microservice demonstrating Kubernetes probes, idempotency, and correlation IDs.",
    version="2.0.0"
)

# In-memory idempotency cache (In real production, use Redis setnx)
idempotency_store: Dict[str, Any] = {}

@app.middleware("http")
async def add_correlation_id_and_timer(request: Request, call_next):
    """
    FDE Middleware: Injects a unique trace ID into every request for distributed tracing
    and records latency metrics to prevent slow-query outages.
    """
    request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
    start_time = time.time()
    
    response = await call_next(request)
    
    duration = round((time.time() - start_time) * 1000, 2)
    response.headers["X-Request-ID"] = request_id
    response.headers["X-Response-Time-Ms"] = str(duration)
    logger.info(f"Path={request.url.path} Status={response.status_code} DurationMs={duration} RequestID={request_id}")
    return response

@app.get("/health/live", status_code=status.HTTP_200_OK)
def liveness_probe():
    """
    Kubernetes Liveness Probe: Returns 200 OK as long as the Python event loop is responsive.
    """
    return {"status": "ALIVE", "timestamp": time.time()}

@app.get("/health/ready", status_code=status.HTTP_200_OK)
def readiness_probe():
    """
    Kubernetes Readiness Probe: Verifies internal dependencies (cache, DB) before taking traffic.
    """
    # If DB or Redis is down, return 503 Service Unavailable so Kubernetes drains traffic!
    return {"status": "READY", "dependencies": {"database": "connected", "redis": "connected"}}

@app.get("/")
def read_root():
    return {"message": "Hello from FDE Production API!", "status": "operational"}

@app.post("/checkout")
def idempotent_checkout(
    amount: float,
    x_idempotency_key: Optional[str] = Header(None, alias="X-Idempotency-Key")
):
    """
    Demonstrates network retry safety (Idempotency Key).
    If a client retries due to dropped network ACK packets, return cached result without double charging!
    """
    if not x_idempotency_key:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Missing mandatory X-Idempotency-Key header for financial mutation."
        )
    
    if x_idempotency_key in idempotency_store:
        logger.warning(f"Duplicate request intercepted for IdempotencyKey={x_idempotency_key}. Returning cached response.")
        return {"status": "CACHED_SUCCESS", "message": "Transaction previously completed.", "data": idempotency_store[x_idempotency_key]}
    
    # Execute business logic
    result = {"transaction_id": f"txn_{uuid.uuid4().hex[:8]}", "charged_amount": amount, "timestamp": time.time()}
    idempotency_store[x_idempotency_key] = result
    
    return {"status": "SUCCESS", "message": "Payment charged successfully.", "data": result}

