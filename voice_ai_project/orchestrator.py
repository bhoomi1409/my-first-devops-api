import os
import json
import asyncio
from dotenv import load_dotenv
import litellm

load_dotenv()

class Assistant:
    def __init__(self, config_name: str, config_path: str = "personas.json"):
        with open(config_path, "r") as f:
            all_configs = json.load(f)
            
        if config_name not in all_configs:
            raise ValueError(f"Persona '{config_name}' not found in {config_path}")
            
        self.config = all_configs[config_name]
        self.name = self.config["name"]
        
        # 1. Setup LLM via LiteLLM
        llm_conf = self.config["llm"]
        # litellm requires the model string formatted as "provider/model" for non-openai
        self.llm_model = f"{llm_conf['provider']}/{llm_conf['model']}" if llm_conf['provider'] != 'openai' else llm_conf['model']
        self.system_prompt = llm_conf["system_prompt"]
        self.message_history = [{"role": "system", "content": self.system_prompt}]
        
        # 2. Setup Transcriber
        stt_conf = self.config["transcriber"]
        self.stt_provider = stt_conf["provider"]
        self.stt_model = stt_conf["model"]
        
        # 3. Setup Synthesizer
        tts_conf = self.config["synthesizer"]
        self.tts_provider = tts_conf["provider"]
        self.tts_voice = tts_conf["voice_id"]
        
        print(f"🚀 Initialized Agent: {self.name}")
        print(f"   🎙️ STT: {self.stt_provider} ({self.stt_model})")
        print(f"   🧠 LLM: {self.llm_model}")
        print(f"   🔊 TTS: {self.tts_provider} (Voice: {self.tts_voice})")

    async def generate_response(self, user_input: str):
        self.message_history.append({"role": "user", "content": user_input})
        
        print(f"\n[{self.name}] Thinking... (Routing to {self.llm_model})")
        
        # LiteLLM abstract call (works identically for OpenAI, Anthropic, Mistral, Gemini, Azure, etc.)
        response = await litellm.acompletion(
            model=self.llm_model,
            messages=self.message_history,
            temperature=0.3
        )
        
        ai_text = response.choices[0].message.content
        self.message_history.append({"role": "assistant", "content": ai_text})
        
        print(f"[{self.name}] Says: '{ai_text}'")
        
        # In a real app, you would now dynamically route to the self.tts_provider 
        # using the self.tts_voice setting.
        return ai_text

async def main():
    print("=== Phase 7: Config-Driven Orchestration (Bolna style) ===\n")
    
    # Check for keys. LiteLLM automatically uses API keys from env.
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️ Warning: OPENAI_API_KEY missing.")
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("⚠️ Warning: ANTHROPIC_API_KEY missing. (The Customer Support persona will fail unless you provide this).")
    if not os.getenv("MISTRAL_API_KEY"):
        print("⚠️ Warning: MISTRAL_API_KEY missing. (The Tech Advisor persona will fail).")
        
    print("1️⃣ Loading 'FireReach SDR' Persona...")
    sdr_agent = Assistant("fire_reach_sdr")
    await sdr_agent.generate_response("Hi, I'm interested in your software.")
    
    print("\n-------------------------------------------------\n")
    
    print("2️⃣ Loading 'Friendly Support' Persona...")
    support_agent = Assistant("customer_support")
    try:
        await support_agent.generate_response("My account is locked, can you help me?")
    except Exception as e:
        print(f"❌ Failed to run support agent: {e}")

    print("\n-------------------------------------------------\n")

    print("3️⃣ Loading 'Mistral Tech Advisor' Persona...")
    tech_agent = Assistant("tech_advisor")
    try:
        await tech_agent.generate_response("Should I use websockets or WebRTC for a voice bot?")
    except Exception as e:
        print(f"❌ Failed to run tech agent: {e}")

if __name__ == "__main__":
    asyncio.run(main())
