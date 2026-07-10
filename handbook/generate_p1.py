import re

html_path = "/Users/bhoomim/devops CI:CD/handbook/ai_agents_observability.html"
with open(html_path, "r") as f:
    content = f.read()

# Remove the generic t2-t11 from getTopicTheory (lines 853-855) so they don't show up twice
# Actually let's just leave the string fallback in getTopicTheory, but add to RICH_TOPICS.
# If it's in RICH_TOPICS, showTopic uses it instead of getTopicTheory.

t2_to_t4 = """
  t2: {
    tag:'Core Concept · AI Fundamentals', num:2, title:'Agent vs Chatbot vs Automation', desc:'Understanding the boundaries between simple automation, LLM chatbots, and autonomous agents.',
    theory:`<div class="card"><h3>⚖️ Agent vs Chatbot vs Automation</h3><table><tr><th>Dimension</th><th>🤖 Chatbot</th><th>⚙️ Automation</th><th>🧠 Agent</th></tr><tr><td>Decision Logic</td><td>Pattern / LLM text</td><td>Hardcoded rules</td><td>Reasoning + Planning</td></tr><tr><td>Goal</td><td>Answer questions</td><td>Execute defined tasks</td><td>Achieve complex goals</td></tr><tr><td>Tool Use</td><td>None or minimal</td><td>Fixed predefined</td><td>Dynamic selection</td></tr><tr><td>Handles Unknown</td><td>Responds w/ uncertainty</td><td>Fails/errors</td><td>Reasons and adapts</td></tr></table><div class="box b-cy"><h5>💡 When to Use Each</h5><p><strong>Chatbot</strong>: FAQ, conversational tasks<br><strong>Automation</strong>: Repetitive, predictable workflows<br><strong>Agent</strong>: Dynamic, multi-step, real-world tool use</p></div></div>`,
    mcqs:[
      {q:"What is the defining trait of an automation compared to an agent?",opts:["A. Autonomy","B. Hardcoded rules","C. Uses LLMs","D. Requires internet"],ans:1,exp:"Automations use hardcoded rules (if X then Y). Agents use dynamic reasoning."},
      {q:"Chatbots primarily focus on:",opts:["A. Taking complex actions","B. Managing databases","C. Conversational text generation","D. System administration"],ans:2,exp:"Chatbots generate conversational text but lack deep goal-oriented action planning."},
      {q:"Which system is best for a highly predictable, repetitive task?",opts:["A. AI Agent","B. Chatbot","C. Traditional Automation","D. ReAct Loop"],ans:2,exp:"Traditional automation is faster, cheaper, and more reliable for completely predictable tasks."},
      {q:"When an unknown edge case occurs, a traditional automation typically:",opts:["A. Solves it","B. Fails or throws an error","C. Asks the user","D. Uses an LLM to guess"],ans:1,exp:"Automations fail on unhandled edge cases. Agents attempt to reason through them."},
      {q:"An agent differs from a chatbot mainly because the agent:",opts:["A. Has a better UI","B. Uses GPT-4","C. Can plan and use tools autonomously to change the environment","D. Is faster"],ans:2,exp:"Agents have agency (tool use, planning, taking action)."},
      {q:"Which of these is a typical agent task?",opts:["A. Translate this text","B. Summarize this article","C. Research competitors, build a CSV, and email it","D. Respond to 'Hello'"],ans:2,exp:"Agents handle multi-step, tool-dependent tasks."},
      {q:"If a workflow requires 100% deterministic execution, you should use:",opts:["A. CoT Agent","B. Traditional Automation","C. ReAct Agent","D. AutoGPT"],ans:1,exp:"Agents are non-deterministic (probabilistic). Automations are 100% deterministic."},
      {q:"Which system has the highest execution cost?",opts:["A. Python script","B. Zapier workflow","C. Autonomous Agent","D. Bash script"],ans:2,exp:"Agents require repeated LLM API calls, making them the most expensive."},
      {q:"Tool selection in an agent is:",opts:["A. Static","B. Dynamic based on reasoning","C. Random","D. Manual only"],ans:1,exp:"Agents dynamically choose tools based on the current context and goal."},
      {q:"A system that books flights, updates calendar, and emails friends is best built as:",opts:["A. A simple Chatbot","B. An AI Agent","C. A SQL query","D. A static website"],ans:1,exp:"This requires multi-step planning and interacting with multiple external APIs."},
      {q:"LLMs in chatbots vs agents:",opts:["A. Different models","B. Chatbots use LLMs for text; Agents use LLMs for reasoning and tool selection","C. Agents don't use LLMs","D. Chatbots are smarter"],ans:1,exp:"In agents, the LLM is the reasoning/routing engine, not just a text generator."},
      {q:"Which metric is least relevant to traditional automation but critical to agents?",opts:["A. Uptime","B. Hallucination rate","C. Execution speed","D. Memory usage"],ans:1,exp:"Automations don't hallucinate; agents do, making hallucination rate critical."},
      {q:"If you ask a chatbot to 'delete my database', it will:",opts:["A. Delete it","B. Tell you how to delete it","C. Crash","D. Write a SQL script and run it"],ans:1,exp:"Chatbots lack the 'actuators' or tools to actually perform the action."},
      {q:"Why might an agent be slower than an automation?",opts:["A. Network latency","B. Iterative LLM reasoning loops take time","C. Bad code","D. Language choice"],ans:1,exp:"Each step in an agent requires an LLM call which takes seconds to generate."},
      {q:"The best approach for building a customer support system is:",opts:["A. Pure Agent","B. Pure Automation","C. Hybrid (Automation for simple, Agent for complex)","D. Pure Chatbot"],ans:2,exp:"Hybrids optimize cost, speed, and capability."}
    ],
    flows:[
      {title:"Automation Logic",items:["start:Trigger","dec:If A","proc:Action X","dec:If B","proc:Action Y","end:Done"]},
      {title:"Chatbot Logic",items:["start:User Input","proc:Context Retrieval","proc:LLM Generation","end:Text Output"]},
      {title:"Agent Logic",items:["start:Goal","proc:Observe","proc:Reason (LLM)","proc:Act (Tool)","dec:Goal Met?","end:Finish"]}
    ],
    game:{icon:"⚖️",title:"System Architect",desc:"Choose the right system for the job",badges:["⚙️ Automator","🤖 Bot Builder","🧠 Agent Architect"],challenges:[{icon:"📝",title:"Identify",desc:"List 3 chatbot use cases",xp:50},{icon:"⚙️",title:"Automate",desc:"List 3 automation use cases",xp:50},{icon:"🧠",title:"Agentify",desc:"List 3 agent use cases",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 12+ on MCQs",xp:100}]},
    project:{title:"Hybrid System Design",badge:"Architect",desc:"Design a system combining automation, chatbots, and agents.",tags:["Design","Architecture"],steps:[{title:"Define Problem",desc:"Customer return processing"},{title:"Automation Layer",desc:"Webhooks for DB updates"},{title:"Chatbot Layer",desc:"FAQ answering"},{title:"Agent Layer",desc:"Complex return policy reasoning and tool execution"}],code:`# Pseudocode for Hybrid System\ndef handle_request(req):\n    if is_simple_faq(req):\n        return chatbot.answer(req)\n    elif is_standard_return(req):\n        return automation.process_return(req)\n    else:\n        return agent.resolve_complex_issue(req)`}
  },
  t3: {
    tag:'Core Concept · AI Fundamentals', num:3, title:'6 Core Agent Components', desc:'The anatomy of an AI Agent: Perception, Memory, Reasoning, Tools, Action, Output.',
    theory:`<div class="card"><h3>🔬 6 Core Agent Components</h3><table><tr><th>Component</th><th>Analogy</th><th>Tech</th></tr><tr><td>Perception</td><td>Eyes &amp; Ears</td><td>Input parsers, webhooks</td></tr><tr><td>Memory</td><td>Working/Long-term</td><td>Redis, Pinecone, messages[]</td></tr><tr><td>Reasoning Engine</td><td>Brain</td><td>GPT-4, Claude, Gemini</td></tr><tr><td>Tool Registry</td><td>Hands &amp; Tools</td><td>JSON tool definitions</td></tr><tr><td>Action Executor</td><td>Muscles</td><td>Function calls, API calls</td></tr><tr><td>Output Generator</td><td>Voice &amp; Mouth</td><td>Response formatter</td></tr></table><div class="cb"><span class="ck">class</span> <span class="cv">AIAgent</span>:
    <span class="ck">def</span> __init__(self):
        self.memory = Memory()
        self.tools = ToolRegistry()
        self.llm = ReasoningEngine()</div></div>`,
    mcqs:[
      {q:"Which component acts as the 'brain' of the agent?",opts:["A. Memory","B. Tool Registry","C. Reasoning Engine (LLM)","D. Action Executor"],ans:2,exp:"The LLM processes context and makes decisions, acting as the brain."},
      {q:"What does the 'Perception' component do?",opts:["A. Executes code","B. Stores data","C. Ingests and parses environment inputs","D. Generates text"],ans:2,exp:"Perception involves receiving user inputs, webhook events, or sensor data."},
      {q:"The Tool Registry is analogous to:",opts:["A. Eyes","B. Brain","C. A toolbox or hands","D. Voice"],ans:2,exp:"Tools are the capabilities the agent can use to affect the world."},
      {q:"Short-term memory in an agent is typically implemented as:",opts:["A. A SQL database","B. The conversational message history context","C. A vector database","D. A hard drive"],ans:1,exp:"Working memory is the immediate message list passed to the LLM."},
      {q:"Long-term memory is often implemented using:",opts:["A. RAM","B. Vector databases (RAG)","C. CPU cache","D. Message history"],ans:1,exp:"Vector databases store vast amounts of past knowledge for semantic retrieval."},
      {q:"The Action Executor is responsible for:",opts:["A. Thinking about what to do","B. Actually calling the API or running the function","C. Formatting the final output","D. Storing logs"],ans:1,exp:"Once the LLM decides on a tool, the executor runs the actual code."},
      {q:"Why is the Output Generator important?",opts:["A. It makes the LLM faster","B. It formats the final result for the user (e.g., Markdown, JSON)","C. It connects to the internet","D. It stores memory"],ans:1,exp:"The generator takes the final state and creates a user-friendly response."},
      {q:"Which component is most likely to use JSON Schema?",opts:["A. Perception","B. Memory","C. Tool Registry","D. Output Generator"],ans:2,exp:"Tools are defined using JSON Schema so the LLM understands their parameters."},
      {q:"If an agent fails to remember a fact from 3 weeks ago, which component failed?",opts:["A. Short-term memory","B. Long-term memory / Retrieval","C. Action Executor","D. Tool Registry"],ans:1,exp:"Long-term memory handles distant historical context."},
      {q:"If an agent decides to search the web but the code throws a 404 error, which component failed?",opts:["A. Reasoning Engine","B. Tool Registry","C. Action Executor","D. Perception"],ans:2,exp:"The executor runs the tool code, so network/execution errors happen here."},
      {q:"The Reasoning Engine is entirely dependent on:",opts:["A. The quality of the prompt and context (Memory + Perception)","B. The speed of the CPU","C. The database size","D. The user's internet connection"],ans:0,exp:"Garbage in, garbage out. The LLM needs good context to reason well."},
      {q:"A Vector Database belongs to which component?",opts:["A. Reasoning","B. Memory","C. Tools","D. Perception"],ans:1,exp:"Vector DBs are used for semantic long-term memory retrieval."},
      {q:"Which component converts a user's voice audio into text for the agent?",opts:["A. Perception","B. Memory","C. Action","D. Reasoning"],ans:0,exp:"Perception processes raw inputs into usable data."},
      {q:"Can an agent have multiple Reasoning Engines?",opts:["A. No, impossible","B. Yes, multi-agent systems use different LLMs for different tasks","C. Only if they are the exact same model","D. Yes, but it slows them down 100x"],ans:1,exp:"Complex agents often route tasks to different LLMs (e.g., a fast model for routing, a smart model for coding)."},
      {q:"The integration of all 6 components forms:",opts:["A. A chatbot","B. An Agent Architecture / Execution Loop","C. A vector database","D. A prompt"],ans:1,exp:"These components operate together in a loop to create agency."}
    ],
    flows:[
      {title:"Component Interaction",items:["start:Perception","proc:Memory Retrieval","proc:Reasoning Engine","proc:Tool Selection","proc:Action Execution","end:Output Generation"]},
      {title:"Memory Flow",items:["start:Input","proc:Query Short-term","proc:Query Long-term","proc:Inject to Context","end:Send to LLM"]},
      {title:"Action Flow",items:["start:LLM Decision","proc:Parse JSON Args","proc:Validate against Schema","proc:Execute Function","end:Return Result to Memory"]}
    ],
    game:{icon:"🔬",title:"Anatomy Lab",desc:"Master the 6 components of an agent",badges:["👀 Perceiver","🧠 Mastermind","🛠️ Tinkerer"],challenges:[{icon:"🧩",title:"Matchmaker",desc:"Match components to analogies",xp:50},{icon:"📝",title:"List 'em",desc:"Name all 6 components",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 12+ on MCQs",xp:100}]},
    project:{title:"Component Scaffold",badge:"Builder",desc:"Create a python class structure with the 6 components.",tags:["Python","Architecture"],steps:[{title:"Define Classes",desc:"Create dummy classes for each component"},{title:"Agent Class",desc:"Create main AIAgent class composing them"},{title:"Run Method",desc:"Wire them together in a run() method"}],code:`class Perception:\n    def parse(self, input): return input\nclass Memory:\n    def get_context(self): return []\nclass ReasoningEngine:\n    def think(self, ctx): return "action"\nclass ToolRegistry:\n    def get_tool(self, name): return lambda x: x\nclass ActionExecutor:\n    def run(self, tool): return "result"\nclass OutputGenerator:\n    def format(self, res): return res\n\nclass AIAgent:\n    def __init__(self):\n        self.p, self.m, self.r, self.t, self.a, self.o = Perception(), Memory(), ReasoningEngine(), ToolRegistry(), ActionExecutor(), OutputGenerator()\n    def run(self, user_input):\n        ctx = self.m.get_context() + [self.p.parse(user_input)]\n        decision = self.r.think(ctx)\n        return self.o.format(decision)`}
  },
  t4: {
    tag:'Core Concept · AI Fundamentals', num:4, title:'Anatomy of Agent Memory', desc:'Short-term, Long-term, and Episodic memory. How agents remember context across complex tasks.',
    theory:`<div class="card"><h3>🧠 Types of Agent Memory</h3><table><tr><th>Type</th><th>Description</th><th>Implementation</th></tr><tr><td>Short-Term (Working)</td><td>Current context window</td><td>Array of message dicts</td></tr><tr><td>Long-Term</td><td>Factual knowledge retrieval</td><td>Vector Database (RAG)</td></tr><tr><td>Episodic</td><td>Memory of past actions/tasks</td><td>Logs / DB records</td></tr><tr><td>Semantic</td><td>General world knowledge</td><td>Baked into LLM weights</td></tr></table><div class="box b-am"><h5>⚠️ The Context Limit Problem</h5><p>LLMs have finite context windows (e.g., 128k tokens). If short-term memory grows too large, the agent forgets early instructions, slows down, and costs increase. <strong>Solution:</strong> Summarization &amp; Eviction.</p></div></div>`,
    mcqs:[
      {q:"What is Short-Term memory in an agent?",opts:["A. The hard drive","B. The current conversation context window","C. The vector database","D. The model weights"],ans:1,exp:"Short-term memory is the immediate list of messages (context window) passed to the LLM."},
      {q:"Long-Term memory is primarily used for:",opts:["A. Storing the immediate last message","B. Retrieving facts and documents from a large corpus","C. Generating random numbers","D. Running Python code"],ans:1,exp:"Long-term memory uses RAG to retrieve relevant facts from vast data stores."},
      {q:"Episodic memory refers to:",opts:["A. Remembering past tasks and experiences","B. Knowing facts like 'Paris is in France'","C. The current user prompt","D. Model weights"],ans:0,exp:"Episodic memory recalls specific past episodes or interactions."},
      {q:"Semantic memory is usually:",opts:["A. Stored in Redis","B. Baked into the LLM's pre-trained weights","C. Stored in localstorage","D. User provided"],ans:1,exp:"Semantic memory is the general world knowledge the model learned during training."},
      {q:"What happens when short-term memory exceeds the LLM context window?",opts:["A. The LLM gets smarter","B. The API returns an error or early tokens are truncated","C. The LLM automatically uses a vector DB","D. The agent works faster"],ans:1,exp:"Context limits are hard limits. Exceeding them causes errors or loss of early context."},
      {q:"Which is a strategy to manage growing short-term memory?",opts:["A. Buy more RAM","B. Summarize older messages and evict them","C. Delete the tool registry","D. Use a smaller LLM"],ans:1,exp:"Summarization compresses older context to save tokens while retaining meaning."},
      {q:"What technology is synonymous with Long-Term agent memory?",opts:["A. RAG (Retrieval-Augmented Generation)","B. CNNs","C. RNNs","D. HTML"],ans:0,exp:"RAG uses vector embeddings to retrieve relevant long-term memory."},
      {q:"If an agent needs to remember the user's preferences across sessions, it uses:",opts:["A. Short-term memory","B. Long-term / Persistent memory","C. Semantic memory","D. Episodic memory"],ans:1,exp:"Persistent memory (DB or Vector DB) is needed across different sessions."},
      {q:"Which memory type is updated continuously during a single task execution loop?",opts:["A. Semantic","B. Short-term / Working memory","C. Vector weights","D. Model architecture"],ans:1,exp:"Every thought, action, and observation is appended to working memory."},
      {q:"Memory eviction means:",opts:["A. Deleting the entire agent","B. Removing the oldest or least relevant items from the context window","C. Formatting the hard drive","D. Kicking users out"],ans:1,exp:"Eviction keeps the context window within limits."},
      {q:"Vector databases store data as:",opts:["A. JSON objects only","B. High-dimensional arrays of numbers (embeddings)","C. SQL tables","D. Plain text files"],ans:1,exp:"Embeddings capture semantic meaning as vectors."},
      {q:"Why not just put all long-term memory into the context window?",opts:["A. It's too expensive and exceeds token limits","B. It makes the LLM too smart","C. It's impossible","D. Vector DBs require it"],ans:0,exp:"Large context windows cost more per API call and have hard token limits."},
      {q:"An agent remembering that it failed a similar coding task yesterday is an example of:",opts:["A. Semantic memory","B. Episodic memory","C. Short-term memory","D. Cache"],ans:1,exp:"Recalling a specific past event is episodic memory."},
      {q:"The most common format for working memory in OpenAI's API is:",opts:["A. A single long string","B. A list of message dictionaries (role/content)","C. A binary file","D. A CSV array"],ans:1,exp:"The Chat Completions API uses an array of role-based message objects."},
      {q:"Which helps an agent avoid repeating the same mistake?",opts:["A. Deleting memory","B. Reflection and appending the failure to episodic/working memory","C. Using a smaller context window","D. Randomizing temperature"],ans:1,exp:"Reflecting on mistakes and storing them in memory prevents repetition."}
    ],
    flows:[
      {title:"Memory Lifecycle",items:["start:User Input","proc:Add to Short-Term","proc:Agent Action","proc:Add Result to Short-Term","dec:Context Full?","proc:Summarize & Store in Long-Term","end:Continue"]},
      {title:"RAG Retrieval",items:["start:Query","proc:Embed Query","proc:Vector DB Search","proc:Retrieve Top-K","proc:Inject into Prompt","end:LLM Generation"]},
      {title:"Context Management",items:["start:Check Token Count","dec:> Limit?","proc:Extract Key Facts","proc:Replace Old Msgs with Summary","end:Ready for LLM"]}
    ],
    game:{icon:"💾",title:"Memory Master",desc:"Learn to manage tokens and context",badges:["📝 Note Taker","🧠 Recall Master","🗜️ Compressor"],challenges:[{icon:"📏",title:"Token Math",desc:"Calculate token usage for a 10-turn conversation",xp:50},{icon:"🗜️",title:"Summarize",desc:"Write a prompt to summarize memory",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 12+ on MCQs",xp:100}]},
    project:{title:"Memory Manager",badge:"Archivist",desc:"Implement a rolling-window memory manager with summarization.",tags:["Python","Memory Management"],steps:[{title:"List Setup",desc:"Create a list to hold messages"},{title:"Token Counter",desc:"Use tiktoken to count tokens"},{title:"Summarization Logic",desc:"If tokens > max, call LLM to summarize oldest 5 messages"},{title:"Replacement",desc:"Replace the 5 messages with 1 summary message"}],code:`import tiktoken\n\nclass MemoryManager:\n    def __init__(self, max_tokens=4000):\n        self.history = []\n        self.max_tokens = max_tokens\n        self.enc = tiktoken.get_encoding("cl100k_base")\n\n    def add(self, role, content):\n        self.history.append({"role": role, "content": content})\n        self.check_limits()\n\n    def check_limits(self):\n        tokens = sum(len(self.enc.encode(m["content"])) for m in self.history)\n        if tokens > self.max_tokens:\n            self.summarize_oldest()`}
  },
"""

insert_idx = content.find("t21: {")
new_content = content[:insert_idx] + t2_to_t4 + content[insert_idx:]

with open(html_path, "w") as f:
    f.write(new_content)
print("Done inserting t2-t4")
