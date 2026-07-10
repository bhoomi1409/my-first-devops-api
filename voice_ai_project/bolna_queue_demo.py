import asyncio

class BolnaPipelineDemo:
    def __init__(self):
        # The core architecture of Bolna relies on independent asyncio Queues
        # connecting isolated workers. This decoupling is what makes barge-in
        # and latency management so reliable.
        self.stt_to_llm_queue = asyncio.Queue()
        self.llm_to_tts_queue = asyncio.Queue()
        self.tts_to_speaker_queue = asyncio.Queue()
        
        # State flag for interruptions
        self.is_interrupted = False
        self.workers = []

    async def stt_worker(self):
        """Simulates receiving chunks from Deepgram and putting them into the LLM queue."""
        print("[STT] Worker started.")
        try:
            # Simulate user speaking
            await asyncio.sleep(1)
            print("👤 [STT] Emitting final transcript: 'Tell me a joke.'")
            await self.stt_to_llm_queue.put("Tell me a joke.")
            
            # Simulate a barge-in 2 seconds later
            await asyncio.sleep(2)
            print("\n🚨 [STT] USER BARGED IN! Emitting interim transcript: 'Stop!'")
            await self.handle_interruption()
            
        except asyncio.CancelledError:
            print("[STT] Worker cancelled.")

    async def llm_worker(self):
        """Pulls transcripts from STT, streams from LLM, puts tokens into TTS queue."""
        print("[LLM] Worker started.")
        try:
            while True:
                transcript = await self.stt_to_llm_queue.get()
                if self.is_interrupted:
                    self.stt_to_llm_queue.task_done()
                    continue
                
                print(f"🧠 [LLM] Processing: '{transcript}'")
                
                # Simulate LLM generating a stream of tokens
                joke_tokens = ["Why ", "did ", "the ", "AI ", "cross ", "the ", "road? ", "To ", "optimize ", "the ", "other ", "side!"]
                
                for token in joke_tokens:
                    if self.is_interrupted:
                        print("🛑 [LLM] Interrupted mid-generation! Dropping remaining tokens.")
                        break
                    
                    print(f"🧠 [LLM] Yielding: '{token}'")
                    await self.llm_to_tts_queue.put(token)
                    await asyncio.sleep(0.3) # Simulate LLM generation time
                
                self.stt_to_llm_queue.task_done()
        except asyncio.CancelledError:
            print("[LLM] Worker cancelled.")

    async def tts_worker(self):
        """Pulls tokens from LLM, synthesizes audio, puts audio chunks into speaker queue."""
        print("[TTS] Worker started.")
        try:
            while True:
                token = await self.llm_to_tts_queue.get()
                if self.is_interrupted:
                    self.llm_to_tts_queue.task_done()
                    continue
                
                # Simulate converting text to audio bytes
                print(f"🔊 [TTS] Synthesizing audio for: '{token}'")
                await asyncio.sleep(0.1) # Simulate TTS latency
                
                await self.tts_to_speaker_queue.put(f"<AUDIO BYTES FOR: {token}>")
                self.llm_to_tts_queue.task_done()
        except asyncio.CancelledError:
            print("[TTS] Worker cancelled.")

    async def speaker_worker(self):
        """Pulls audio chunks and 'plays' them to the user/telephony line."""
        print("[SPEAKER] Worker started.")
        try:
            while True:
                audio_chunk = await self.tts_to_speaker_queue.get()
                if self.is_interrupted:
                    self.tts_to_speaker_queue.task_done()
                    continue
                
                print(f"🎧 [SPEAKER] Playing: {audio_chunk}")
                await asyncio.sleep(0.2) # Simulate actual playback time
                
                self.tts_to_speaker_queue.task_done()
        except asyncio.CancelledError:
            print("[SPEAKER] Worker cancelled.")

    async def handle_interruption(self):
        """This is how Bolna handles barge-in cleanly across decoupled stages."""
        self.is_interrupted = True
        print("\n🧹 [MANAGER] Clearing all queues...")
        
        # 1. Clear the queues immediately so workers don't process stale data
        self._clear_queue(self.stt_to_llm_queue)
        self._clear_queue(self.llm_to_tts_queue)
        self._clear_queue(self.tts_to_speaker_queue)
        
        # 2. Reset interrupt flag
        await asyncio.sleep(0.1) 
        self.is_interrupted = False
        print("✅ [MANAGER] Ready for new input.\n")

    def _clear_queue(self, q: asyncio.Queue):
        while not q.empty():
            try:
                q.get_nowait()
                q.task_done()
            except asyncio.QueueEmpty:
                break

    async def run(self):
        print("=== Bolna TaskManager Queue Architecture Demo ===\n")
        # Start all workers concurrently
        self.workers = [
            asyncio.create_task(self.stt_worker()),
            asyncio.create_task(self.llm_worker()),
            asyncio.create_task(self.tts_worker()),
            asyncio.create_task(self.speaker_worker())
        ]
        
        # Run the demo for 5 seconds to see the barge-in happen
        await asyncio.sleep(5)
        
        # Cleanup
        print("\n⏹️ Stopping demo...")
        for w in self.workers:
            w.cancel()
        await asyncio.gather(*self.workers, return_exceptions=True)

if __name__ == "__main__":
    demo = BolnaPipelineDemo()
    asyncio.run(demo.run())
