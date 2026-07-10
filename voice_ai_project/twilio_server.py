import os
import json
import base64
import asyncio
from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import Response
from dotenv import load_dotenv
from openai import AsyncOpenAI
from deepgram import DeepgramClient, LiveOptions, LiveTranscriptionEvents
import websockets

load_dotenv()

app = FastAPI()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "21m00Tcm4TlvDq8ikWAM")

@app.post("/incoming")
async def incoming_call(request: Request):
    """Twilio Voice webhook endpoint. Returns TwiML."""
    host = request.headers.get("host")
    # TwiML to start a media stream to our websocket
    twiml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say>Connecting you to the AI agent.</Say>
    <Connect>
        <Stream url="wss://{host}/media" />
    </Connect>
</Response>"""
    return Response(content=twiml, media_type="text/xml")

class TwilioAgent:
    def __init__(self, websocket: WebSocket):
        self.ws = websocket
        self.stream_sid = None
        self.llm_client = AsyncOpenAI(api_key=OPENAI_API_KEY)
        self.dg_client = DeepgramClient(DEEPGRAM_API_KEY)
        self.dg_connection = self.dg_client.listen.asyncwebsocket.v("1")
        self.current_task = None
        self.is_speaking = False
        self.message_history = [
            {"role": "system", "content": "You are a helpful phone assistant. Keep answers to 1 or 2 sentences maximum."}
        ]

    async def generate_and_speak(self, prompt: str):
        self.is_speaking = True
        self.message_history.append({"role": "user", "content": prompt})
        
        # ElevenLabs output format for Twilio is ulaw_8000
        uri = f"wss://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream-input?model_id=eleven_turbo_v2_5&output_format=ulaw_8000"
        
        try:
            async with websockets.connect(uri) as tts_ws:
                init_msg = {
                    "text": " ",
                    "voice_settings": {"stability": 0.5, "similarity_boost": 0.8},
                    "xi_api_key": ELEVENLABS_API_KEY
                }
                await tts_ws.send(json.dumps(init_msg))

                async def send_text():
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
                            await tts_ws.send(json.dumps({"text": delta, "try_trigger_generation": True}))
                    await tts_ws.send(json.dumps({"text": ""}))
                    self.message_history.append({"role": "assistant", "content": ai_response})

                async def receive_audio():
                    while True:
                        msg = await tts_ws.recv()
                        data = json.loads(msg)
                        if data.get("audio"):
                            # Send mulaw audio chunk back to Twilio
                            twilio_msg = {
                                "event": "media",
                                "streamSid": self.stream_sid,
                                "media": {
                                    "payload": data["audio"]
                                }
                            }
                            await self.ws.send_json(twilio_msg)
                        if data.get("isFinal"):
                            break

                await asyncio.gather(send_text(), receive_audio())
        except asyncio.CancelledError:
            print("🛑 Task cancelled due to barge-in.")
            # Send a clear event to Twilio to instantly stop playing the audio buffer
            await self.ws.send_json({
                "event": "clear",
                "streamSid": self.stream_sid
            })
            raise
        finally:
            self.is_speaking = False

    async def start(self):
        # Deepgram setup
        async def on_message(self_dg, result, **kwargs):
            sentence = result.channel.alternatives[0].transcript
            if len(sentence) == 0:
                return

            if not result.is_final:
                if self.is_speaking:
                    # Cancel generation on barge-in
                    if self.current_task and not self.current_task.done():
                        self.current_task.cancel()
            else:
                if not self.is_speaking:
                    print(f"User: {sentence}")
                    self.current_task = asyncio.create_task(self.generate_and_speak(sentence))

        self.dg_connection.on(LiveTranscriptionEvents.Transcript, on_message)

        # Twilio audio format: mulaw 8000Hz
        options = LiveOptions(
            model="nova-2",
            language="en",
            smart_format=True,
            encoding="mulaw", # Crucial for Twilio
            channels=1,
            sample_rate=8000, # Crucial for Twilio
            interim_results=True,
            endpointing=400,
        )

        await self.dg_connection.start(options)

        try:
            while True:
                data = await self.ws.receive_json()
                if data['event'] == 'start':
                    self.stream_sid = data['start']['streamSid']
                    print(f"📞 Call started! Stream SID: {self.stream_sid}")
                elif data['event'] == 'media':
                    audio_payload = data['media']['payload']
                    audio_bytes = base64.b64decode(audio_payload)
                    # Send audio to Deepgram
                    self.dg_connection.send(audio_bytes)
                elif data['event'] == 'stop':
                    print("📞 Call ended.")
                    break
        except Exception as e:
            print(f"WebSocket closed: {e}")
        finally:
            await self.dg_connection.finish()

@app.websocket("/media")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    agent = TwilioAgent(websocket)
    await agent.start()

if __name__ == "__main__":
    import uvicorn
    print("=== Phase 5: Twilio Telephony Layer ===")
    print("Server running on port 8000.")
    print("Use ngrok to expose this port: ngrok http 8000")
    print("Set your Twilio Voice webhook to: https://<your-ngrok-url>/incoming")
    uvicorn.run(app, host="0.0.0.0", port=8000)
