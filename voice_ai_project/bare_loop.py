import os
import time
import requests
from openai import OpenAI
import sounddevice as sd
import soundfile as sf
from dotenv import load_dotenv

# Load environment variables (e.g. from .env file)
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

if not OPENAI_API_KEY:
    print("Warning: OPENAI_API_KEY is not set. STT and LLM will fail.")
if not ELEVENLABS_API_KEY:
    print("Warning: ELEVENLABS_API_KEY is not set. TTS will fail.")

# Initialize OpenAI Client (used for Whisper STT and GPT-4o-mini LLM)
openai_client = OpenAI(api_key=OPENAI_API_KEY)

ELEVENLABS_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "21m00Tcm4TlvDq8ikWAM") # Default voice

def record_audio(filename="input.wav", duration=5, fs=44100):
    print(f"\n🎤 Recording for {duration} seconds... Speak now!")
    # Blocking recording
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    sf.write(filename, recording, fs)
    print("✅ Recording saved.")
    return filename

def stt_whisper(filename="input.wav"):
    print("⏳ Running STT (Whisper API)...")
    start_time = time.time()
    
    with open(filename, "rb") as audio_file:
        transcription = openai_client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
        )
        
    latency = time.time() - start_time
    print(f"✅ STT Latency: {latency:.2f}s")
    return transcription.text, latency

def llm_gpt(prompt):
    print("⏳ Running LLM (GPT-4o-mini)...")
    start_time = time.time()
    
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful, concise AI voice assistant. Keep your answers brief (1-2 sentences)."},
            {"role": "user", "content": prompt}
        ]
    )
    
    text = response.choices[0].message.content
    latency = time.time() - start_time
    print(f"✅ LLM Latency: {latency:.2f}s")
    return text, latency

def tts_elevenlabs(text, filename="output.mp3"):
    print("⏳ Running TTS (ElevenLabs)...")
    start_time = time.time()
    
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVENLABS_VOICE_ID}"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": ELEVENLABS_API_KEY
    }
    data = {
        "text": text,
        "model_id": "eleven_turbo_v2_5",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }
    
    response = requests.post(url, json=data, headers=headers)
    if response.status_code != 200:
        print("❌ TTS Failed:", response.text)
        return None, 0
        
    # Save the received audio
    with open(filename, "wb") as f:
        f.write(response.content)
        
    latency = time.time() - start_time
    print(f"✅ TTS Latency: {latency:.2f}s")
    return filename, latency

def play_audio(filename):
    print("🔊 Playing audio...")
    # Using afplay, which is native to macOS for playing audio files
    os.system(f"afplay {filename}")

def main():
    print("=== Phase 1: Bare Loop Audio Pipeline ===")
    if not OPENAI_API_KEY or not ELEVENLABS_API_KEY:
        print("❌ Please set your OPENAI_API_KEY and ELEVENLABS_API_KEY in the .env file or environment.")
        return

    # 1. Record Audio (Blocking)
    input_wav = record_audio(duration=5)
    
    # 2. STT (Speech to Text)
    user_text, stt_latency = stt_whisper(input_wav)
    print(f"\n👤 User said: '{user_text}'")
    
    if not user_text.strip():
        print("No speech detected. Exiting.")
        return

    # 3. LLM (Language Model)
    ai_text, llm_latency = llm_gpt(user_text)
    print(f"\n🤖 AI says: '{ai_text}'")
    
    # 4. TTS (Text to Speech)
    output_audio, tts_latency = tts_elevenlabs(ai_text)
    
    if output_audio:
        # 5. Play Output
        play_audio(output_audio)
    
    # Summary of metrics
    print("\n=== Performance Metrics ===")
    print(f"STT Latency: {stt_latency:.2f}s")
    print(f"LLM Latency: {llm_latency:.2f}s")
    print(f"TTS Latency: {tts_latency:.2f}s")
    print(f"Total Pipeline Latency: {(stt_latency + llm_latency + tts_latency):.2f}s")
    print("===========================\n")

if __name__ == "__main__":
    main()
