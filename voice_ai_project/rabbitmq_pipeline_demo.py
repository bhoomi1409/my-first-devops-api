import asyncio
import aio_pika
import os

RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost/")

# In a distributed production system (like an enterprise Bolna deployment),
# each of these workers would run in entirely separate Docker containers,
# horizontally scaled independently based on their GPU/CPU needs.

async def stt_worker(connection):
    """Listens to microphone/telephony and pushes transcripts to RabbitMQ."""
    print("[STT] Worker started.")
    channel = await connection.channel()
    await channel.declare_queue("stt_to_llm", auto_delete=True)
    
    # Simulate speech arriving
    await asyncio.sleep(1)
    print("👤 [STT] Emitting final transcript: 'Tell me a joke.'")
    await channel.default_exchange.publish(
        aio_pika.Message(body=b"Tell me a joke.", expiration=5000),
        routing_key="stt_to_llm"
    )
    
    # Simulate a barge-in event
    await asyncio.sleep(2)
    print("\n🚨 [STT] USER BARGED IN! Broadcasting 'purge' event.")
    # In RabbitMQ, we handle barge-in by publishing to a fanout exchange
    # or by sending a control message to flush queues.
    # For simplicity, we just simulate the event log here.

async def llm_worker(connection):
    """Pulls from STT queue, generates tokens, pushes to TTS queue."""
    print("[LLM] Worker started.")
    channel = await connection.channel()
    
    # QOS prefretch count ensures load balancing if running multiple LLM workers
    await channel.set_qos(prefetch_count=1)
    
    in_queue = await channel.declare_queue("stt_to_llm", auto_delete=True)
    await channel.declare_queue("llm_to_tts", auto_delete=True)
    
    async with in_queue.iterator() as queue_iter:
        async for message in queue_iter:
            async with message.process():
                transcript = message.body.decode()
                print(f"🧠 [LLM] Processing: '{transcript}'")
                
                # Simulate LLM generating a stream of tokens
                joke_tokens = ["Why ", "did ", "the ", "AI ", "cross ", "the ", "road? ", "To ", "scale ", "horizontally!"]
                
                for token in joke_tokens:
                    print(f"🧠 [LLM] Yielding: '{token}'")
                    await channel.default_exchange.publish(
                        aio_pika.Message(body=token.encode(), expiration=2000), # Messages expire quickly in real-time voice
                        routing_key="llm_to_tts"
                    )
                    await asyncio.sleep(0.3)

async def tts_worker(connection):
    """Pulls tokens from LLM, synthesizes audio, pushes to Speaker queue."""
    print("[TTS] Worker started.")
    channel = await connection.channel()
    await channel.set_qos(prefetch_count=1)
    
    in_queue = await channel.declare_queue("llm_to_tts", auto_delete=True)
    await channel.declare_queue("tts_to_speaker", auto_delete=True)
    
    async with in_queue.iterator() as queue_iter:
        async for message in queue_iter:
            async with message.process():
                token = message.body.decode()
                print(f"🔊 [TTS] Synthesizing audio for: '{token}'")
                await asyncio.sleep(0.1) # Simulate TTS latency
                
                await channel.default_exchange.publish(
                    aio_pika.Message(body=f"<AUDIO BYTES FOR: {token}>".encode(), expiration=2000),
                    routing_key="tts_to_speaker"
                )

async def speaker_worker(connection):
    """Pulls audio bytes and plays them."""
    print("[SPEAKER] Worker started.")
    channel = await connection.channel()
    await channel.set_qos(prefetch_count=1)
    
    in_queue = await channel.declare_queue("tts_to_speaker", auto_delete=True)
    
    async with in_queue.iterator() as queue_iter:
        async for message in queue_iter:
            async with message.process():
                audio_chunk = message.body.decode()
                print(f"🎧 [SPEAKER] Playing: {audio_chunk}")
                await asyncio.sleep(0.2) # Simulate actual playback time

async def main():
    print("=== Distributed Voice Pipeline via RabbitMQ ===\n")
    
    try:
        connection = await aio_pika.connect_robust(RABBITMQ_URL)
        print("✅ Connected to RabbitMQ.")
    except Exception as e:
        print(f"❌ Failed to connect to RabbitMQ at {RABBITMQ_URL}")
        print("   Make sure RabbitMQ is running. You can start it via Docker:")
        print("   docker run -it --rm -p 5672:5672 rabbitmq")
        return

    # Start all workers concurrently
    workers = [
        asyncio.create_task(llm_worker(connection)),
        asyncio.create_task(tts_worker(connection)),
        asyncio.create_task(speaker_worker(connection)),
        asyncio.create_task(stt_worker(connection)),
    ]
    
    # Run the demo for 6 seconds
    await asyncio.sleep(6)
    
    # Cleanup
    print("\n⏹️ Stopping demo...")
    for w in workers:
        w.cancel()
    await connection.close()

if __name__ == "__main__":
    asyncio.run(main())
