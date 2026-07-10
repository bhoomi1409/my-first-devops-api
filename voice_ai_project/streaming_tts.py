import os
import time
import asyncio
import base64
import json
import pyaudio
import websockets
from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "21m00Tcm4TlvDq8ikWAM")

async def text_chunker(chunks):
    """Used to split the stream into sensible text chunks before sending to ElevenLabs"""
    # ElevenLabs recommends sending text in chunks when a space or punctuation is reached
    splitters = (".", ",", "?", "!", ";", ":", "—", "-", "(", ")", "[", "]", "}", " ")
    buffer = ""
    async for text in chunks:
        buffer += text
        if buffer.endswith(splitters):
            yield buffer
            buffer = ""
    if buffer:
        yield buffer

async def get_llm_stream(prompt):
    """Simulate getting a stream of text from LLM"""
    aclient = AsyncOpenAI(api_key=OPENAI_API_KEY)
    response = await aclient.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )
    async for chunk in response:
        delta = chunk.choices[0].delta.content
        if delta:
            yield delta

async def streaming_tts(prompt):
    print("⏳ Getting LLM response & streaming to TTS...")
    start_time = time.time()
    
    # ElevenLabs websocket URL for streaming
    uri = f"wss://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream-input?model_id=eleven_turbo_v2_5&output_format=pcm_16000_1"
    
    # Initialize PyAudio
    p = pyaudio.PyAudio()
    audio_stream = p.open(format=pyaudio.paInt16,
                          channels=1,
                          rate=16000,
                          output=True)

    async with websockets.connect(uri) as ws:
        # Send initial configuration with the API key
        init_msg = {
            "text": " ",
            "voice_settings": {"stability": 0.5, "similarity_boost": 0.8},
            "xi_api_key": ELEVENLABS_API_KEY
        }
        await ws.send(json.dumps(init_msg))

        async def send_text():
            # We wrap the LLM stream in the chunker to optimize TTS pacing
            llm_gen = get_llm_stream(prompt)
            print("🤖 AI: ", end="", flush=True)
            async for text_chunk in text_chunker(llm_gen):
                print(text_chunk, end="", flush=True)
                await ws.send(json.dumps({"text": text_chunk, "try_trigger_generation": True}))
            
            # Send empty string to indicate end of text
            await ws.send(json.dumps({"text": ""}))

        async def receive_audio():
            first_chunk_time = None
            
            while True:
                try:
                    message = await ws.recv()
                    data = json.loads(message)
                    if data.get("audio"):
                        # Log time-to-first-audio-chunk
                        if first_chunk_time is None:
                            first_chunk_time = time.time()
                            print(f"\n\n⚡ Time to first audio chunk (LLM + TTS latency): {(first_chunk_time - start_time)*1000:.0f}ms")
                            
                        audio_bytes = base64.b64decode(data["audio"])
                        # Play the audio immediately as it arrives
                        audio_stream.write(audio_bytes)
                    
                    if data.get("isFinal"):
                        break
                except websockets.exceptions.ConnectionClosed:
                    break

        # Run text sending and audio receiving concurrently
        await asyncio.gather(send_text(), receive_audio())
        
    audio_stream.stop_stream()
    audio_stream.close()
    p.terminate()

async def main():
    if not OPENAI_API_KEY or not ELEVENLABS_API_KEY:
        print("❌ Error: Please set OPENAI_API_KEY and ELEVENLABS_API_KEY in your .env file.")
        return
        
    print("=== Phase 3: Chunked LLM to Streaming TTS ===")
    prompt = "Give me a thrilling 2-sentence introduction about the future of voice AI agents."
    print(f"👤 Prompt: {prompt}\n")
    
    await streaming_tts(prompt)
    print("\n✅ Done!")

if __name__ == "__main__":
    asyncio.run(main())
