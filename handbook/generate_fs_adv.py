









import re

html_path = "/Users/bhoomim/devops CI:CD/handbook/fullstack_ai_handbook.html"
with open(html_path, "r") as f:
    content = f.read()

rich_content = r"""
  t151: {
    tag:'Phase 6 · Advanced', num:151,
    title:'OAuth 2.0 & OpenID Connect',
    desc:'The modern protocols for secure delegation of authorization and authentication.',
    theory:`<div class="card"><h3>🤝 The Valet Key</h3><p>If you want a new app to access your Google Calendar, you don't give the app your actual Google Password. Instead, you use <strong>OAuth 2.0</strong>. You log into Google, and Google gives the app a temporary "Access Token" (like a valet key) that ONLY allows it to read your calendar, nothing else.</p><h4>OpenID Connect (OIDC)</h4><p>OAuth 2.0 is purely for <em>Authorization</em> (what you can do). It does not verify <em>Authentication</em> (who you are). <strong>OIDC</strong> is an identity layer built on top of OAuth 2.0. It provides an "ID Token" (usually a JWT) so the app knows your name and email address. This is how "Log in with Google/Apple" buttons work!</p></div>`,
    mcqs:[
      {q:"What is the primary purpose of the OAuth 2.0 protocol?",opts:["A. To encrypt database passwords","B. To securely delegate Authorization, allowing a third-party application to access a user's data on another service (like Google or Facebook) WITHOUT the user giving away their password.","C. To speed up network requests","D. To route API traffic"],ans:1,exp:"Think of it as giving a hotel valet a special key that only drives the car, but doesn't open the trunk or glovebox."},
      {q:"Why was OpenID Connect (OIDC) created on top of OAuth 2.0?",opts:["A. Because OAuth was too slow","B. Because OAuth 2.0 is designed for Authorization (access), not Authentication (identity). OIDC adds an ID Token so the application can actually verify WHO the user is.","C. To support XML","D. To replace JWTs"],ans:1,exp:"OAuth says 'You can read the calendar'. OIDC says 'You are John Doe'."},
      {q:"What format is the OIDC 'ID Token' usually in?",opts:["A. A plain text file","B. A JSON Web Token (JWT), containing signed claims about the user (like email, name, and profile picture URL)","C. A binary executable","D. An XML string"],ans:1,exp:"The app decodes the JWT to instantly get the user's profile info."},
      {q:"In the OAuth flow, what is an 'Access Token'?",opts:["A. The user's password","B. A secure, short-lived string issued by the Authorization Server that the client app sends to the Resource Server (API) to prove it has permission to fetch data.","C. A database ID","D. A routing key"],ans:1,exp:"The client app includes the Access Token in the HTTP Authorization header (Bearer token)."},
      {q:"What is the purpose of a 'Refresh Token'?",opts:["A. To reload the browser","B. Access Tokens expire quickly (e.g., 1 hour) for security. A Refresh Token is a long-lived credential used by the app to quietly request a NEW Access Token without forcing the user to log in again.","C. To clear the cache","D. To update the UI"],ans:1,exp:"If an Access Token is stolen, the hacker only has 1 hour. If a Refresh Token is stolen, it's a massive security breach."}
    ],
    flows:[
      {title:"OAuth 2.0 Flow",items:["start:User clicks 'Login with Google'","proc:App redirects User to Google's Server","proc:User logs in & grants permission","dec:Google redirects back to App with a 'Code'","end:App trades 'Code' for Access & ID Tokens!"]}
    ],
    game:{icon:"🤝",title:"The Delegator",desc:"Master OAuth & OIDC",badges:["🤝 Valet Parker","🆔 Identity Checker","🔄 Token Refresher"],challenges:[{icon:"📝",title:"Auth vs Auth",desc:"Authorization vs Authentication?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Token Roles",badge:"Security Guard",desc:"Understand the 3 tokens.",tags:["Security","OAuth"],steps:[{title:"ID Token",desc:"Who is the user? (Used by Frontend)"},{"title:"Access Token",desc:"What can they do? (Sent to Backend API)"},{"title:"Refresh Token",desc:"Get new tokens when they expire."}],code:`// Mental Model for OAuth Headers\n\n// When fetching data from an API, the frontend sends the Access Token:\nconst response = await fetch('https://api.github.com/user', {\n  headers: {\n    'Authorization': 'Bearer gho_16C7e42f292c6912E7710c838347Ae178B4a'\n  }\n});`}
  },
  t152: {
    tag:'Phase 6 · Advanced', num:152,
    title:'WebSockets & Real-Time',
    desc:'Moving beyond HTTP to create persistent, bi-directional connections for chat apps and live games.',
    theory:`<div class="card"><h3>⚡ The Open Line</h3><p>Standard HTTP is <strong>Stateless and Uni-directional</strong>. The client asks for data, the server replies, and the connection hangs up. If you build a chat app this way, the client has to ask "Any new messages?" every 1 second (Long Polling). This crushes server performance.</p><h4>WebSockets</h4><p>The <strong>WebSocket (ws://)</strong> protocol creates a persistent, two-way connection between the client and server. The connection stays open! If User B sends a message, the Server instantly pushes it down the open pipe to User A without User A ever having to ask for it. Essential for live chat, stock tickers, and multiplayer games.</p></div>`,
    mcqs:[
      {q:"What is the primary limitation of standard HTTP for real-time applications like live chat?",opts:["A. It cannot send text","B. It is strictly Request-Response (Client initiates, Server replies, connection closes). The server cannot spontaneously push new data to the client when an event happens.","C. It only works on desktop","D. It is too secure"],ans:1,exp:"To get around this, developers used to 'poll' the server every few seconds, wasting massive bandwidth."},
      {q:"How does the WebSocket protocol differ from HTTP?",opts:["A. It is slower","B. It establishes a persistent, bi-directional, full-duplex TCP connection. Both the Client and the Server can send messages to each other at any time without establishing a new connection.","C. It uses UDP","D. It only works for video"],ans:1,exp:"A WebSocket connection starts as a standard HTTP request, then 'Upgrades' to a WebSocket."},
      {q:"What prefix is used for secure WebSocket URLs?",opts:["A. https://","B. wss:// (WebSocket Secure)","C. ws://","D. tcp://"],ans:1,exp:"wss:// uses TLS encryption, exactly like https://. Always use wss:// in production."},
      {q:"If a user's internet connection briefly drops, what happens to the WebSocket?",opts:["A. It fixes the internet","B. The connection breaks. You must write Javascript logic to detect the disconnection and automatically attempt to reconnect (or use a library like Socket.io that does this for you).","C. The server crashes","D. The browser crashes"],ans:1,exp:"Reconnection logic and handling missed messages are the hardest parts of WebSocket development."},
      {q:"Which popular Node.js library acts as a wrapper around WebSockets, providing automatic reconnections, fallbacks to polling, and broadcast 'Rooms'?",opts:["A. Express.js","B. Socket.io","C. React","D. Mongoose"],ans:1,exp:"Socket.io makes real-time development incredibly easy, but it is NOT a raw native WebSocket."}
    ],
    flows:[
      {title:"WebSocket Chat Flow",items:["start:Client connects to wss://chat.com","proc:Connection remains OPEN permanently","dec:User 2 sends message to Server","proc:Server instantly PUSHES message down pipe to Client","end:Client UI updates instantly (No polling needed!)"]}
    ],
    game:{icon:"⚡",title:"The Broadcaster",desc:"Master Real-Time connections",badges:["⚡ Socket Keeper","🔄 Full Duplexer","🚪 Room Manager"],challenges:[{icon:"📝",title:"Polling vs Sockets",desc:"Why is polling bad for servers?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Socket.io Event",badge:"Live Chatter",desc:"Emit and listen for events.",tags:["Sockets","Node"],steps:[{title:"Server",desc:"io.on('connection', socket => ...)"},{"title:"Client Emits",desc:"socket.emit('sendMessage', 'Hello')"},{"title:"Server Broadcasts",desc:"io.emit('newMessage', 'Hello') to everyone!"}],code:`// Basic Socket.io Server Logic
io.on('connection', (socket) => {
  console.log('A user connected!');

  // Listen for a custom event from this specific client
  socket.on('chatMessage', (msg) => {
    // Broadcast the message to ALL connected clients instantly!
    io.emit('chatMessage', msg);
  });
});`}
  },
  t153: {
    tag:'Phase 6 · Advanced', num:153,
    title:'GraphQL vs REST',
    desc:'A revolutionary query language for APIs that solves the over-fetching problem.',
    theory:`<div class="card"><h3>📊 Ask For Exactly What You Want</h3><p>In a standard <strong>REST API</strong>, if you hit <code>/api/users/1</code>, the backend returns a massive JSON object with the user's name, email, age, address, and 50 other fields. What if the Mobile App ONLY needed the user's name? That is wasted bandwidth (<strong>Over-fetching</strong>).</p><h4>GraphQL</h4><p>Created by Facebook, <strong>GraphQL</strong> has only ONE endpoint (e.g., <code>/graphql</code>). The Frontend sends a precise Query describing <em>exactly</em> the fields it wants. If it asks for <code>name</code> and <code>age</code>, the backend returns a JSON object with <em>only</em> <code>name</code> and <code>age</code>. Nothing more, nothing less.</p></div>`,
    mcqs:[
      {q:"What is the 'Over-fetching' problem in traditional REST APIs?",opts:["A. Fetching data too fast","B. An endpoint returning a massive amount of data fields that the client doesn't actually need, wasting network bandwidth and slowing down mobile devices.","C. Fetching from the wrong server","D. Deleting fetched data"],ans:1,exp:"REST endpoints are usually fixed and inflexible."},
      {q:"What is the 'Under-fetching' (N+1) problem in traditional REST APIs?",opts:["A. Not getting enough sleep","B. When one endpoint doesn't return enough data, forcing the client to make multiple additional HTTP requests to other endpoints (e.g., get User, then loop to get 50 Posts for that user).","C. When the server is too slow","D. Getting 404 errors"],ans:1,exp:"GraphQL solves this by allowing nested queries in a single request."},
      {q:"How does GraphQL fundamentally differ from REST regarding endpoints?",opts:["A. It uses XML instead of JSON","B. REST has multiple endpoints (URLs) for different resources (e.g., /users, /posts, /comments). GraphQL typically exposes exactly ONE endpoint (e.g., /graphql) that handles all queries.","C. GraphQL doesn't use HTTP","D. GraphQL is only for databases"],ans:1,exp:"The routing logic is moved from the URL path into the GraphQL Query Body itself."},
      {q:"In GraphQL, what is a 'Mutation'?",opts:["A. A software bug","B. The equivalent of a REST POST/PUT/DELETE request. It is a specific operation used to modify (write/update) data on the server rather than just reading it.","C. Changing CSS colors","D. A database crash"],ans:1,exp:"Queries are for reading (GET). Mutations are for writing."},
      {q:"Why do developers love the GraphQL 'Schema'?",opts:["A. It is colorful","B. It acts as a strongly-typed contract between the Frontend and Backend. It auto-generates flawless documentation and gives Frontend developers incredible autocomplete in their IDEs.","C. It writes CSS","D. It deploys the app"],ans:1,exp:"The schema ensures the frontend never asks for a field that doesn't exist."}
    ],
    flows:[
      {title:"GraphQL Query Flow",items:["start:Frontend needs just User Name & Post Titles","proc:Sends POST to /graphql","dec:Body: query { user(id:1) { name, posts { title } } }","proc:Backend GraphQL Resolver fetches exact data","end:Returns exactly 2 fields. Zero wasted bandwidth!"]}
    ],
    game:{icon:"📊",title:"The Grapher",desc:"Master GraphQL APIs",badges:["📊 Over-fetch Stopper","🧩 Resolver Writer","📝 Schema Definer"],challenges:[{icon:"📝",title:"One Endpoint",desc:"Why does GraphQL only use one URL?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Write a Query",badge:"Query Crafter",desc:"Request exact data from a GraphQL API.",tags:["API","GraphQL"],steps:[{title:"REST Way",desc:"GET /users/1, GET /users/1/posts, GET /users/1/followers"},{"title:"GraphQL Way",desc:"One query asking for everything nested!"},{"title:"Result",desc:"One single HTTP request. Saves mobile battery."}],code:`# A standard GraphQL Query sent from the Frontend\n\nquery GetUserProfile {\n  user(id: "123") {\n    name\n    avatarUrl\n    # Nested data in the same request!\n    recentPosts(limit: 3) {\n      title\n      likes\n    }\n  }\n}\n# The backend will return a JSON object perfectly matching this shape.`}
  },
  t154: {
    tag:'Phase 6 · Advanced', num:154,
    title:'WebAssembly (Wasm)',
    desc:'Running high-performance C++, Rust, and Go code directly inside the web browser.',
    theory:`<div class="card"><h3>🚀 Breaking the Speed Limit</h3><p>JavaScript is fast, but it is not fast enough to run a 3D AAA video game, Adobe Photoshop, or complex video rendering directly in the browser.</p><h4>WebAssembly (Wasm)</h4><p>Wasm is a low-level binary instruction format. It allows developers to write code in blazing-fast languages like <strong>Rust, C++, or Go</strong>, compile it into a tiny <code>.wasm</code> binary file, and run it in the browser at near-native speeds. It doesn't replace JavaScript; it works <em>alongside</em> it. JS handles the UI, and Wasm handles the heavy mathematical lifting.</p></div>`,
    mcqs:[
      {q:"What is the primary goal of WebAssembly (Wasm)?",opts:["A. To replace HTML and CSS","B. To enable high-performance applications (like 3D games, CAD software, and video editors) to run directly in the web browser at near-native speeds.","C. To make JavaScript slower","D. To build databases"],ans:1,exp:"Figma and AutoCAD use WebAssembly heavily to run complex graphics engines in the browser."},
      {q:"Does WebAssembly aim to completely replace JavaScript?",opts:["A. Yes, JavaScript will be obsolete","B. No. Wasm is designed to work alongside JavaScript. JS handles the DOM and UI, while Wasm handles heavy computational tasks. They can call each other's functions.","C. Yes, for security reasons","D. No, it replaces CSS"],ans:1,exp:"You use the right tool for the job. UI = JS. Math = Wasm."},
      {q:"How do you write WebAssembly?",opts:["A. By typing 1s and 0s manually","B. You typically don't write it directly. You write code in a language like Rust, C++, C#, or Go, and then use a compiler to output a binary .wasm file that the browser understands.","C. Using standard Javascript","D. Using Python"],ans:1,exp:"Rust has become the most popular language for writing WebAssembly due to its safety and speed."},
      {q:"Is WebAssembly secure?",opts:["A. No, it has full access to the user's hard drive","B. Yes, it executes inside a memory-safe, sandboxed execution environment, utilizing the exact same security policies (like Same-Origin) as JavaScript.","C. It turns off the firewall","D. It is vulnerable to SQL injection"],ans:1,exp:"A Wasm module cannot break out of the browser sandbox."},
      {q:"Can WebAssembly directly manipulate the HTML DOM (e.g., changing a div's color)?",opts:["A. Yes, directly and easily","B. Currently, no. Wasm cannot directly touch the DOM. It must call a JavaScript function, and let Javascript update the DOM on its behalf.","C. Only in Chrome","D. Yes, using CSS"],ans:1,exp:"This is why Wasm isn't meant to build standard UI web apps."}
    ],
    flows:[
      {title:"The WebAssembly Flow",items:["start:Developer writes heavy image filter in Rust","proc:Compiles Rust code to 'filter.wasm' binary","dec:Browser downloads HTML, JS, and the Wasm file","proc:JS UI captures webcam photo","end:JS passes photo to Wasm. Wasm processes it in 1ms!"]}
    ],
    game:{icon:"🚀",title:"The Optimizer",desc:"Master Wasm concepts",badges:["🚀 Near-Native Speed","🦀 Rust Compiler","🤝 JS Collaborator"],challenges:[{icon:"📝",title:"The DOM",desc:"Can Wasm directly change HTML?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Wasm Architecture",badge:"Visionary",desc:"Design a hybrid JS/Wasm app.",tags:["Wasm","Architecture"],steps:[{title:"The UI",desc:"React/JS renders the buttons and layout."},{"title:"The Engine",desc:"Rust/Wasm handles the physics calculations."},{"title:"The Bridge",desc:"React passes coordinates to Wasm. Wasm returns results."}],code:`// Mental Model of JS + Wasm Interop\n\n// 1. Fetch the compiled C++ or Rust binary\nconst wasmModule = await WebAssembly.instantiateStreaming(fetch('math.wasm'));\n\n// 2. Extract the blazing fast function\nconst fastCalculate = wasmModule.instance.exports.calculate;\n\n// 3. Let JS handle the UI, let Wasm handle the math!\nbutton.onclick = () => {\n  const result = fastCalculate(999999999);\n  document.getElementById('result').innerText = result;\n};`}
  },
  t155: {
    tag:'Phase 6 · Advanced', num:155,
    title:'Progressive Web Apps (PWAs)',
    desc:'Making web applications feel exactly like native iOS or Android apps.',
    theory:`<div class="card"><h3>📱 The Best of Both Worlds</h3><p>Building a website, an iOS app, and an Android app requires 3 different teams and 3 different codebases. It is wildly expensive.</p><h4>Progressive Web Apps</h4><p>A <strong>PWA</strong> is a standard website built with React/Next.js that looks and behaves like a native mobile app. It uses a <strong>Service Worker</strong> to cache files, allowing the app to work completely <em>offline</em>! Users can "Install" the website directly to their phone's home screen, and it can even send Push Notifications. Write once, run everywhere.</p></div>`,
    mcqs:[
      {q:"What is a Progressive Web App (PWA)?",opts:["A. A website that only works on desktop","B. A standard web application that utilizes modern browser features to provide an installable, app-like experience (offline support, push notifications) on mobile devices without needing an App Store.","C. An app written in Swift","D. A database application"],ans:1,exp:"Twitter (X) Mobile is a famous PWA. It feels native, but it's just a website."},
      {q:"What is the core technology that allows a PWA to work Offline?",opts:["A. LocalStorage","B. Service Workers. These are JavaScript scripts that run in the background, acting as a network proxy. They intercept HTTP requests and serve cached files if there is no internet connection.","C. WebSockets","D. React Router"],ans:1,exp:"Service Workers are the magic behind true PWAs."},
      {q:"What does the 'Web App Manifest' (manifest.json) do in a PWA?",opts:["A. It writes the CSS","B. It provides metadata about the app (name, icons, theme colors, display mode). This tells the browser how the app should look when 'Installed' to the user's home screen.","C. It stores the database","D. It manages the server"],ans:1,exp:"It allows the app to open in 'standalone' mode, hiding the browser's URL bar so it looks like a real app."},
      {q:"Why do businesses love PWAs compared to native iOS/Android apps?",opts:["A. They are slower","B. They bypass the Apple/Google App Stores completely. No 30% revenue cut, no waiting for app review approvals, and only 1 codebase to maintain.","C. They only work on Android","D. They use older technology"],ans:1,exp:"Updating a PWA is as easy as deploying a website. Instantly live for all users."},
      {q:"Can a PWA send Push Notifications to a user's phone?",opts:["A. No, only native apps can do that","B. Yes, by using the Push API and the Service Worker running in the background, even when the web app is closed.","C. Only via email","D. Only on Windows"],ans:1,exp:"Note: Apple's iOS has historically restricted PWA features (like Push) compared to Android, though they are slowly improving."}
    ],
    flows:[
      {title:"Service Worker Offline Flow",items:["start:User opens PWA on Airplane Mode","proc:App tries to fetch '/index.html'","dec:Service Worker intercepts the network request!","proc:Service Worker checks Cache Storage","end:Finds 'index.html', serves it. App loads offline!"]}
    ],
    game:{icon:"📱",title:"The App Maker",desc:"Master PWA features",badges:["📱 Home Screen Installer","📴 Offline Cacher","🔔 Push Notifier"],challenges:[{icon:"📝",title:"Service Worker",desc:"What is a background proxy?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Manifest Creation",badge:"Configurator",desc:"Write a web app manifest.",tags:["PWA","Config"],steps:[{title:"Icons",desc:"Provide high-res icons for the home screen."},{"title:"Display",desc:"Set 'display': 'standalone' to hide URL bar."},{"title:"Theme",desc:"Set theme_color to match brand."}],code:`// manifest.json - The soul of a PWA
{
  "name": "My Awesome Chat",
  "short_name": "Chat",
  "start_url": "/",
  "display": "standalone", // Hides the browser Safari/Chrome UI!
  "background_color": "#ffffff",
  "theme_color": "#000000",
  "icons": [
    {
      "src": "/icon-512x512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ]
}`}
  },
  t156: {
    tag:'Phase 6 · Advanced', num:156,
    title:'GitOps & ArgoCD',
    desc:'The modern evolution of Kubernetes deployment and configuration management.',
    theory:`<div class="card"><h3>🤖 The Infinite Loop</h3><p>Traditional CI/CD uses a "Push" model. GitHub Actions builds the Docker image and then runs <code>kubectl apply</code> to push the YAML to Kubernetes. But what if someone manually logs into K8s and changes a setting? Your cluster is now out of sync with your Git repository! (Configuration Drift).</p><h4>GitOps (ArgoCD)</h4><p>GitOps uses a "Pull" model. You install an agent (<strong>ArgoCD</strong>) <em>inside</em> the K8s cluster. ArgoCD constantly monitors your GitHub repository. If you change a YAML file in Git, ArgoCD automatically pulls the change and applies it. If a human manually messes up the K8s cluster, ArgoCD instantly overwrites it to match what is in Git. Git becomes the absolute Single Source of Truth.</p></div>`,
    mcqs:[
      {q:"What is the core philosophy of GitOps?",opts:["A. Using Git to store images","B. Git is the single source of truth for declarative infrastructure and applications. The entire state of the system is version-controlled in Git.","C. Replacing Docker with Git","D. Using Git to write CSS"],ans:1,exp:"If your entire cluster is destroyed, you can rebuild it perfectly in minutes because every setting is stored in a Git repo."},
      {q:"How does GitOps (ArgoCD) differ from traditional CI/CD (GitHub Actions pushing to K8s)?",opts:["A. It doesn't use YAML","B. Traditional CD 'pushes' deployments from the outside. GitOps uses an agent running INSIDE the cluster that constantly 'pulls' the desired state from Git and reconciles it.","C. It is much slower","D. It uses Jenkins"],ans:1,exp:"Because ArgoCD lives inside the cluster, you don't have to give GitHub Actions your sensitive K8s admin credentials."},
      {q:"What is 'Configuration Drift'?",opts:["A. When the code gets older","B. When the actual running state of the infrastructure (e.g., manual K8s tweaks by an admin) no longer matches the configuration stored in Git.","C. When the server moves data centers","D. A feature of Docker"],ans:1,exp:"ArgoCD's main job is to constantly fight Configuration Drift by enforcing the Git state."},
      {q:"If a rogue admin manually deletes a critical Pod or changes a Service port via 'kubectl', how does ArgoCD react?",opts:["A. It crashes","B. It detects the drift immediately. It automatically kicks in, overwrites the manual changes, and restores the K8s object to perfectly match the YAML defined in Git.","C. It sends an email and waits","D. It deletes the Git repo"],ans:1,exp:"This is the ultimate security and stability measure."},
      {q:"In a GitOps workflow, how do you perform a rollback to a previous version of your app?",opts:["A. You manually edit the K8s cluster","B. You simply perform a 'git revert' to a previous commit in your repository. ArgoCD sees the change in Git and automatically rolls the cluster back.","C. You restart the server","D. You delete the database"],ans:1,exp:"Every deployment is just a standard Git commit!"}
    ],
    flows:[
      {title:"The ArgoCD Pull Flow",items:["start:Dev commits 'replicas: 5' to Git Repo","proc:ArgoCD (inside K8s) polls Git every 3 mins","dec:Notices K8s currently has 3 replicas (Drift!)","proc:ArgoCD triggers Sync process","end:ArgoCD forces K8s to scale to 5. State matched!"]}
    ],
    game:{icon:"🤖",title:"The Reconciler",desc:"Master GitOps",badges:["🤖 Argo Fan","🧲 Pull Modeler","⚓ Drift Preventer"],challenges:[{icon:"📝",title:"Push vs Pull",desc:"Why is Pull more secure?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"GitOps Workflow",badge:"Drift Fixer",desc:"Understand the GitOps lifecycle.",tags:["DevOps","GitOps"],steps:[{title:"The Change",desc:"Dev opens PR changing image tag to v2.0."},{"title:"The Merge",desc:"Tech Lead approves and merges PR."},{"title:"The Automation",desc:"ArgoCD sees merge, deploys v2.0 silently."}],code:`// The GitOps Law:
// "If it is not in Git, it does not exist."
// 
// You no longer run kubectl apply manually.
// You no longer give CI tools cluster admin rights.
// You just commit YAML to GitHub, and the cluster updates itself.`}
  },
  t157: {
    tag:'Phase 6 · Advanced', num:157,
    title:'Serverless Edge Computing',
    desc:'Running backend logic globally, physically closer to the user to eliminate latency.',
    theory:`<div class="card"><h3>🌍 Pushing Code to the Edge</h3><p>Normally, if a user in Tokyo requests your website, the request travels across the ocean to your AWS server in Virginia, causing 200ms of latency (lag). CDNs fixed this for static files (images) by caching them in Tokyo.</p><h4>Edge Functions</h4><p>But what about dynamic backend logic? (e.g., checking authentication or AB testing). <strong>Edge Computing (Cloudflare Workers, Vercel Edge)</strong> allows you to deploy your JavaScript backend functions to hundreds of mini-servers globally. When the user in Tokyo logs in, the JS function executes in a Tokyo datacenter, returning the result in 10ms!</p></div>`,
    mcqs:[
      {q:"What physical problem does Edge Computing solve?",opts:["A. Low battery life","B. The speed of light. Data takes time to travel across the globe. By running code at the 'Edge' (datacenters physically close to the user), latency is drastically reduced.","C. Small hard drives","D. Slow CPU processors"],ans:1,exp:"A request from London to AWS us-east-1 takes 100ms. A request from London to a London Edge node takes 5ms."},
      {q:"How do Edge Functions (like Cloudflare Workers) differ from traditional Serverless Functions (like AWS Lambda)?",opts:["A. Edge functions use Python","B. AWS Lambdas run in one specific region (e.g., Ohio). Edge Functions are replicated and deployed globally to hundreds of data centers instantly.","C. Edge functions are slower","D. Lambda is for frontend"],ans:1,exp:"Cloudflare has a datacenter within 50 milliseconds of 95% of the internet-connected population."},
      {q:"What is a major limitation of running code at the Edge?",opts:["A. It is too expensive","B. They use lightweight V8 isolates instead of full Node.js or Docker containers. This means they start instantly (no cold starts), but they have strict limits on execution time, memory, and lack full Node.js API support.","C. They only work on mobile","D. They don't support HTTP"],ans:1,exp:"You use the Edge for lightweight middleware (routing, auth checks, redirecting), not for heavy video processing."},
      {q:"What is a perfect use-case for an Edge Function?",opts:["A. Training an AI model","B. Intercepting a user's request to read their 'Cookie' and instantly routing them to an A/B test version of the site before hitting the main server.","C. Hosting a massive SQL database","D. Rendering 3D graphics"],ans:1,exp:"Edge middleware can modify the request/response instantly before it reaches your expensive main servers."},
      {q:"What does 'No Cold Starts' mean in the context of Edge isolates (like Vercel Edge)?",opts:["A. The servers are physically hot","B. Because they don't boot up a full Docker container or Node environment (they just run V8 Javascript directly), the code executes in 0-1 milliseconds, eliminating the massive lag associated with AWS Lambda.","C. They only work in summer","D. They skip the boot sequence"],ans:1,exp:"This makes Edge functions incredibly snappy and ideal for UI-blocking requests."}
    ],
    flows:[
      {title:"The Global Edge Flow",items:["start:User (in Paris) clicks 'Login'","proc:Request hits Cloudflare Edge Node (in Paris)","dec:Edge Function checks JWT token instantly (5ms)","proc:Valid! Edge Function forwards req to AWS (USA)","end:Edge handles auth, AWS handles database."]}
    ],
    game:{icon:"🌍",title:"The Globetrotter",desc:"Master Edge computing",badges:["🌍 Edge Deployer","⚡ 1ms Executor","🚦 Middleware Router"],challenges:[{icon:"📝",title:"V8 Isolates",desc:"Why are Edge functions faster than Lambda?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Edge Auth Middleware",badge:"Interceptor",desc:"Write an Edge routing script.",tags:["Edge","Next.js"],steps:[{title:"The Request",desc:"User tries to access /dashboard"},{"title:"The Edge Check",desc:"Edge reads cookie. No token?"},{"title:"The Redirect",desc:"Edge redirects to /login instantly!"}],code:`// Next.js Edge Middleware Example
import { NextResponse } from 'next/server'
 
// This function runs globally at the Edge (Cloudflare/Vercel)
// It executes in < 1ms before the request even hits your backend!
export function middleware(request) {
  const token = request.cookies.get('auth_token');
  
  if (!token) {
    // Instantly bounce unauthorized users away from your expensive servers
    return NextResponse.redirect(new URL('/login', request.url));
  }
}`}
  },
  t158: {
    tag:'Phase 6 · Advanced', num:158,
    title:'Fine-Tuning LLMs (LoRA)',
    desc:'Customizing Open-Source AI models for specialized industry tasks.',
    theory:`<div class="card"><h3>🛠️ Sharpening the Blade</h3><p>RAG is great for giving an AI <em>facts</em> (like a document). But what if you want the AI to learn a new <em>skill</em> or adopt a highly specific <em>tone of voice</em> (like outputting perfectly formatted medical JSON)? You use <strong>Fine-Tuning</strong>.</p><h4>LoRA (Low-Rank Adaptation)</h4><p>Fine-tuning a massive open-source model (like LLaMA-3) used to require millions of dollars in GPUs to update all 70 billion parameters. <strong>LoRA</strong> is a brilliant mathematical trick. Instead of changing the original model, it trains a tiny "adapter" module (a few megabytes) that sits on top of the frozen base model, achieving the same results using a single cheap GPU!</p></div>`,
    mcqs:[
      {q:"When should you use Fine-Tuning instead of RAG (Retrieval-Augmented Generation)?",opts:["A. When you want the AI to know recent news","B. Use RAG for teaching the AI new FACTS (data). Use Fine-Tuning for teaching the AI new SKILLS, formats, behaviors, or a highly specific tone of voice (e.g., writing code in a proprietary company language).","C. Use Fine-Tuning for everything","D. Use RAG for images"],ans:1,exp:"Fine-tuning is terrible for memorizing facts (it hallucinates). RAG is perfect for facts."},
      {q:"What is LoRA (Low-Rank Adaptation)?",opts:["A. A new programming language","B. An incredibly efficient technique that allows you to fine-tune massive AI models on consumer hardware by training a tiny 'adapter' matrix instead of updating billions of original parameters.","C. A Vector Database","D. An image generator"],ans:1,exp:"LoRA democratized AI training. Anyone with a decent gaming GPU can now fine-tune LLaMA."},
      {q:"What format does training data usually need to be in to fine-tune a chat model?",opts:["A. PDF files","B. A massive JSONL file containing thousands of examples of 'Conversations' (System Prompt, User Message, ideal Assistant Response).","C. MP3 audio files","D. An Excel spreadsheet"],ans:1,exp:"You are showing the model exactly how you want it to respond, thousands of times over."},
      {q:"What is 'Catastrophic Forgetting' in neural networks?",opts:["A. When the database crashes","B. When you train a model so heavily on a new task that it 'forgets' how to do the things it used to be good at (like forgetting general English while learning medical terms).","C. When it deletes its training data","D. When the API key expires"],ans:1,exp:"This is why fine-tuning requires a delicate balance of diverse data."},
      {q:"Why might a company choose to fine-tune an Open-Source model (like Meta's LLaMA) instead of just using the OpenAI API?",opts:["A. Open source is slower","B. Privacy, Data Security, and Cost. They can run the fine-tuned model entirely on their own private AWS servers, guaranteeing sensitive customer data never leaves their network.","C. OpenAI has bad grammar","D. Open source requires no code"],ans:1,exp:"For hospitals and banks, sending data to a 3rd party API is often illegal."}
    ],
    flows:[
      {title:"The LoRA Fine-Tuning Flow",items:["start:Base Model: LLaMA-3 (Frozen, 70B Params)","proc:Prepare 10,000 Medical QA JSON examples","dec:Train LoRA Adapter (Updates only 10M Params)","proc:Merge Adapter with Base Model","end:Result: A specialized Medical AI running on 1 GPU!"]}
    ],
    game:{icon:"🛠️",title:"The Tuner",desc:"Master AI fine-tuning",badges:["🛠️ Data Preparer","🧮 Matrix Adapter","🧠 Skill Teacher"],challenges:[{icon:"📝",title:"RAG vs Fine-Tune",desc:"Which is for facts vs skills?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Training Data format",badge:"Data Engineer",desc:"Prepare JSONL for fine-tuning.",tags:["AI","Data"],steps:[{title:"System",desc:"You are a sarcastic bot."},{"title:"User",desc:"What is the weather?"},{"title:"Assistant",desc:"Look outside, I'm a computer not a window."}],code:`// JSONL format for Fine-Tuning a Chat Model
{"messages": [{"role": "system", "content": "You are a pirate."}, {"role": "user", "content": "Hello"}, {"role": "assistant", "content": "Ahoy matey!"}]}
{"messages": [{"role": "system", "content": "You are a pirate."}, {"role": "user", "content": "Where is the gold?"}, {"role": "assistant", "content": "Buried in the sand, ye scallywag!"}]}
// You need 1,000+ of these high-quality examples to change behavior!`}
  },
  t159: {
    tag:'Phase 6 · Advanced', num:159,
    title:'Agent Frameworks (LangChain)',
    desc:'Orchestrating complex, multi-step LLM workflows and memory.',
    theory:`<div class="card"><h3>🧩 The Orchestration Layer</h3><p>Connecting an LLM to a Vector DB, managing conversation memory, and parsing the LLM's JSON tool calls manually requires hundreds of lines of complex boilerplate code.</p><h4>LangChain & AutoGen</h4><p>Frameworks like <strong>LangChain</strong> provide pre-built "Chains". You can easily chain together a Prompt Template -> an LLM -> an Output Parser -> and a Tool Executor in 5 lines of code. Advanced frameworks like <strong>Microsoft AutoGen</strong> allow you to create multiple different AI Agents (e.g., a "Coder Agent" and a "Reviewer Agent") that chat with each other to solve a complex task together!</p></div>`,
    mcqs:[
      {q:"What is the primary purpose of an LLM framework like LangChain?",opts:["A. To train new AI models","B. To provide abstractions and pre-built components (chains, memory, tool integrations) that make it incredibly fast to build complex AI applications and Agents without writing boilerplate code.","C. To generate UI components","D. To replace the OpenAI API"],ans:1,exp:"It acts as the glue between the LLM and your external databases and tools."},
      {q:"In LangChain, what is a 'Chain'?",opts:["A. A security feature","B. A sequence of automated steps (e.g., taking user input, injecting it into a prompt template, passing it to the LLM, and parsing the JSON output) linked together.","C. A database cluster","D. A blockchain ledger"],ans:1,exp:"The most famous chain is the 'ConversationalRetrievalChain' (RAG built-in)."},
      {q:"How do LLMs inherently handle 'Memory' (remembering what was said earlier in the chat)?",opts:["A. They store it in a SQL database","B. They don't. LLMs are completely stateless. You (or the framework) must append the entire conversation history to the prompt every single time you send a new message.","C. They use cookies","D. They save it to the hard drive"],ans:1,exp:"LangChain provides 'Memory' modules that automatically manage this growing conversation history for you."},
      {q:"What is Multi-Agent orchestration (e.g., Microsoft AutoGen)?",opts:["A. Running multiple servers","B. Creating a system where multiple distinct AI Agents (with different system prompts and tools) interact and debate with EACH OTHER to solve a massive task, rather than just talking to a human.","C. A multiplayer video game","D. A load balancing strategy"],ans:1,exp:"You could have a 'Researcher Agent' gather data, hand it to a 'Writer Agent', who hands it to an 'Editor Agent' for review."},
      {q:"What is a common criticism of using heavy frameworks like LangChain in production?",opts:["A. They are too fast","B. The abstractions can be too 'magical' and difficult to debug when things go wrong. Many senior engineers prefer writing the raw API calls (using the official SDKs) for more control.","C. They use too much CSS","D. They are illegal"],ans:1,exp:"Frameworks are amazing for prototyping, but sometimes standard code is better for production stability."}
    ],
    flows:[
      {title:"Multi-Agent AutoGen Flow",items:["start:Human Goal: 'Write a Python script for Snake'","proc:CoderAgent writes V1 script","dec:Passes code to ReviewerAgent","proc:ReviewerAgent finds bug -> Sends back to CoderAgent","end:CoderAgent fixes it. Final code sent to Human!"]}
    ],
    game:{icon:"🧩",title:"The Orchestrator",desc:"Master AI Frameworks",badges:["🧩 Chain Linker","🧠 Memory Manager","🤖 Multi-Agent Commander"],challenges:[{icon:"📝",title:"Stateless",desc:"How do LLMs remember chat history?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"A Simple Chain",badge:"Chainer",desc:"Understand the LangChain mental model.",tags:["AI","LangChain"],steps:[{title:"Prompt",desc:"Template: 'Translate {text} to French'"},{"title:"Model",desc:"Instantiate ChatOpenAI"},{"title:"Chain",desc:"const chain = prompt.pipe(model)"}],code:`// The LangChain Mental Model (LCEL)
// You build a pipeline (a chain) of operations.

const prompt = ChatPromptTemplate.fromTemplate("Tell me a joke about {topic}");
const model = new ChatOpenAI({});
const outputParser = new StringOutputParser();

// Create the Chain!
const chain = prompt.pipe(model).pipe(outputParser);

// Execute it!
const result = await chain.invoke({ topic: "bears" });`}
  },
  t160: {
    tag:'Phase 6 · Advanced', num:160,
    title:'System Observability',
    desc:'Monitoring, Logging, and Tracing: How to know what is actually happening in production.',
    theory:`<div class="card"><h3>📡 The Dashboard</h3><p>If you have 50 microservices running in Kubernetes and an API request fails, how do you know which service caused the error? You can't SSH into 50 servers to read text files.</p><h4>The Three Pillars</h4><ul><li><strong>Metrics (Prometheus & Grafana):</strong> Dashboards showing CPU usage, memory, and HTTP 500 error rates in real-time.</li><li><strong>Logs (Elasticsearch/Kibana or Datadog):</strong> Centralized, searchable text logs aggregated from every single container into one place.</li><li><strong>Distributed Tracing (Jaeger):</strong> Injecting a unique Request ID into an HTTP request. You can visually track that single request as it jumps through the API Gateway, the Auth Service, the Billing Service, and the Database, seeing exactly which hop caused the 3-second delay!</li></ul></div>`,
    mcqs:[
      {q:"What is 'Observability' in Software Engineering?",opts:["A. Looking at the UI","B. The ability to measure the internal state of a complex system (and quickly identify problems) based purely on the data it generates (Logs, Metrics, and Traces).","C. Writing documentation","D. Code reviews"],ans:1,exp:"Without observability, you are flying blind in production."},
      {q:"What are the 'Three Pillars of Observability'?",opts:["A. HTML, CSS, JS","B. Logs, Metrics, and Distributed Traces","C. AWS, Azure, Google Cloud","D. Unit Tests, Integration Tests, E2E Tests"],ans:1,exp:"Logs tell you WHAT happened. Metrics tell you HOW MUCH it's happening. Traces tell you WHERE it happened."},
      {q:"What is the primary use of Prometheus and Grafana?",opts:["A. To write code","B. Prometheus scrapes numeric 'Metrics' (like CPU%, Memory%, Request/Sec) from your servers. Grafana visualizes that data into beautiful, real-time graphs and dashboards.","C. To store images","D. To compile CSS"],ans:1,exp:"Grafana is where DevOps engineers set up alerts (e.g., 'Ping Slack if Error Rate > 5%')."},
      {q:"In a Microservices architecture, what is 'Distributed Tracing'?",opts:["A. Tracing a drawing","B. Attaching a unique 'Trace ID' to an incoming HTTP request at the API Gateway, and passing that ID to every downstream service. This allows you to visually trace the entire journey of one specific request across 10 different apps.","C. Finding lost databases","D. Tracing IP addresses"],ans:1,exp:"If a request takes 5 seconds, Jaeger or Zipkin will show you a waterfall graph revealing exactly which microservice caused the bottleneck."},
      {q:"What is Centralized Logging?",opts:["A. Putting all code in one file","B. Automatically streaming the console.log() output from hundreds of ephemeral Docker containers into one massive, searchable database (like Elasticsearch/Kibana or Datadog) so developers don't have to SSH into servers.","C. Writing logs to a local text file","D. Deleting logs daily"],ans:1,exp:"When a Pod dies in Kubernetes, its local logs die with it. Centralized logging saves them."}
    ],
    flows:[
      {title:"Distributed Tracing Flow",items:["start:User clicks 'Pay' -> Hits API Gateway","proc:Gateway generates TraceID 'XYZ-123'","dec:Gateway passes 'XYZ-123' to BillingService","proc:BillingService passes 'XYZ-123' to Stripe API","end:Datadog aggregates 'XYZ-123'. Shows 500ms total latency!"]}
    ],
    game:{icon:"📡",title:"The Observer",desc:"Master system monitoring",badges:["📈 Metric Master","🔎 Log Sleuth","🕵️ Trace Detective"],challenges:[{icon:"📝",title:"The 3 Pillars",desc:"Name Logs, Metrics, and...",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Trace ID Injection",badge:"Tracer",desc:"Pass a Trace ID between services.",tags:["DevOps","Observability"],steps:[{title:"Service A",desc:"Generates unique ID: 98765"},{"title:"The HTTP Call",desc:"Passes ID in header: 'X-Trace-Id: 98765'"},{"title:"Service B",desc:"Logs error: '[98765] DB Connection Failed'"}],code:`// Example of injecting a Trace ID in a Node.js microservice
const axios = require('axios');
const { v4: uuidv4 } = require('uuid');

app.get('/checkout', async (req, res) => {
  // 1. Generate or extract the Trace ID
  const traceId = req.headers['x-trace-id'] || uuidv4();

  // 2. Pass it to the next microservice!
  await axios.post('http://billing-service/charge', data, {
    headers: { 'X-Trace-Id': traceId }
  });

  // 3. Include it in all logs for easy searching in Datadog
  console.log(\`[\${traceId}] Checkout initiated\`);
});`}
  }
"""

start_marker = "};\n\nlet userXP"
inject_idx = content.find(start_marker)

if inject_idx != -1:
    new_content = content[:inject_idx] + ",\n" + rich_content + content[inject_idx:]
    with open(html_path, "w") as f:
        f.write(new_content)
    print("Successfully generated T151-T160 rich content!")
else:
    print("Could not find injection point.")
