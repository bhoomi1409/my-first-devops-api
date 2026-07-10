import os
import asyncio
from dotenv import load_dotenv

from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, llm
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import openai, elevenlabs, deepgram, silero

load_dotenv()

async def entrypoint(ctx: JobContext):
    print("\n⏳ Agent joining LiveKit room...")
    # Connect to the room and only subscribe to audio tracks (no video)
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)
    print("✅ Connected to room!")

    # 1. Speech-to-Text: Deepgram
    stt = deepgram.STT(model="nova-2", language="en")
    
    # 2. Language Model: OpenAI
    llm_plugin = openai.LLM(model="gpt-4o-mini")

    # 3. Text-to-Speech: ElevenLabs
    tts = elevenlabs.TTS(
        model="eleven_turbo_v2_5",
        voice=os.getenv("ELEVENLABS_VOICE_ID", "21m00Tcm4TlvDq8ikWAM")
    )

    # LiveKit VoiceAssistant encapsulates Phase 1-4. 
    # It automatically handles VAD, interim transcripts, and barge-in cancellations.
    assistant = VoiceAssistant(
        vad=ctx.proc.userdata["vad"],
        stt=stt,
        llm=llm_plugin,
        tts=tts,
        chat_ctx=llm.ChatContext().append(
            role="system",
            text="You are a concise voice assistant powered by LiveKit. Keep answers under 2 sentences."
        ),
        # You can tune endpointing directly here:
        min_endpointing_delay=0.3, # 300ms
    )

    # Start listening to the room
    assistant.start(ctx.room)

    # Optional: Greet the user when they join
    await asyncio.sleep(1) # Short delay to ensure audio streams are ready
    await assistant.say("Hi there! I am powered by LiveKit. Try interrupting me!", allow_interruptions=True)

def prewarm(proc):
    # Preload the Silero VAD model locally into memory before the agent connects
    # Silero is the industry standard open-source VAD
    proc.userdata["vad"] = silero.VAD()

if __name__ == "__main__":
    if not all([os.getenv("OPENAI_API_KEY"), os.getenv("ELEVENLABS_API_KEY"), os.getenv("DEEPGRAM_API_KEY"), os.getenv("LIVEKIT_URL"), os.getenv("LIVEKIT_API_KEY"), os.getenv("LIVEKIT_API_SECRET")]):
        print("❌ Error: Missing API keys or LiveKit credentials in .env file.")
    else:
        print("=== Phase 6: LiveKit WebRTC Agent ===")
        # cli.run_app handles process management and connects the worker to the LiveKit Server
        cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, prewarm_fnc=prewarm))
