from fastapi import FastAPI

# Create the main application object
app = FastAPI(title="My First DevOps API")

# Define our first "Endpoint" (a URL we can visit)
@app.get("/")
def read_root():
    return {"message": "Hello World! My API is running!"}

# Define a second endpoint that mimics an ML prediction
@app.get("/predict")
def predict(value: int):
    # In reality, this would use an ML model. Here we just do simple math.
    result = value * 100
    return {"input": value, "prediction": result, "status": "success"}
