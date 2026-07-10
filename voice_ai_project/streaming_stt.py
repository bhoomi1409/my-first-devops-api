import os
import time
import asyncio
from dotenv import load_dotenv

from deepgram import (
    DeepgramClient,
    LiveTranscriptionEvents,
    LiveOptions,
    Microphone,
)

load_dotenv()

DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")

async def main():
    if not DEEPGRAM_API_KEY:
        print("❌ Error: DEEPGRAM_API_KEY is not set. Please add it to your .env file.")
        return

    print("=== Phase 2: Real-time Streaming STT (Deepgram) ===")
    
    try:
        # Initialize Deepgram Client
        deepgram = DeepgramClient(DEEPGRAM_API_KEY)
        
        # Create a websocket connection to Deepgram
        dg_connection = deepgram.listen.asyncwebsocket.v("1")

        # Track when the user stops speaking
        last_interim_time = time.time()

        async def on_message(self, result, **kwargs):
            nonlocal last_interim_time
            sentence = result.channel.alternatives[0].transcript
            
            if len(sentence) == 0:
                return

            if result.is_final:
                endpointing_latency = time.time() - last_interim_time
                # Clear the interim line
                print("\033[K", end="")
                print(f"🟢 [FINAL] ({endpointing_latency*1000:.0f}ms endpointing latency): {sentence}")
                print("   ➡️ (This is where we would trigger the LLM generation)")
            else:
                last_interim_time = time.time()
                # Print interim results on the same line
                print(f"⚪️ [Interim]: {sentence}", end="\r", flush=True)

        async def on_error(self, error, **kwargs):
            print(f"\n❌ Error: {error}")

        dg_connection.on(LiveTranscriptionEvents.Transcript, on_message)
        dg_connection.on(LiveTranscriptionEvents.Error, on_error)

        # Configure the live stream
        options = LiveOptions(
            model="nova-2",
            language="en",
            smart_format=True,
            encoding="linear16",
            channels=1,
            sample_rate=16000,
            interim_results=True,  # Crucial for the streaming mental shift
            endpointing=300,       # Endpointing threshold in ms
            utterance_end_ms="1000" # Detect end of utterance
        )

        print("\n⏳ Connecting to Deepgram Websocket...")
        if await dg_connection.start(options) is False:
            print("❌ Failed to connect to Deepgram")
            return

        print("✅ Connected!")
        print("🎤 Please start speaking into your microphone (Press Ctrl+C to stop)...\n")
        
        # Deepgram's SDK includes a helper Microphone class (requires PyAudio)
        microphone = Microphone(dg_connection.send)
        microphone.start()

        # Keep the script running
        while True:
            await asyncio.sleep(1)

    except KeyboardInterrupt:
        print("\n⏹️ Stopping...")
    except Exception as e:
        print(f"\n❌ Exception: {e}")
    finally:
        try:
            microphone.finish()
            await dg_connection.finish()
        except:
            pass
        print("🔌 Connection closed.")

if __name__ == "__main__":
    asyncio.run(main())
