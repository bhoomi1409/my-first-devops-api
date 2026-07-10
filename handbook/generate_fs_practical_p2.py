import re

html_path = "/Users/bhoomim/devops CI:CD/handbook/fullstack_ai_handbook.html"
with open(html_path, "r") as f:
    content = f.read()

rich_content = r"""
  t166: {
    tag:'Phase 7 · Practical Scenarios', num:166,
    title:'Feature Flags & Dark Launches',
    desc:'Decoupling code deployment from feature release to control risk.',
    theory:`<div class="card"><h3>🎛️ The Switchboard</h3><p>Historically, if you wanted to launch a new UI, you merged the code to <code>main</code> and deployed it. The moment it deployed, 100% of users saw the new UI. If it broke, you had to frantically write a fix and redeploy.</p><h4>Feature Flags</h4><p>A <strong>Feature Flag</strong> (or toggle) is a remote switch. You wrap the new UI code in an <code>if (featureEnabled)</code> statement. You deploy the code to production, but keep the flag <strong>OFF</strong>. The code is sitting in production ("Dark Launch"), but no users can see it. On launch day, a Product Manager simply clicks a button in a dashboard (like LaunchDarkly) turning the flag <strong>ON</strong>. The UI instantly appears for users without a deployment!</p></div>`,
    mcqs:[
      {q:"What is the primary benefit of using Feature Flags?",opts:["A. They make the code compile faster","B. They completely decouple the Deployment of code from the Release of a feature. You can deploy code into production weeks before it is actually 'turned on' for the user.","C. They write tests automatically","D. They prevent database errors"],ans:1,exp:"This drastically reduces the stress of a 'Release Day'."},
      {q:"What happens if you turn a Feature Flag ON for a massive new feature, and the server immediately starts crashing?",opts:["A. You have to write a patch and deploy it","B. You simply click the button in your Feature Flag dashboard to turn it OFF. The feature instantly vanishes, and the server recovers in milliseconds. No redeployment required.","C. You delete the database","D. You reboot the AWS servers"],ans:1,exp:"Feature flags provide the ultimate 'Kill Switch'."},
      {q:"What is a 'Dark Launch'?",opts:["A. Launching a dark mode UI","B. Deploying new backend code (like a new database query) behind a flag that executes alongside the old code, but silently throwing away the new results. This allows you to test the performance of the new code under real production traffic without impacting the user.","C. Launching without telling marketing","D. A cybersecurity attack"],ans:1,exp:"Once you confirm the new query doesn't crash the DB, you switch the flag to actually use the results."},
      {q:"How do Feature Flags enable targeted A/B Testing?",opts:["A. They generate fake data","B. You can configure the flag to turn ON for exactly 50% of users. You then measure which group (A or B) generates more revenue, and roll it out to 100% if successful.","C. They ask users questions","D. They change CSS colors randomly"],ans:1,exp:"Companies like Facebook run thousands of feature flags simultaneously."},
      {q:"What is 'Feature Flag Debt'?",opts:["A. The monetary cost of the service","B. The messy, unused 'if/else' statements left scattered throughout your codebase months after a feature was successfully launched to 100% of users. They must be cleaned up.","C. Unpaid developer bills","D. A database error"],ans:1,exp:"If a flag is permanent (like 'enable_admin_mode'), keep it. If it was temporary for a launch, delete it after a week."}
    ],
    flows:[
      {title:"Feature Flag Flow",items:["start:Dev wraps new Checkout flow in 'if(new_checkout)'","proc:Dev deploys to Prod (new_checkout = FALSE)","dec:Marketing says 'GO!' -> PM toggles flag to TRUE","proc:Users start using new Checkout. Error rates spike!","end:PM toggles flag to FALSE. Crisis averted instantly!"]}
    ],
    game:{icon:"🎛️",title:"The Switchboard",desc:"Master feature flags",badges:["🎛️ Toggler","🥷 Dark Launcher","🗑️ Debt Cleaner"],challenges:[{icon:"📝",title:"Kill Switch",desc:"Why is a flag better than a rollback?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"A/B Test Flag",badge:"Experimenter",desc:"Implement a basic flag check.",tags:["DevOps","Code"],steps:[{title:"The Check",desc:"const isNewUI = await flags.get('new-ui')"},{"title:"The Logic",desc:"if(isNewUI) render <NewCard />"},{"title:"The Fallback",desc:"else render <OldCard />"}],code:`// Mental Model of a Feature Flag in React\nexport default function Dashboard({ user }) {\n  // Fetch flag status from a service like LaunchDarkly\n  const showNewDashboard = useFeatureFlag('v2-dashboard-enable');\n\n  // A PM can toggle this boolean remotely at any time!\n  if (showNewDashboard) {\n    return <NewReactDashboard />;\n  } else {\n    return <LegacyDashboard />;\n  }\n}`}
  },
  t167: {
    tag:'Phase 7 · Practical Scenarios', num:167,
    title:'Code Reviews & Pair Programming',
    desc:'The human element of software engineering: Ensuring quality through collaboration.',
    theory:`<div class="card"><h3>👥 The Second Pair of Eyes</h3><p>Writing code is only 20% of a Software Engineer's job. Reading, reviewing, and discussing code is the other 80%.</p><h4>Code Reviews (Pull Requests)</h4><p>Before your code is merged into the <code>main</code> branch, another engineer must review it. They check for logic flaws, security vulnerabilities, and adherence to company style guidelines. It is a collaborative process, not a test.</p><h4>Pair Programming</h4><p>Two engineers working on the exact same computer (or screen share). The "Driver" types the code, and the "Navigator" reviews it in real-time, thinking about the broader architecture and edge cases. It eliminates the need for a separate Code Review and spreads knowledge instantly.</p></div>`,
    mcqs:[
      {q:"What is the primary purpose of a Code Review (Pull Request)?",opts:["A. To punish developers for making mistakes","B. To catch bugs before they reach production, share knowledge across the team, and maintain a high standard of code quality and consistency.","C. To slow down development","D. To test the compiler"],ans:1,exp:"A good code review is a mentorship opportunity, not a critique."},
      {q:"When reviewing someone's code, what should you focus on?",opts:["A. Formatting and indentation (tabs vs spaces)","B. Architectural decisions, security flaws, edge cases, and performance bottlenecks. (Formatting should be handled automatically by a Linter like Prettier before the PR is even opened).","C. Spelling errors in comments","D. Counting the lines of code"],ans:1,exp:"Never argue about formatting in a PR. Let the machines handle it."},
      {q:"What is the 'Driver' and 'Navigator' dynamic in Pair Programming?",opts:["A. The Driver drives the car, the Navigator reads the map","B. The Driver physically types the code and focuses on the micro-level logic. The Navigator watches, reviews in real-time, and thinks about the macro-level architecture and edge cases.","C. The Driver sleeps, the Navigator types","D. Both type at the exact same time"],ans:1,exp:"They swap roles frequently (e.g., every 30 minutes) to stay fresh."},
      {q:"Why do many teams consider Pair Programming to be FASTER than solo programming, despite using two engineers for one task?",opts:["A. It's not, it's a waste of money","B. It drastically reduces time spent debugging, eliminates the days-long wait for asynchronous Code Reviews, and prevents massive architectural mistakes early on.","C. Two people type faster","D. It looks good on a resume"],ans:1,exp:"The code quality is usually so high that it sails through testing."},
      {q:"What is a highly toxic behavior in a Code Review?",opts:["A. Asking questions to understand the logic","B. Saying 'This is terrible code, fix it.' Reviews should focus on the code, not the person. Use phrases like 'What happens if this variable is null?' instead of 'You forgot the null check.'","C. Approving the code quickly","D. Leaving a 'Looks Good To Me' (LGTM) comment"],ans:1,exp:"Psychological safety is the foundation of a high-performing engineering team."}
    ],
    flows:[
      {title:"The Pull Request Flow",items:["start:Dev pushes 'feature-x' branch to GitHub","proc:Opens a Pull Request (PR) against 'main'","dec:Reviewer finds a logic bug on Line 42","proc:Dev fixes bug, pushes new commit to PR","end:Reviewer Approves (LGTM). Code is merged!"]}
    ],
    game:{icon:"👥",title:"The Collaborator",desc:"Master team dynamics",badges:["👥 Pair Programmer","👀 Code Reviewer","🛡️ Linter Advocate"],challenges:[{icon:"📝",title:"The Navigator",desc:"What does the navigator do?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Constructive Feedback",badge:"Mentor",desc:"Rewrite a toxic PR comment.",tags:["Soft Skills","Team"],steps:[{title:"Toxic",desc:"'You idiot, this will cause a memory leak.'"},{"title:"Constructive",desc:"'Great work on this! I noticed that if we don't close this connection, it might leak. Thoughts?'"},{"title:"Result",desc:"A productive, ego-free conversation."}],code:`// Code Review Best Practices:
// 1. Automate the easy stuff (Linting, Unit Tests) via CI/CD.
// 2. Review the hard stuff (Architecture, Security).
// 3. Keep PRs small (under 300 lines of code). Massive PRs get rubber-stamped.
// 4. Be kind. You are reviewing the code, not the developer.`}
  },
  t168: {
    tag:'Phase 7 · Practical Scenarios', num:168,
    title:'Technical Debt & Refactoring',
    desc:'Managing the invisible cost of cutting corners in software engineering.',
    theory:`<div class="card"><h3>💳 The Credit Card of Code</h3><p>Your boss says, "We need this feature launched tomorrow." You know the right way to build it will take 3 days. So, you copy/paste some messy code, hardcode a few variables, and launch it in 1 day. You just took on <strong>Technical Debt</strong>.</p><h4>Paying the Interest</h4><p>Like financial debt, technical debt accrues "interest". Next month, when you try to add a new feature to that messy code, it takes you 3 days instead of 1. If you never pay down the debt (through <strong>Refactoring</strong>), the codebase eventually becomes so fragile and tangled that development grinds to a complete halt.</p></div>`,
    mcqs:[
      {q:"What is 'Technical Debt'?",opts:["A. Money owed to AWS","B. The implied cost of additional rework caused by choosing an easy, fast, or 'hacky' solution now instead of using a better approach that would take longer.","C. The cost of buying new laptops","D. An unpaid API subscription"],ans:1,exp:"Sometimes taking on debt is a smart business decision to hit a market deadline. But it MUST be paid back."},
      {q:"What is 'Refactoring'?",opts:["A. Deleting the entire codebase and starting over","B. The process of restructuring existing computer code—changing the factoring—without changing its external behavior. (Cleaning up the messy code while ensuring it still passes all tests).","C. Adding new features to the app","D. Upgrading the database hardware"],ans:1,exp:"Refactoring makes the code easier to read and maintain for the next developer."},
      {q:"Why is having a comprehensive suite of Automated Unit Tests critical before you begin Refactoring?",opts:["A. Tests write the code for you","B. Because tests ensure that while you are tearing apart the internal structure of the code, you haven't accidentally broken its external behavior. Without tests, refactoring is just guessing.","C. Tests make the code run faster","D. Tests compile the code"],ans:1,exp:"Red -> Green -> Refactor. (Write a failing test, make it pass, then clean up the code)."},
      {q:"What is a 'Code Smell'?",opts:["A. A computer overheating","B. A surface indication (like a function that is 500 lines long, or massive amounts of duplicated code) that usually corresponds to a deeper problem in the system. It indicates it's time to refactor.","C. An error in the terminal","D. A syntax error"],ans:1,exp:"Duplicate code (violating the DRY principle - Don't Repeat Yourself) is the most common code smell."},
      {q:"How should a team handle Technical Debt?",opts:["A. Ignore it until the app breaks","B. Dedicate a specific percentage of every development cycle (e.g., 20% of every Sprint) specifically to paying down tech debt and refactoring, rather than only building new features.","C. Make the newest developer fix it","D. Delete the old code"],ans:1,exp:"Product managers must understand that building features 100% of the time will eventually lead to 0% productivity."}
    ],
    flows:[
      {title:"The Tech Debt Cycle",items:["start:Startup launches MVP fast (High Debt)","proc:Debt Interest: New features take 2x as long","dec:Team dedicates 1 Sprint to Refactoring (Paying Debt)","proc:Code becomes clean and modular again","end:New features take normal time to build!"]}
    ],
    game:{icon:"💳",title:"The Debt Collector",desc:"Master code maintainability",badges:["💳 Debt Payer","🧹 Refactorer","👃 Code Smeller"],challenges:[{icon:"📝",title:"Code Smell",desc:"What is a 500-line function?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Refactor Duplication",badge:"DRY Master",desc:"Identify and fix a code smell.",tags:["Code","Refactoring"],steps:[{title:"Smell",desc:"You see the exact same 10 lines of date-formatting code in 5 different files."},{"title:"Refactor",desc:"Extract those 10 lines into a shared 'formatDate()' utility function."},{"title:"Result",desc:"Code is DRY (Don't Repeat Yourself)."}],code:`// Technical Debt is not always bad.
// If your startup dies because you spent 3 weeks writing 'perfect' code 
// instead of launching the MVP in 3 days, you failed.
// 
// The goal is to take on debt strategically, 
// and pay it back the moment you find product-market fit.`}
  },
  t169: {
    tag:'Phase 7 · Practical Scenarios', num:169,
    title:'Designing for Failure (Circuit Breaker)',
    desc:'Building resilient systems that survive when external dependencies inevitably die.',
    theory:`<div class="card"><h3>🔌 The Circuit Breaker</h3><p>Your E-commerce app relies on the Stripe API to process payments. What happens if the Stripe API goes down? If your app keeps sending 100 requests a second to Stripe, they will all fail, your app's threads will lock up waiting for responses, and your entire app will crash.</p><h4>The Circuit Breaker Pattern</h4><p>You wrap your Stripe API call in a "Circuit Breaker". If the API fails 5 times in a row, the circuit "Trips" (Opens). For the next 60 seconds, your app instantly rejects all payment attempts, returning a friendly "Please try again later" UI without even attempting to call Stripe. This saves your servers from crashing under the weight of hanging requests!</p></div>`,
    mcqs:[
      {q:"What is the fundamental philosophy of 'Designing for Failure'?",opts:["A. Expecting the software to be perfect","B. Assuming that every network, server, and external dependency WILL eventually fail, and writing code that degrades gracefully rather than crashing the entire system.","C. Designing bad software","D. Buying insurance"],ans:1,exp:"'Everything fails all the time.' - Werner Vogels, CTO of Amazon."},
      {q:"What problem does the Circuit Breaker pattern solve in microservices?",opts:["A. It speeds up the internet","B. It prevents a cascading failure. If a downstream service is dead, the circuit breaker stops sending traffic to it, preventing the upstream service from running out of threads waiting for timeouts.","C. It encrypts passwords","D. It restarts the server"],ans:1,exp:"It gives the dead service time to recover, rather than hammering it with retries."},
      {q:"In a Circuit Breaker, what does the 'Half-Open' state mean?",opts:["A. The circuit is physically broken","B. After a timeout period, the breaker allows a single 'test' request through to the dead service. If it succeeds, the circuit 'Closes' (normal operations resume). If it fails, it 'Opens' again.","C. Half the users get access","D. The database is reading, not writing"],ans:1,exp:"This allows the system to auto-recover without human intervention."},
      {q:"What is an 'Exponential Backoff' retry strategy?",opts:["A. Retrying a failed API call every 1 second infinitely","B. If an API call fails, you wait 1 second to retry. If it fails again, wait 2 seconds. Then 4s, 8s, 16s. This prevents overwhelming a struggling server with a flood of immediate retries.","C. Never retrying","D. Retrying from a different server"],ans:1,exp:"Adding a bit of randomness ('Jitter') to the backoff prevents 10,000 clients from retrying at the exact same millisecond."},
      {q:"What is a 'Fallback' mechanism?",opts:["A. Tripping and falling backward","B. Providing a default or cached response when a service fails. (e.g., If the 'Live Recommendations' AI service is down, fallback to showing the 'Top 10 Global Hits').","C. Deleting the user account","D. Restoring a database backup"],ans:1,exp:"The user might not even know a failure occurred!"}
    ],
    flows:[
      {title:"Circuit Breaker Flow",items:["start:App calls Stripe API (Fails 5 times!)","proc:Circuit Breaker trips to OPEN state","dec:User tries to pay. Breaker instantly rejects (0ms)","proc:60 seconds later, Breaker moves to HALF-OPEN","end:Allows 1 test request. It succeeds! Breaker CLOSES!"]}
    ],
    game:{icon:"🔌",title:"The Electrician",desc:"Master system resilience",badges:["🔌 Circuit Breaker","⏳ Backoff Master","🪂 Fallback Provider"],challenges:[{icon:"📝",title:"Half-Open",desc:"How does a breaker auto-recover?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Exponential Backoff",badge:"Patient Caller",desc:"Implement a backoff loop.",tags:["Network","Logic"],steps:[{title:"Attempt 1",desc:"Fails. Wait 2 seconds."},{"title:"Attempt 2",desc:"Fails. Wait 4 seconds."},{"title:"Attempt 3",desc:"Fails. Wait 8 seconds. Then give up and show error."}],code:`// Mental Model of a Fallback Mechanism
async function getRecommendations(userId) {
  try {
    // Attempt to call the highly complex, fragile AI Microservice
    return await axios.get(\`http://ai-service/recs/\${userId}\`, { timeout: 2000 });
  } catch (error) {
    // If it crashes or times out, DO NOT CRASH THE APP.
    // Fallback: Return a hardcoded list of popular items!
    console.warn("AI Service down. Using Fallback.");
    return ['Harry Potter', 'Lord of the Rings', 'Star Wars'];
  }
}`}
  },
  t170: {
    tag:'Phase 7 · The Real End', num:170,
    title:'Writing High-Quality Documentation',
    desc:'The most underrated skill that separates Junior developers from Staff Engineers.',
    theory:`<div class="card"><h3>📝 Leaving a Map</h3><p>You can write the most brilliant, highly-optimized Rust WebAssembly microservice in the world. If nobody else on your team knows how to run it, deploy it, or understand its architecture... it is useless.</p><h4>The README.md</h4><p>Every repository must have a README that explains: 1. What the project does. 2. How to run it locally (step-by-step commands). 3. Required Environment Variables. 4. How to deploy it.</p><h4>Architecture Decision Records (ADRs)</h4><p>When you make a massive decision (e.g., "We are switching from MongoDB to Postgres"), you write a 1-page ADR explaining <em>WHY</em> you did it. Two years later, when a new engineer asks "Why didn't they use Mongo?", the ADR provides the exact historical context!</p></div>`,
    mcqs:[
      {q:"Why is documentation often considered more important than the code itself in large enterprise organizations?",opts:["A. It isn't, code is king","B. Code constantly changes and is rewritten. Documentation (like ADRs) captures the 'Why'—the business logic and historical context that prevents future teams from repeating the same expensive mistakes.","C. Because managers can't read code","D. To make the repository look full"],ans:1,exp:"Code tells you HOW. Documentation tells you WHY."},
      {q:"What is the absolute minimum documentation every code repository must have?",opts:["A. A 50-page PDF manual","B. A clear, concise README.md file explaining what the project is, prerequisite installations, and the exact terminal commands required to get it running locally.","C. A video tutorial","D. A UML diagram"],ans:1,exp:"If a new hire takes 3 days to figure out how to start the app locally, your README has failed."},
      {q:"What is an Architecture Decision Record (ADR)?",opts:["A. A voice memo","B. A short text file that captures an important architectural decision made along with its context, the options considered, and the consequences (good and bad) of that decision.","C. A database table","D. A code review tool"],ans:1,exp:"ADRs prevent the endless loop of developers questioning past decisions."},
      {q:"When writing comments in your actual code, what is the Golden Rule?",opts:["A. Comment every single line","B. Don't comment on WHAT the code is doing (the code itself should be readable enough to explain that). Comment on WHY the code is doing something strange or unintuitive (e.g., a workaround for a specific browser bug).","C. Never write comments","D. Use emojis"],ans:1,exp:"Example of a bad comment: // Adds 1 to i. (We can see that!). Example of a good comment: // Fast inverse square root hack for physics engine performance."},
      {q:"Have you reached the absolute, undeniable end of the practical handbook?",opts:["A. No","B. Yes. I am fully equipped with the theory, the architecture, and the practical best practices to be a Top-Tier Software Engineer.","C. Maybe","D. Let's do 10 more"],ans:1,exp:"Now it's time to build."}
    ],
    flows:[
      {title:"The New Hire Flow",items:["start:New Dev clones repo on Day 1","proc:Reads README.md","dec:Runs 'npm install' and 'docker-compose up'","proc:App runs flawlessly on their laptop in 5 minutes","end:New Dev feels incredibly happy and productive!"]}
    ],
    game:{icon:"📝",title:"The Scribe",desc:"Master documentation",badges:["📝 README Writer","🏛️ ADR Historian","🧠 Context Provider"],challenges:[{icon:"📝",title:"Code Comments",desc:"What should a code comment explain?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"The Perfect README",badge:"Documenter",desc:"Structure a repository README.",tags:["Docs","Best Practices"],steps:[{title:"Title & Description",desc:"What is this app?"},{"title:"Quickstart",desc:"How do I run this on my Macbook?"},{"title:"Environment Vars",desc:"What keys do I need to supply?"}],code:`# 🚀 Ultimate API Service

This microservice handles all Stripe billing interactions.

## 🛠️ Quickstart (Local Dev)
1. Ensure Docker is installed.
2. Clone repo and run \`cp .env.example .env\`
3. Run \`docker-compose up\`
4. API is live at \`http://localhost:8080\`

## 📝 Architecture Notes
See \`/docs/ADR-001-why-we-chose-stripe.md\` for payment provider context.`}
  }
"""

start_marker = "};\n\nlet userXP"
inject_idx = content.find(start_marker)

if inject_idx != -1:
    new_content = content[:inject_idx] + ",\n" + rich_content + content[inject_idx:]
    with open(html_path, "w") as f:
        f.write(new_content)
    print("Successfully generated T161-T170 rich content!")
else:
    print("Could not find injection point.")
