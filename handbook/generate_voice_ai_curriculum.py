import os

def generate_voice_ai_curriculum():
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Voice AI Agent Mastery — Full Curriculum</title>
    <style>
        :root {
            --primary-bg: #0f172a;
            --secondary-bg: #1e293b;
            --accent-color: #3b82f6;
            --text-main: #f8fafc;
            --text-muted: #cbd5e1;
            --border-color: #334155;
            --gradient-start: #3b82f6;
            --gradient-end: #8b5cf6;
        }

        body {
            font-family: 'Inter', system-ui, -apple-system, sans-serif;
            background-color: var(--primary-bg);
            color: var(--text-main);
            line-height: 1.6;
            margin: 0;
            padding: 0;
        }

        .container {
            max-width: 1000px;
            margin: 0 auto;
            padding: 2rem;
        }

        header {
            text-align: center;
            margin-bottom: 4rem;
            padding-bottom: 2rem;
            border-bottom: 1px solid var(--border-color);
        }

        h1 {
            font-size: 2.5rem;
            background: linear-gradient(to right, var(--gradient-start), var(--gradient-end));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
        }

        h2 {
            font-size: 2rem;
            color: var(--text-main);
            margin-top: 3rem;
            margin-bottom: 1.5rem;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid var(--border-color);
        }

        h3 {
            font-size: 1.5rem;
            color: var(--accent-color);
            margin-top: 2rem;
            margin-bottom: 1rem;
        }

        p {
            color: var(--text-muted);
            margin-bottom: 1.5rem;
        }

        .code-block {
            background-color: #000;
            padding: 1.5rem;
            border-radius: 0.5rem;
            font-family: 'Fira Code', monospace;
            color: #10b981;
            margin-bottom: 1.5rem;
            overflow-x: auto;
        }

        ul, ol {
            color: var(--text-muted);
            margin-bottom: 1.5rem;
            padding-left: 1.5rem;
        }

        li {
            margin-bottom: 0.5rem;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 2rem;
            background-color: var(--secondary-bg);
            border-radius: 0.5rem;
            overflow: hidden;
        }

        th, td {
            padding: 1rem;
            text-align: left;
            border: 1px solid var(--border-color);
        }

        th {
            background-color: rgba(255, 255, 255, 0.05);
            font-weight: 600;
            color: var(--text-main);
        }

        .phase-card {
            background-color: var(--secondary-bg);
            border: 1px solid var(--border-color);
            border-radius: 0.5rem;
            padding: 2rem;
            margin-bottom: 2rem;
            transition: transform 0.2s;
        }

        .phase-card:hover {
            transform: translateY(-5px);
        }

        .practical-demo {
            background-color: rgba(59, 130, 246, 0.1);
            border-left: 4px solid var(--accent-color);
            padding: 1.5rem;
            margin-top: 1.5rem;
            border-radius: 0 0.5rem 0.5rem 0;
        }

        .practical-demo h4 {
            margin-top: 0;
            color: var(--text-main);
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Voice AI Agent Mastery — Full Curriculum</h1>
            <p>Building a Bolna / LiveKit / Tough Tongue-level Voice AI Platform from Scratch</p>
        </header>

        <section id="mental-model">
            <h2>0. The Mental Model (read this first)</h2>
            <p>Every product in this space — Bolna, LiveKit Agents, Vapi, Retell, Tough Tongue, Hyperbound, Synthflow, Bland AI — is the <strong>same pipeline</strong> wearing different clothes:</p>
            
            <div class="code-block">
Audio In → VAD (detect speech) → STT (speech-to-text)
        → LLM (understand + decide + generate)
        → TTS (text-to-speech) → Audio Out
            </div>

            <p>Wrapped in:</p>
            <ul>
                <li><strong>Transport layer</strong>: how audio actually moves (phone call / browser / Zoom)</li>
                <li><strong>Turn-taking layer</strong>: who's allowed to talk right now, and what happens on interruption</li>
                <li><strong>Orchestration layer</strong>: config-driven agent definition, tool-calling, session state</li>
                <li><strong>Product layer</strong>: what you sell on top (roleplay scoring, SDR calling, interview coaching)</li>
            </ul>

            <p>Once you understand this, every competitor is just "where did they draw the line on what to build vs buy":</p>

            <table>
                <thead>
                    <tr>
                        <th>Layer</th>
                        <th>Bolna</th>
                        <th>LiveKit</th>
                        <th>Vapi/Retell</th>
                        <th>Tough Tongue/Hyperbound</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Transport</td>
                        <td>Twilio/Plivo/Exotel (telephony)</td>
                        <td>WebRTC (own infra)</td>
                        <td>Managed (both)</td>
                        <td>Managed (both)</td>
                    </tr>
                    <tr>
                        <td>Orchestration</td>
                        <td>Open source, JSON config, self-host</td>
                        <td>Open source Agents SDK</td>
                        <td>Managed, dashboard config</td>
                        <td>Managed, no-code</td>
                    </tr>
                    <tr>
                        <td>Product layer</td>
                        <td>None — you build it</td>
                        <td>None — you build it</td>
                        <td>None — you build it</td>
                        <td>Roleplay scoring, SDR flows, coaching</td>
                    </tr>
                </tbody>
            </table>

            <p><strong>Your target</strong>: clone the orchestration + transport layers (Bolna/LiveKit tier), then optionally bolt a product layer on top (Tough Tongue tier) for FireReach's outbound calling feature.</p>
        </section>

        <section id="phase-1" class="phase-card">
            <h2>PHASE 1 — Foundations (Week 1)</h2>
            <p><strong>Goal: understand every piece before wiring them together</strong></p>

            <h3>Topics</h3>
            <ol>
                <li><strong>The streaming mental shift</strong> — nothing in production voice AI waits for a "complete" anything. STT emits partial transcripts word by word. LLM emits tokens as they're generated. TTS emits audio chunks as text arrives. If you wait for full completions at any stage, you get 3-5 second dead air and the product feels broken.</li>
                <li><strong>Latency budget</strong> — human conversation has ~200-500ms response gaps. Your total pipeline (STT final + LLM first token + TTS first audio chunk) needs to land under 800ms-1s to feel natural. Know where every millisecond goes:
                    <ul>
                        <li>Network round trip to each provider</li>
                        <li>STT endpointing delay (deciding "user stopped talking")</li>
                        <li>LLM time-to-first-token</li>
                        <li>TTS time-to-first-audio-chunk</li>
                    </ul>
                </li>
                <li><strong>VAD (Voice Activity Detection)</strong> — the very first gate. Silero VAD (open source, runs locally) is the industry standard. It decides "is there speech in this audio frame right now" before anything else happens.</li>
                <li><strong>Endpointing</strong> — the genuinely hard problem. How do you know the user is <em>done</em> talking vs just pausing to think? Bolna, LiveKit, and Vapi all have tunable endpointing sensitivity for exactly this reason.</li>
                <li><strong>WebSockets</strong> — the backbone protocol. Telephony providers (Twilio Media Streams), STT providers (Deepgram), and TTS providers (ElevenLabs) all stream over websockets, not REST. If you're not comfortable with async websocket code in Python or Node, start here.</li>
            </ol>

            <div class="practical-demo">
                <h4>Practical Demo 1: Bare pipeline, no telephony</h4>
                <p>Build a CLI script: mic input → local Whisper or Deepgram API → GPT-4o-mini or Claude → ElevenLabs TTS → speaker output. Not streaming yet — just prove the full loop works and measure baseline latency at each stage. This is your control group for every optimization later.</p>
                <p><strong>Deliverable</strong>: a Python script <code>bare_loop.py</code> that logs <code>stt_latency</code>, <code>llm_latency</code>, <code>tts_latency</code> per turn.</p>
            </div>
        </section>

        <section id="phase-2" class="phase-card">
            <h2>PHASE 2 — STT (Speech-to-Text) Deep Dive (Week 1-2)</h2>
            <h3>Topics</h3>
            <ol>
                <li><strong>Deepgram streaming API</strong> (industry default for real-time) — websocket connection, interim vs final results, <code>nova-2</code>/<code>nova-3</code> model tiers, language detection.</li>
                <li><strong>AssemblyAI</strong> — comparable alternative, slightly different latency/accuracy tradeoffs.</li>
                <li><strong>Whisper</strong> (OpenAI, local or API) — best accuracy, but NOT built for streaming natively; people wrap it in chunked-inference hacks. Understand why this makes it a poor fit for live calls vs good fit for post-call transcription/analytics.</li>
                <li><strong>Language + accent handling</strong> — since you're building for Indian GTM contexts, look specifically at Hindi/Hinglish code-switching support. Deepgram and Sarvam AI (Indian STT/TTS specialist) both have relevant multilingual models — worth comparing directly since FireReach's market context is India.</li>
                <li><strong>Interim results architecture</strong> — how do you feed <em>partial</em> transcripts to the LLM without triggering a premature response? (Answer: you don't feed interims to the LLM — you use them only to detect "user is still talking" for barge-in purposes. Only <em>final</em> transcripts go to the LLM.)</li>
            </ol>
            <div class="practical-demo">
                <h4>Practical Demo 2: Swap in real-time streaming STT</h4>
                <p>Replace your CLI mic input with a live Deepgram websocket stream. Print interim results as they arrive (you'll see the transcript "growing" word by word), then trigger your LLM call only on the final result. Log time from "user stopped speaking" to "final transcript received" — this is your endpointing latency.</p>
            </div>
        </section>

        <section id="phase-3" class="phase-card">
            <h2>PHASE 3 — TTS (Text-to-Speech) Deep Dive (Week 2)</h2>
            <h3>Topics</h3>
            <ol>
                <li><strong>ElevenLabs streaming</strong> — <code>eleven_turbo_v2_5</code> / <code>flash_v2_5</code> models are built for latency (~150-300ms to first chunk) vs their higher-quality models which are slower. Understand the quality/speed tradeoff dial.</li>
                <li><strong>Cartesia</strong> — newer entrant, often benchmarks as the lowest-latency TTS available right now; worth testing head-to-head against ElevenLabs.</li>
                <li><strong>PlayHT, Deepgram Aura, AWS Polly, XTTS (open source/self-hosted)</strong> — the wider provider landscape Bolna itself supports natively.</li>
                <li><strong>Voice cloning</strong> — ElevenLabs' instant voice cloning (few seconds of sample audio) vs professional cloning (higher quality, needs more samples). Relevant if FireAgent ever needs a consistent branded voice.</li>
                <li><strong>Chunked/streaming synthesis</strong> — TTS providers let you stream text <em>in</em> (as the LLM generates it) and get audio <em>out</em> in chunks, rather than waiting for the full LLM response before starting synthesis. This single optimization is often the biggest perceived-latency win in the whole pipeline.</li>
            </ol>
            <div class="practical-demo">
                <h4>Practical Demo 3: Streaming TTS playback</h4>
                <p>Feed your LLM's streamed token output directly into ElevenLabs' streaming endpoint sentence-by-sentence (don't wait for the full response), and play audio chunks as they arrive rather than waiting for the complete clip. Compare the "feel" against Phase 1's blocking version — this is the single most noticeable UX upgrade you'll build.</p>
            </div>
        </section>

        <section id="phase-4" class="phase-card">
            <h2>PHASE 4 — Turn-Taking & Interruption Handling (Week 2-3)</h2>
            <p><strong>This is the hardest phase and the one that separates toy demos from real products.</strong></p>
            <h3>Topics</h3>
            <ol>
                <li><strong>The state machine</strong>: <code>LISTENING → THINKING → SPEAKING → INTERRUPTED → LISTENING</code>. Every voice agent framework, including Bolna's <code>TaskManager</code>, is built around some version of this.</li>
                <li><strong>Barge-in</strong> — user starts talking while the AI is mid-sentence. You must: (a) detect this via VAD/interim STT within ~100-200ms, (b) immediately stop audio playback, (c) cancel the in-flight LLM generation, (d) cancel any in-flight TTS synthesis, (e) start listening to the new input. All four cancellations need to happen atomically or you get overlapping audio (the classic "broken voice bot" symptom).</li>
                <li><strong>Filler phrases / thinking sounds</strong> — Bolna explicitly implements this: while the LLM is generating (which can take 500ms-2s for complex responses), play a short "mm-hmm" or "let me check that" filler so the silence doesn't feel like a dead connection.</li>
                <li><strong>Async task cancellation in Python</strong> — <code>asyncio.Task.cancel()</code>, queue-based architectures. Bolna's core <code>TaskManager</code> coordinates STT/LLM/TTS stages through <code>asyncio</code> queues specifically so any stage can be killed mid-flight without corrupting the others.</li>
            </ol>
            <div class="practical-demo">
                <h4>Practical Demo 4: Build the interrupt handler</h4>
                <p>Take your Phase 3 pipeline and add: while TTS is playing, keep the STT websocket open and listening. If new speech is detected, immediately kill audio playback, cancel the LLM stream, and cancel TTS synthesis, then re-enter listening state. Test this by talking over your own AI mid-sentence — if it doesn't stop within ~200ms, your cancellation logic is wrong.</p>
            </div>
        </section>

        <section id="phase-5" class="phase-card">
            <h2>PHASE 5 — Telephony Layer (Week 3-4)</h2>
            <h3>Topics</h3>
            <ol>
                <li><strong>Twilio Voice + Media Streams</strong> — the most common way voice AI reaches an actual phone number. Media Streams opens a websocket that streams raw audio both directions during a live call.</li>
                <li><strong>SIP trunking basics</strong> — what's actually happening under the hood when Bolna/Vapi connect to Twilio/Plivo/Exotel. You don't need to build your own SIP stack, but understand what a trunk is and why bi-directional streaming support is the hard requirement for any telephony provider to work with these frameworks (Bolna's own docs explicitly call this out when discussing adding new providers).</li>
                <li><strong>Plivo, Exotel</strong> — the other two telephony providers Bolna supports natively; Exotel matters specifically for India-based calling (better local number support, pricing, compliance vs Twilio).</li>
                <li><strong>Audio format wrangling</strong> — telephony audio is typically 8kHz μ-law (mulaw), while STT/TTS providers often expect 16kHz/24kHz PCM. A huge chunk of "why doesn't this work" bugs in this space are audio format/sample-rate mismatches at the telephony boundary.</li>
            </ol>
            <div class="practical-demo">
                <h4>Practical Demo 5: Real phone number, real call</h4>
                <p>Get a Twilio trial number, set up Media Streams pointed at your websocket server (ngrok for local testing), and route the incoming audio through your Phase 4 pipeline. Call the number from your own phone. You now have a voice AI agent answering real phone calls.</p>
            </div>
        </section>

        <section id="phase-6" class="phase-card">
            <h2>PHASE 6 — LiveKit Specifically (Week 4)</h2>
            <h3>Topics</h3>
            <ol>
                <li><strong>WebRTC fundamentals</strong> — LiveKit is built on WebRTC, not raw websockets. Understand the difference: WebRTC is peer-to-peer-oriented (with SFU media routing for scale), built for browser-native low-latency media, and handles NAT traversal/jitter buffering/packet loss concealment automatically — all things you'd otherwise hand-roll with raw websockets.</li>
                <li><strong>LiveKit Agents SDK (Python/Node)</strong> — abstracts most of Phase 1-4 for you: it has built-in VAD, turn-detection, and interruption handling as configurable plugins rather than code you write yourself.</li>
                <li><strong>Room/participant/track model</strong> — LiveKit's core abstraction: a "room" has "participants," each publishing/subscribing "tracks" (audio/video/data). Your AI agent is just another participant that happens to be a bot.</li>
                <li><strong>When to use LiveKit vs Twilio</strong> — LiveKit shines for browser-based or Zoom/Meet-style experiences (like Tough Tongue's "join Zoom/Meet" capability). Twilio/Plivo shine for pure PSTN phone-number calling. Many production stacks (see the "Mesh Pilot" example in the GitHub ecosystem) actually combine LiveKit for the agent runtime with Twilio/SIP underneath for the actual PSTN leg.</li>
            </ol>
            <div class="practical-demo">
                <h4>Practical Demo 6: Rebuild Phase 4 on LiveKit</h4>
                <p>Install the LiveKit Agents SDK, rebuild your interrupt-handling agent using its built-in VAD/turn-detection plugins instead of your hand-rolled state machine. Compare lines of code and actual interruption-response latency against your Phase 4 version.</p>
            </div>
        </section>

        <section id="phase-7" class="phase-card">
            <h2>PHASE 7 — Orchestration Layer (Week 5)</h2>
            <p><strong>This is what actually makes something "Bolna" instead of just "a script that makes calls."</strong></p>
            <h3>Topics</h3>
            <ol>
                <li><strong>Config-driven agent definition</strong> — Bolna's real API (this is literally how their Python SDK works):
<div class="code-block">
from bolna.assistant import Assistant
from bolna.models import Transcriber, Synthesizer, ElevenLabsConfig, LlmAgent, SimpleLlmAgent

assistant = Assistant(name="demo_agent")

transcriber = Transcriber(provider="deepgram", model="nova-2", stream=True, language="en")

llm_agent = LlmAgent(
    agent_type="simple_llm_agent",
    agent_flow_type="streaming",
    llm_config=SimpleLlmAgent(provider="openai", model="gpt-4o-mini", temperature=0.3),
)

synthesizer = Synthesizer(
    provider="elevenlabs",
    provider_config=ElevenLabsConfig(voice="George", voice_id="JBFqnCBsd6RMkjVDRZzb", model="eleven_turbo_v2_5"),
    stream=True,
    audio_format="wav",
)

assistant.add_task(
    task_type="conversation",
    llm_agent=llm_agent,
    transcriber=transcriber,
    synthesizer=synthesizer,
)
</div>
                Notice: every provider is swappable via config, not hardcoded. This is the actual "product" — a clean abstraction layer over STT/LLM/TTS providers, not the AI itself.</li>
                <li><strong>LiteLLM</strong> — Bolna uses this library specifically so <code>llm_config=SimpleLlmAgent(provider="openai", ...)</code> can become <code>provider="anthropic"</code> or <code>provider="azure"</code> with zero other code changes. Study LiteLLM directly — it's a reusable pattern for your own orchestration layer.</li>
                <li><strong>Function/tool calling mid-conversation</strong> — the LLM needs to call out to real systems mid-call: "check calendar availability," "look up this lead in the CRM," "log this call outcome." This is standard LLM tool-use, just triggered inside a live voice loop instead of a chat window.</li>
                <li><strong>Multi-agent / routing</strong> — Bolna's <code>enums.py</code> defines multiple agent types (conversational, extraction, summarization) — meaning a single call can route through different specialized "sub-agents" depending on what stage of conversation you're in (e.g., a qualification agent handing off to a scheduling agent).</li>
                <li><strong>Concurrency</strong> — one event loop needs to serve N simultaneous calls. This is where <code>asyncio</code> architecture really matters — a blocking call anywhere in your pipeline stalls every other concurrent conversation.</li>
            </ol>
            <div class="practical-demo">
                <h4>Practical Demo 7: Build your own config schema</h4>
                <p>Design a JSON/YAML schema so you can spin up a new agent persona — different system prompt, different voice, different tools — purely by editing config, with zero code changes. Test it by creating two distinct personas (e.g., "FireReach SDR qualifying a lead" vs "FireReach demo booking assistant") from the same codebase.</p>
            </div>
        </section>

        <section id="phase-8" class="phase-card">
            <h2>PHASE 8 — Observability, Evaluation & Cost (Week 5-6)</h2>
            <h3>Topics</h3>
            <ol>
                <li><strong>Latency tracking per stage</strong> — Bolna explicitly tracks ASR/LLM/TTS latency separately per call (this is a first-class feature, not an afterthought) because when something feels slow, you need to know <em>which</em> stage regressed.</li>
                <li><strong>Call recording + transcript storage</strong> — needed for both debugging and any coaching/scoring product layer.</li>
                <li><strong>Scoring rubrics</strong> (the Tough Tongue/Hyperbound layer) — talk/listen ratio, filler word count, objection-handling detection, sentiment over time. This is genuinely a separate ML/prompt-engineering problem layered on top of the raw transcript, not something the voice pipeline gives you for free.</li>
                <li><strong>Cost modeling</strong> — every provider charges per-minute or per-character: STT (~$0.01-0.05/min), LLM (per-token, scales with conversation length and system prompt size), TTS (~$0.05-0.30/min), telephony (~$0.01-0.02/min). A single 5-minute qualification call can cost $0.50-$2 all-in — model this before you scale to hundreds of calls/day.</li>
                <li><strong>Caching & optimization</strong> — Bolna implements response caching for common phrases/greetings specifically to shave latency and cost on repeated patterns — worth studying as a concrete optimization technique.</li>
            </ol>
            <div class="practical-demo">
                <h4>Practical Demo 8: Build a call dashboard</h4>
                <p>Log per-call: total latency breakdown (STT/LLM/TTS), full transcript, cost breakdown, and a basic sentiment tag (even a simple LLM-based post-call classifier). This is your MVP of the "product layer" that separates raw infra from something you'd actually deploy for FireReach outbound calling.</p>
            </div>
        </section>

        <section id="competitors">
            <h2>Competitor Reference Map (who to study, in what order)</h2>
            <p><strong>Study in this order — infra first, product layer second:</strong></p>
            <ol>
                <li><strong>Bolna</strong> (github.com/bolna-ai/bolna) — read this first. Fully open source, real production code, JSON-config pattern, uses LiteLLM for provider abstraction. Closest match to what you're trying to clone. Also check <code>deepwiki.com/bolna-ai/bolna</code> for an architecture-diagram walkthrough of their actual codebase.</li>
                <li><strong>LiveKit Agents</strong> (docs.livekit.io/agents) — compare their approach to turn-taking/interruption against Bolna's. Different abstraction philosophy (WebRTC/room-based vs telephony-websocket-based).</li>
                <li><strong>Pipecat</strong> — another open-source pipeline/orchestration framework, worth a side-by-side read against Bolna for a second perspective on the same problem.</li>
                <li><strong>Vapi / Retell AI</strong> — managed, closed-source equivalents. Read their docs (not code) to see how much of Phase 1-6 they hide behind a dashboard — useful for understanding what "managed" actually buys a customer.</li>
                <li><strong>Dograh</strong> — newer open-source alternative positioned directly against Bolna; worth comparing their architecture doc if you want a second open-source reference implementation.</li>
            </ol>
            <p><strong>Product-layer competitors (study after infra, optional for FireReach):</strong></p>
            <ol start="6">
                <li><strong>Tough Tongue AI</strong> — roleplay/coaching + AI SDR calling combined. No-code scenario builder, audio-first processing (analyzes raw waveform, not just transcribed text, for tone/hesitation detection).</li>
                <li><strong>Hyperbound</strong> — narrower: high-volume SDR cold-call practice specifically, ICP-mirrored buyer personas.</li>
                <li><strong>Second Nature</strong> — enterprise/LMS-integrated, 3D avatars, more rigid template-based scenarios.</li>
                <li><strong>Yoodli</strong> — public-speaking coach pivoted into sales enablement, more solo-practice tool than team platform.</li>
                <li><strong>Synthflow / Bland AI / Air AI</strong> — pure AI SDR outbound calling automation, no coaching/roleplay layer — closest to what FireAgent's outbound calling feature would actually need if you skip the training/roleplay angle entirely.</li>
            </ol>
        </section>

        <section id="pace">
            <h2>Suggested Week-by-Week Pace</h2>
            <table>
                <thead>
                    <tr>
                        <th>Week</th>
                        <th>Focus</th>
                        <th>Output</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>1</td>
                        <td>Phase 1 + 2</td>
                        <td>Bare pipeline + real-time STT streaming</td>
                    </tr>
                    <tr>
                        <td>2</td>
                        <td>Phase 3 + start Phase 4</td>
                        <td>Streaming TTS + basic interrupt detection</td>
                    </tr>
                    <tr>
                        <td>3</td>
                        <td>Finish Phase 4 + Phase 5</td>
                        <td>Full barge-in handling + live Twilio phone number</td>
                    </tr>
                    <tr>
                        <td>4</td>
                        <td>Phase 6</td>
                        <td>LiveKit rebuild, side-by-side comparison</td>
                    </tr>
                    <tr>
                        <td>5</td>
                        <td>Phase 7</td>
                        <td>Config-driven multi-persona agent</td>
                    </tr>
                    <tr>
                        <td>5-6</td>
                        <td>Phase 8</td>
                        <td>Cost/latency/transcript dashboard — MVP complete</td>
                    </tr>
                </tbody>
            </table>
            <p>By end of Week 6 you'll have a working, config-driven, interruption-handling, telephony-connected voice agent with observability — which is genuinely Bolna-tier, built by you, understood end to end.</p>
        </section>
        
        <section id="next-steps">
            <h2>What I can build with you next</h2>
            <ul>
                <li>Actual working code for any single phase (start with Phase 1's <code>bare_loop.py</code>)</li>
                <li>A deeper technical breakdown of Bolna's <code>TaskManager</code> async queue architecture specifically</li>
                <li>A cost model spreadsheet for FireAgent's projected outbound call volume add all tis</li>
            </ul>
        </section>
    </div>
</body>
</html>"""
    
    file_path = os.path.join(os.path.dirname(__file__), 'voice_ai_curriculum.html')
    with open(file_path, 'w') as f:
        f.write(html_content)
    
    print(f"Generated {file_path}")

if __name__ == "__main__":
    generate_voice_ai_curriculum()
