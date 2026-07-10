import re

html_path = "/Users/bhoomim/devops CI:CD/handbook/fullstack_ai_handbook.html"
with open(html_path, "r") as f:
    content = f.read()

rich_content = r"""
  t161: {
    tag:'Phase 7 · Practical Scenarios', num:161,
    title:'The Twelve-Factor App',
    desc:'The gold standard methodology for building scalable, cloud-native applications.',
    theory:`<div class="card"><h3>📏 The Blueprint for the Cloud</h3><p>Building an app that runs on your laptop is easy. Building an app that scales to 1,000 servers on AWS requires strict discipline. The <strong>Twelve-Factor App</strong> methodology (created by Heroku) is a set of 12 rules for building modern web apps.</p><h4>Key Factors</h4><ul><li><strong>I. Codebase:</strong> One codebase tracked in revision control, many deploys.</li><li><strong>III. Config:</strong> Store config (API keys, DB URLs) in the environment, NOT in the code.</li><li><strong>VI. Processes:</strong> Execute the app as one or more stateless processes. Any data that needs to persist must be stored in a stateful backing service (like a Database or Cache).</li></ul></div>`,
    mcqs:[
      {q:"What is the primary goal of the Twelve-Factor App methodology?",opts:["A. To write less code","B. To provide a standardized set of best practices for building scalable, reliable, and maintainable cloud-native (SaaS) applications.","C. To eliminate databases","D. To enforce object-oriented programming"],ans:1,exp:"Apps that follow these rules are incredibly easy to deploy to Docker/Kubernetes."},
      {q:"According to Factor III (Config), where is the ONLY acceptable place to store configuration data like database passwords?",opts:["A. Hardcoded in a config.js file","B. In Environment Variables (ENV vars) injected at runtime by the host system.","C. In a public GitHub repo","D. In a separate microservice"],ans:1,exp:"This guarantees that the exact same Docker Image can be promoted from QA to Production without recompiling."},
      {q:"According to Factor VI (Processes), why must your application be completely 'Stateless'?",opts:["A. Because state is illegal","B. Because cloud servers are ephemeral. If your app saves user uploads to its local hard drive, and the server scales down or crashes, the data is lost forever.","C. Because it saves RAM","D. Because it makes the code run faster"],ans:1,exp:"If a process dies, it should have zero impact on the user. State belongs in a Database (RDS) or Object Storage (S3)."},
      {q:"What does Factor IV (Backing Services) dictate?",opts:["A. You should build your own databases","B. Treat external resources (Databases, Caches, SMTP servers) as attached resources. The app should make no distinction between a local Postgres DB and a managed AWS RDS DB.","C. Don't use databases","D. Only use local JSON files"],ans:1,exp:"If a database fails, you should be able to instantly swap the URL in the environment variables without changing a single line of code."},
      {q:"According to Factor IX (Disposability), how should your app handle startup and shutdown?",opts:["A. It should start slowly and never stop","B. Fast startup (to scale up quickly during traffic spikes) and graceful shutdown (to finish processing current requests before dying).","C. It should require human approval to start","D. It should take 10 minutes to boot"],ans:1,exp:"Kubernetes constantly kills and restarts containers. Your app must be ready for this."}
    ],
    flows:[
      {title:"Stateless Process Flow",items:["start:User uploads Profile Picture","dec:Bad App: Saves to local /images/ folder","proc:Server crashes -> Image permanently lost!","dec:12-Factor App: Saves to Amazon S3 (Backing Service)","end:Server crashes -> Image is safe on S3!"]}
    ],
    game:{icon:"📏",title:"The Disciplinarian",desc:"Master 12-Factor rules",badges:["📏 Architect","🧳 Stateless Traveler","💉 Env Injector"],challenges:[{icon:"📝",title:"Config",desc:"Why not hardcode API keys?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Factor III Audit",badge:"Auditor",desc:"Remove hardcoded config.",tags:["Best Practices","Env"],steps:[{title:"Bad Code",desc:"const db = 'mongodb://prod-server/db'"},{"title:"Good Code",desc:"const db = process.env.DB_URL"},{"title:"Benefit",desc:"Code is now safe to push to public GitHub."}],code:`// BAD: Hardcoded Configuration (Violates Factor III)\nconst DB_PASSWORD = "super_secret_production_password"; \n\n// GOOD: Twelve-Factor Configuration\n// The code is identical in Dev, Staging, and Prod.\n// The host system (AWS, Kubernetes, Vercel) injects the correct string at runtime.\nconst DB_PASSWORD = process.env.DB_PASSWORD;`}
  },
  t162: {
    tag:'Phase 7 · Practical Scenarios', num:162,
    title:'Distributed Transactions (Saga)',
    desc:'How to maintain data integrity across multiple independent microservices.',
    theory:`<div class="card"><h3>🔗 The Broken Chain</h3><p>In a Monolith, if a user buys an item, you wrap the Inventory update and the Billing update in a single SQL <code>TRANSACTION</code>. If Billing fails, Inventory instantly Rolls Back. This is easy.</p><h4>The Microservices Nightmare</h4><p>In Microservices, Inventory and Billing are different apps with different databases. You cannot use a standard SQL transaction. If Inventory succeeds, but Billing fails 2 seconds later... the user gets the item for free!</p><h4>The Saga Pattern</h4><p>To fix this, we use the <strong>Saga Pattern</strong>. A Saga is a sequence of local transactions. If Step 2 (Billing) fails, the system automatically triggers a <strong>Compensating Transaction</strong> (e.g., sending a message back to the Inventory service to 'Restock' the item), rolling back the operation manually.</p></div>`,
    mcqs:[
      {q:"Why are standard SQL Transactions (ACID) impossible in a true Microservices architecture?",opts:["A. SQL doesn't support transactions","B. Because each microservice has its own isolated database. There is no central database engine that can lock rows across both Postgres (Billing) and MongoDB (Inventory) simultaneously.","C. Microservices are too fast","D. Microservices don't use databases"],ans:1,exp:"This is one of the hardest technical challenges in modern software engineering."},
      {q:"What is the 'Saga Pattern'?",opts:["A. A long story","B. A design pattern for managing distributed transactions by breaking them into a sequence of local transactions, chained together by events/messages.","C. A caching strategy","D. A UI component"],ans:1,exp:"If all steps succeed, the Saga is complete. If one step fails, the Saga reverses itself."},
      {q:"In a Saga, what is a 'Compensating Transaction'?",opts:["A. Paying the developer more money","B. A specific, pre-written action designed to explicitly undo the work of a previous step if a failure occurs later in the chain (e.g., if 'Charge Card' fails, execute 'Restock Inventory').","C. A database backup","D. A successful SQL query"],ans:1,exp:"You cannot rely on the database to roll back automatically; you have to write code to do it."},
      {q:"What are the two main ways to orchestrate a Saga?",opts:["A. Fast and Slow","B. Choreography (Services publish events and react to each other like a dance) and Orchestration (A central 'Controller' service tells everyone exactly what to do).","C. Left and Right","D. Front and Back"],ans:1,exp:"Choreography is decentralized (harder to debug). Orchestration is centralized (easier to track)."},
      {q:"Why might a company choose to stick with a Monolith instead of migrating to Microservices?",opts:["A. Microservices are a fad","B. To completely avoid the massive engineering nightmare of dealing with Distributed Transactions, Eventual Consistency, and network failures.","C. Monoliths are faster on the internet","D. Monoliths use less electricity"],ans:1,exp:"As Martin Fowler said, don't use microservices unless the pain of the monolith is unbearable."}
    ],
    flows:[
      {title:"Saga Rollback Flow",items:["start:User Clicks Buy","proc:Step 1: InventoryService reserves Item (Success)","dec:Step 2: BillingService attempts Charge (FAIL: Card Denied!)","proc:Saga triggers Compensating Transaction!","end:Step 3: InventoryService restocks Item (Rollback Complete)"]}
    ],
    game:{icon:"🔗",title:"The Chain Weaver",desc:"Master distributed logic",badges:["🔗 Saga Weaver","🔙 Compensator","🎭 Choreographer"],challenges:[{icon:"📝",title:"The Nightmare",desc:"Why can't you use SQL BEGIN/COMMIT?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Compensating Action",badge:"Rollbacker",desc:"Design a compensation step.",tags:["Architecture","Logic"],steps:[{title:"Action",desc:"Book Flight"},{"title:"Action",desc:"Book Hotel"},{"title:"Action",desc:"Charge Card (Fails!) -> Compensate: Cancel Hotel, Cancel Flight"}],code:`// Pseudocode for an Orchestrated Saga
async function processOrderSaga(order) {
  try {
    await inventoryService.reserve(order.items);
    await shippingService.createLabel(order.address);
    await billingService.charge(order.user); // FAILS!
  } catch (error) {
    // Oh no! We must MANUALLY undo the previous successful steps!
    // These are Compensating Transactions.
    await shippingService.cancelLabel(order.address);
    await inventoryService.restock(order.items);
    throw new Error("Order Failed. Everything rolled back safely.");
  }
}`}
  },
  t163: {
    tag:'Phase 7 · Practical Scenarios', num:163,
    title:'Idempotency in API Design',
    desc:'Preventing catastrophic duplicate actions when networks inevitably fail.',
    theory:`<div class="card"><h3>🔁 The Safe Retry</h3><p>A user clicks "Pay $100". Their phone sends the request to the server. The server successfully charges the credit card. But then, right before the server can reply "Success", the user's internet drops! The user's phone thinks the request failed. What does the user do? They click "Pay" again! They just got charged $200.</p><h4>Idempotency</h4><p>An API endpoint is <strong>Idempotent</strong> if making the exact same request multiple times has the exact same effect as making it once. The frontend generates a unique <code>Idempotency-Key</code> (like a UUID) and sends it with the request. The server saves this key. If the user clicks "Pay" again with the same key, the server says, "I already processed this key! I will ignore the charge and just return Success."</p></div>`,
    mcqs:[
      {q:"What does it mean for an API operation to be 'Idempotent'?",opts:["A. It is very fast","B. Executing the operation 1 time has the exact same result/state as executing it 100 times. It prevents duplicate actions.","C. It only works on mobile devices","D. It deletes data immediately"],ans:1,exp:"Idempotency is critical for payment processing, creating resources, and sending emails."},
      {q:"Which HTTP methods are Idempotent by definition according to the REST standard?",opts:["A. POST and PATCH","B. GET, PUT, and DELETE","C. Only GET","D. None of them"],ans:1,exp:"If you DELETE user 5, they are gone. If you DELETE user 5 again, they are still gone. The end state is the same."},
      {q:"Why is the HTTP POST method generally NOT idempotent?",opts:["A. Because it is too slow","B. POST is used to create new resources. If you send a POST request to '/orders' 5 times, it will create 5 separate orders in the database.","C. Because it is encrypted","D. Because it only sends strings"],ans:1,exp:"This is why we must manually add Idempotency Keys to POST requests!"},
      {q:"How does an 'Idempotency Key' protect against network timeouts?",opts:["A. It speeds up the network","B. The client generates a unique UUID and attaches it to the request. The server checks if it has seen this key before. If yes, it skips the action and just returns the previous cached response.","C. It encrypts the payload","D. It restarts the server"],ans:1,exp:"Stripe requires an Idempotency-Key header on every single payment request for this exact reason."},
      {q:"If a client sends a payment request, the server charges the card, but the Wi-Fi drops before the server can send the HTTP 200 OK response... what happens next?",opts:["A. The money is refunded automatically","B. The client app will likely retry the request. If the endpoint is NOT idempotent, the user will be double-charged.","C. The database crashes","D. The server blocks the IP"],ans:1,exp:"Never assume a network is reliable."}
    ],
    flows:[
      {title:"Idempotent Retry Flow",items:["start:Client clicks 'Pay' -> Sends POST with Key: 999","proc:Server processes payment -> Saves Key: 999 to DB","dec:Network drops! Client thinks it failed!","proc:Client retries POST with Key: 999","end:Server sees Key 999 exists! Skips payment, returns 200 OK!"]}
    ],
    game:{icon:"🔁",title:"The Safecracker",desc:"Master Idempotency",badges:["🔁 Idempotent Thinker","🔑 UUID Generator","🛡️ Double-Charge Preventer"],challenges:[{icon:"📝",title:"HTTP Methods",desc:"Which method is NOT idempotent?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Idempotency Header",badge:"Header Hacker",desc:"Send an idempotency key.",tags:["API","Security"],steps:[{title:"Generate",desc:"const key = uuidv4()"},{"title:"Send",desc:"headers: { 'Idempotency-Key': key }"},{"title:"Server Logic",desc:"if (db.has(key)) return cachedResponse;"}],code:`// Server-side Idempotency Logic
app.post('/charge', async (req, res) => {
  const idempotencyKey = req.headers['idempotency-key'];

  // 1. Check if we already processed this exact request
  const previousCharge = await db.findChargeByKey(idempotencyKey);
  if (previousCharge) {
    // Return the cached success response. Do NOT charge the card again!
    return res.json({ status: "Success", message: "Already processed" });
  }

  // 2. Otherwise, process the new charge and save the key!
  await stripe.chargeCard(req.body.amount);
  await db.saveCharge(idempotencyKey, req.body);
  
  res.json({ status: "Success" });
});`}
  },
  t164: {
    tag:'Phase 7 · Practical Scenarios', num:164,
    title:'Securing APIs (CORS, CSRF, XSS)',
    desc:'The three most common web vulnerabilities and how to defend against them.',
    theory:`<div class="card"><h3>🛡️ The Cybersecurity Basics</h3><p>As a Full-Stack developer, your API will be attacked daily. You must understand the Big Three web vulnerabilities:</p><ul><li><strong>XSS (Cross-Site Scripting):</strong> A hacker injects malicious Javascript into a comment on your blog. When other users view the comment, the JS executes in their browser and steals their tokens. <em>Fix: Never use <code>innerHTML</code>, always sanitize user input.</em></li><li><strong>CSRF (Cross-Site Request Forgery):</strong> A hacker tricks a logged-in user into clicking a link that secretly sends a <code>POST /transfer_funds</code> request to their bank. <em>Fix: Use Anti-CSRF tokens or SameSite Cookies.</em></li><li><strong>CORS (Cross-Origin Resource Sharing):</strong> A browser security feature. If <code>evil.com</code> tries to fetch data from <code>api.yourbank.com</code> via AJAX, the browser blocks it unless the Bank explicitly whitelists <code>evil.com</code>.</li></ul></div>`,
    mcqs:[
      {q:"What is XSS (Cross-Site Scripting)?",opts:["A. Writing CSS across multiple files","B. A vulnerability where an attacker injects malicious executable Javascript into a trusted website, which then executes in the browsers of innocent users viewing that page.","C. A database injection attack","D. A server crash attack"],ans:1,exp:"React automatically protects against XSS by escaping text. But using dangerouslySetInnerHTML bypasses this protection!"},
      {q:"How do you successfully defend against XSS attacks?",opts:["A. Install antivirus software on the server","B. Sanitize all user input before saving it to the database, and strictly avoid injecting raw, unsanitized strings directly into the HTML DOM (e.g., using innerHTML).","C. Use a VPN","D. Encrypt the database"],ans:1,exp:"If a user types '<script>alert(1)</script>' as their username, it must be escaped to &lt;script&gt;."},
      {q:"What is CSRF (Cross-Site Request Forgery)?",opts:["A. Faking a network request","B. An attack that forces an end user to execute unwanted actions on a web application in which they are currently authenticated. (e.g., A trick link that transfers money).","C. Stealing passwords from a database","D. Brute-forcing a login screen"],ans:1,exp:"The attacker exploits the fact that the browser automatically sends the user's Session Cookies with the forged request."},
      {q:"What is the primary defense against CSRF attacks in modern web apps?",opts:["A. Two-Factor Authentication","B. Setting the 'SameSite=Strict' attribute on your Session Cookies, and utilizing unique Anti-CSRF tokens for every form submission.","C. Blocking all POST requests","D. Using shorter passwords"],ans:1,exp:"SameSite=Strict tells the browser: 'Never send this cookie if the request originated from a different domain'."},
      {q:"What is CORS (Cross-Origin Resource Sharing)?",opts:["A. A computer virus","B. A security mechanism built into web browsers that blocks a webpage on Domain A from making an AJAX request to an API on Domain B, unless Domain B explicitly returns headers allowing it.","C. A way to share databases","D. A CSS property"],ans:1,exp:"If your frontend is on localhost:3000 and your backend is on localhost:8080, the browser will block the request until you configure CORS on the backend!"}
    ],
    flows:[
      {title:"XSS Attack Flow",items:["start:Hacker posts comment: '<script>stealTokens()</script>'","proc:Server saves comment to Database (No sanitization)","dec:Victim visits the blog post","proc:Browser renders the raw <script> tag","end:Malicious JS executes! Victim's token is stolen!"]}
    ],
    game:{icon:"🛡️",title:"The Defender",desc:"Master web security",badges:["🛡️ XSS Sanitizer","🛑 CSRF Blocker","🌐 CORS Configurator"],challenges:[{icon:"📝",title:"SameSite",desc:"What does SameSite=Strict do?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"CORS Error",badge:"Debugger",desc:"Fix the most common developer error.",tags:["Security","API"],steps:[{title:"The Error",desc:"'Blocked by CORS policy: No Access-Control-Allow-Origin header is present'"},{"title:"The Fix (Node.js)",desc:"npm install cors"},{"title:"The Code",desc:"app.use(cors({ origin: 'https://myfrontend.com' }))"}],code:`// Fixing CORS in an Express.js Backend
const express = require('express');
const cors = require('cors');
const app = express();

// Without this, the browser will block requests coming from your React frontend!
app.use(cors({
  origin: 'https://my-react-app.com', // Only allow requests from THIS specific domain
  methods: ['GET', 'POST'],           // Only allow these methods
  credentials: true                   // Allow cookies to be sent across domains
}));`}
  },
  t165: {
    tag:'Phase 7 · Practical Scenarios', num:165,
    title:'Chaos Engineering',
    desc:'Intentionally breaking things in production to prove your system can survive.',
    theory:`<div class="card"><h3>🐒 Enter the Chaos Monkey</h3><p>You built your Microservices. You set up Kubernetes self-healing. You added database Read Replicas. Are you <em>sure</em> it works? What happens if an AWS datacenter goes offline at 3 PM on a Tuesday?</p><h4>Chaos Engineering</h4><p>Pioneered by Netflix, Chaos Engineering is the practice of intentionally injecting failures into a production system to test its resilience. Netflix built a tool called <strong>Chaos Monkey</strong> that randomly kills production servers during business hours. If the engineering team built the system correctly, the users won't notice a thing. This forces a culture of high availability.</p></div>`,
    mcqs:[
      {q:"What is the core philosophy of Chaos Engineering?",opts:["A. Writing chaotic, messy code","B. Proactively injecting controlled failures into a production system (like killing servers or dropping network packets) to discover weaknesses before they cause a massive, unplanned outage.","C. Firing developers randomly","D. Ignoring error logs"],ans:1,exp:"'Things will break. You can't prevent it. You can only prepare for it.'"},
      {q:"Who famously pioneered the concept of Chaos Engineering with a tool called 'Chaos Monkey'?",opts:["A. Google","B. Netflix","C. Amazon","D. Microsoft"],ans:1,exp:"Netflix realized that if their engineers knew a server could be randomly destroyed at any second, they would build incredibly resilient software."},
      {q:"If Chaos Monkey randomly terminates the primary Postgres Database server, what should happen in a well-architected system?",opts:["A. The website goes offline for 3 days","B. The system detects the failure instantly, automatically promotes a Read Replica to become the new Master, and continues serving users with zero (or minimal) downtime.","C. An intern has to drive to the datacenter","D. All user data is deleted"],ans:1,exp:"Chaos engineering proves that your auto-scaling and failover mechanisms actually work."},
      {q:"Why is Chaos Engineering typically performed during normal business hours?",opts:["A. Because it's fun to annoy users","B. Because if something goes horribly wrong and the failover doesn't work, all the engineers are currently awake, in the office, and ready to fix it immediately (unlike a 3 AM outage).","C. To save electricity","D. Because the servers are faster"],ans:1,exp:"You control the blast radius, and you control the timing."},
      {q:"What is a prerequisite before a company should even attempt Chaos Engineering?",opts:["A. A large budget","B. A highly automated, observable system (CI/CD, Kubernetes, distributed tracing, and alerts). If you are manually SSHing into servers, Chaos Engineering will just destroy your company.","C. 100% test coverage","D. A monolithic architecture"],ans:1,exp:"Chaos engineering is for mature DevOps organizations."}
    ],
    flows:[
      {title:"The Chaos Monkey Flow",items:["start:2:00 PM: Users are watching Netflix","proc:2:05 PM: Chaos Monkey randomly kills Server Node 4","dec:2:06 PM: K8s detects Node 4 is dead","proc:2:07 PM: K8s reschedules Pods to Node 5","end:Users experience 1 second of buffering. Success!"]}
    ],
    game:{icon:"🐒",title:"The Agent of Chaos",desc:"Master Chaos Engineering",badges:["🐒 Monkey Wrangler","🔥 Blast Radius Controller","🩹 Resilience Tester"],challenges:[{icon:"📝",title:"The Goal",desc:"Why break production intentionally?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Mental Resilience",badge:"Chaos Architect",desc:"Plan a Chaos Experiment.",tags:["DevOps","Testing"],steps:[{title:"Hypothesis",desc:"If the Redis Cache dies, the app will slow down but not crash."},{"title:"Execution",desc:"Terminate the Redis container in Production."},{"title:"Observation",desc:"Did the DB handle the load? Did the app survive?"}],code:`// The 4 Steps of a Chaos Experiment:
// 1. Define the 'Steady State' (e.g., 99% of requests succeed in < 100ms).
// 2. Hypothesize that the steady state will continue if a failure occurs.
// 3. Introduce the failure (kill a pod, spike the CPU).
// 4. Try to disprove the hypothesis. If the system fails, you found a bug!`}
  }
"""

start_marker = "};\n\nlet userXP"
inject_idx = content.find(start_marker)

if inject_idx != -1:
    new_content = content[:inject_idx] + ",\n" + rich_content + content[inject_idx:]
    with open(html_path, "w") as f:
        f.write(new_content)
    print("Successfully generated T161-T165 rich content!")
else:
    print("Could not find injection point.")
