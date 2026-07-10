import os
import time
import asyncio
import base64
import json
import pyaudio
import websockets
from enum import Enum
from dotenv import load_dotenv
from openai import AsyncOpenAI
from deepgram import (
    DeepgramClient,
    LiveTranscriptionEvents,
    LiveOptions,
    Microphone,
)

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "21m00Tcm4TlvDq8ikWAM")

class AgentState(Enum):
    LISTENING = 1
    THINKING = 2
    SPEAKING = 3

class ConversationManager:
    def __init__(self):
        self.state = AgentState.LISTENING
        self.current_task = None
        self.llm_client = AsyncOpenAI(api_key=OPENAI_API_KEY)
        
        # PyAudio setup
        self.p = pyaudio.PyAudio()
        self.audio_stream = self.p.open(format=pyaudio.paInt16,
                                        channels=1,
                                        rate=16000,
                                        output=True)
        
        # Deepgram setup
        self.dg_client = DeepgramClient(DEEPGRAM_API_KEY)
        self.dg_connection = self.dg_client.listen.asyncwebsocket.v("1")
        
        # Conversation history
        self.message_history = [
            {"role": "system", "content": "You are a helpful, conversational voice AI assistant. Keep all responses very short (1-2 sentences maximum)."}
        ]

    async def _text_chunker(self, chunks):
        splitters = (".", ",", "?", "!", ";", ":", "—", "-", "(", ")", "[", "]", "}", " ")
        buffer = ""
        async for text in chunks:
            buffer += text
            if buffer.endswith(splitters):
                yield buffer
                buffer = ""
        if buffer:
            yield buffer

    async def _get_llm_stream(self, prompt):
        self.message_history.append({"role": "user", "content": prompt})
        response = await self.llm_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=self.message_history,
            stream=True
        )
        ai_response = ""
        async for chunk in response:
            delta = chunk.choices[0].delta.content
            if delta:
                ai_response += delta
                yield delta
        self.message_history.append({"role": "assistant", "content": ai_response})

    async def generate_and_speak(self, prompt):
        self.state = AgentState.THINKING
        print("\n🤔 [THINKING]...")
        
        uri = f"wss://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream-input?model_id=eleven_turbo_v2_5&output_format=pcm_16000_1"
        
        try:
            async with websockets.connect(uri) as ws:
                init_msg = {
                    "text": " ",
                    "voice_settings": {"stability": 0.5, "similarity_boost": 0.8},
                    "xi_api_key": ELEVENLABS_API_KEY
                }
                await ws.send(json.dumps(init_msg))

                self.state = AgentState.SPEAKING
                print("🔊 [SPEAKING]: ", end="", flush=True)

                async def send_text():
                    llm_gen = self._get_llm_stream(prompt)
                    async for text_chunk in self._text_chunker(llm_gen):
                        print(text_chunk, end="", flush=True)
                        await ws.send(json.dumps({"text": text_chunk, "try_trigger_generation": True}))
                    await ws.send(json.dumps({"text": ""}))

                async def receive_audio():
                    while True:
                        message = await ws.recv()
                        data = json.loads(message)
                        if data.get("audio"):
                            audio_bytes = base64.b64decode(data["audio"])
                            self.audio_stream.write(audio_bytes)
                        if data.get("isFinal"):
                            break

                await asyncio.gather(send_text(), receive_audio())
                
        except asyncio.CancelledError:
            print("\n\n🛑 [BARGE-IN DETECTED] Cancelling generation and audio playback...")
            # Clear PyAudio buffer
            self.audio_stream.stop_stream()
            self.audio_stream.start_stream()
            # Note: We re-raise the CancelledError to ensure clean task cancellation
            raise
        except Exception as e:
            print(f"\n❌ Error in generate_and_speak: {e}")
        finally:
            self.state = AgentState.LISTENING
            print("\n🎧 [LISTENING]...")

    def trigger_barge_in(self):
        if self.state in [AgentState.THINKING, AgentState.SPEAKING]:
            if self.current_task and not self.current_task.done():
                self.current_task.cancel()

    async def run(self):
        print("=== Phase 4: Full Barge-in & Interruption Handling ===")
        
        async def on_message(self_dg, result, **kwargs):
            sentence = result.channel.alternatives[0].transcript
            if len(sentence) == 0:
                return

            if not result.is_final:
                # INTERIM RESULT
                # If we detect speech while the AI is thinking or speaking, trigger barge-in immediately!
                if self.state in [AgentState.THINKING, AgentState.SPEAKING]:
                    self.trigger_barge_in()
                else:
                    print(f"⚪️ [Interim]: {sentence}", end="\r", flush=True)
            else:
                # FINAL RESULT
                if self.state == AgentState.LISTENING:
                    print("\033[K", end="") # Clear line
                    print(f"🟢 [FINAL]: {sentence}")
                    
                    # Start the assistant response as an asyncio Task so it can be cancelled
                    self.current_task = asyncio.create_task(self.generate_and_speak(sentence))

        async def on_error(self_dg, error, **kwargs):
            print(f"❌ Deepgram Error: {error}")

        self.dg_connection.on(LiveTranscriptionEvents.Transcript, on_message)
        self.dg_connection.on(LiveTranscriptionEvents.Error, on_error)

        options = LiveOptions(
            model="nova-2",
            language="en",
            smart_format=True,
            encoding="linear16",
            channels=1,
            sample_rate=16000,
            interim_results=True,  # Mandatory for instant barge-in
            endpointing=400,       # Endpointing threshold in ms
            utterance_end_ms="1000"
        )

        print("\n⏳ Connecting to Deepgram...")
        if await self.dg_connection.start(options) is False:
            print("❌ Failed to connect to Deepgram")
            return

        microphone = Microphone(self.dg_connection.send)
        microphone.start()
        
        print("✅ Connected! Start speaking.")
        print("💡 TIP: Ask it a question, then try interrupting it mid-sentence by speaking again!\n")
        print("🎧 [LISTENING]...")

        try:
            while True:
                await asyncio.sleep(1)
        except KeyboardInterrupt:
            print("\n⏹️ Stopping...")
        finally:
            try:
                microphone.finish()
                await self.dg_connection.finish()
            except:
                pass
            self.audio_stream.stop_stream()
            self.audio_stream.close()
            self.p.terminate()

if __name__ == "__main__":
    if not all([OPENAI_API_KEY, ELEVENLABS_API_KEY, DEEPGRAM_API_KEY]):
        print("❌ Error: Please ensure OPENAI_API_KEY, ELEVENLABS_API_KEY, and DEEPGRAM_API_KEY are set.")
    else:
        manager = ConversationManager()
        asyncio.run(manager.run())
