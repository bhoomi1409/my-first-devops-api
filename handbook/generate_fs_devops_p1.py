import re

html_path = "/Users/bhoomim/devops CI:CD/handbook/fullstack_ai_handbook.html"
with open(html_path, "r") as f:
    content = f.read()

rich_content = r"""
  t121: {
    tag:'Phase 4 · DevOps', num:121,
    title:'Virtualization vs Containers',
    desc:'The fundamental shift in how applications are packaged and deployed to servers.',
    theory:`<div class="card"><h3>📦 The Shipping Revolution</h3><p>In the past, you deployed code directly onto a physical server. If you needed multiple isolated environments, you used <strong>Virtual Machines (VMs)</strong>. A VM requires an entire, heavy Guest Operating System (like Windows or Ubuntu) to run on top of the Host OS.</p><h4>Enter Containers</h4><p>Containers (like Docker) are extremely lightweight. Instead of installing a full Guest OS, they share the Host OS Kernel. They only package the application code and the exact libraries/dependencies it needs. They boot in milliseconds instead of minutes!</p></div>`,
    mcqs:[
      {q:"What is the primary difference between a Virtual Machine (VM) and a Container?",opts:["A. VMs are for Linux, Containers are for Windows","B. VMs include a full, heavy Guest Operating System. Containers share the Host OS kernel and only package the app and its dependencies, making them incredibly lightweight and fast.","C. Containers are less secure","D. VMs are free"],ans:1,exp:"You can run 100 containers on a server that might only be able to run 5 VMs."},
      {q:"Why do developers say 'But it works on my machine!'?",opts:["A. Because their machine is faster","B. Because their local environment (Node version, OS, specific libraries) is different from the Production server. Containers completely eliminate this problem.","C. Because of Windows updates","D. It's a joke"],ans:1,exp:"If a container runs on your laptop, it is guaranteed to run exactly the same way on AWS."},
      {q:"What does a Container actually contain?",opts:["A. A database","B. The application code, runtime (e.g., Node.js), system tools, system libraries, and settings. Everything needed to run the app.","C. The physical server","D. An internet connection"],ans:1,exp:"It acts as an isolated, self-sufficient package."},
      {q:"Do containers use a Hypervisor?",opts:["A. Yes, always","B. No, VMs use Hypervisors (like VMware or VirtualBox) to emulate hardware. Containers use a Container Engine (like Docker) to isolate processes at the OS level.","C. Only on Macs","D. Yes, for security"],ans:1,exp:"The lack of hardware emulation is what makes containers so fast."},
      {q:"Which of the following is the most famous containerization platform?",opts:["A. Apache","B. Docker","C. Jenkins","D. Git"],ans:1,exp:"Docker revolutionized the entire software industry in the 2010s."}
    ],
    flows:[
      {title:"VM vs Container Architecture",items:["start:Server Hardware -> Host OS","dec:Virtual Machines:","proc:Hypervisor -> Guest OS -> App (Heavy)","dec:Containers:","end:Docker Engine -> App (Lightweight)"]}
    ],
    game:{icon:"📦",title:"The Shipper",desc:"Master containerization",badges:["📦 Packager","⚡ Fast Booter","💻 Works On My Machine"],challenges:[{icon:"📝",title:"Guest OS",desc:"Why don't containers need a Guest OS?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Isolation Concept",badge:"Isolator",desc:"Understand process isolation.",tags:["DevOps","Docker"],steps:[{title:"The Problem",desc:"App A needs Python 2. App B needs Python 3."},{"title:"The VM Way",desc:"Spin up 2 entire Ubuntu VMs. Heavy!"},{"title:"The Container Way",desc:"Spin up 2 isolated Docker containers on 1 OS. Fast!"}],code:`// Containers solve dependency conflicts!\n// You can run a Postgres 12 container and a Postgres 14 container\n// on the exact same laptop at the exact same time, \n// and they will NEVER interfere with each other.`}
  },
  t122: {
    tag:'Phase 4 · DevOps', num:122,
    title:'Docker Basics',
    desc:'Images vs Containers: The core concepts of the Docker ecosystem.',
    theory:`<div class="card"><h3>🐋 The Blueprint and the House</h3><p>To use Docker, you must understand the difference between an Image and a Container.</p><ul><li><strong>Docker Image:</strong> A read-only template containing your code and dependencies. It is the blueprint. (Like a Java Class).</li><li><strong>Docker Container:</strong> A running, live instance of an Image. You can start, stop, delete, and run multiple containers from a single Image. (Like a Java Object).</li></ul><div class="box b-vi"><h5>Common Commands</h5><p><code>docker pull ubuntu</code> (Downloads the image). <br><code>docker run ubuntu</code> (Creates and starts a live container from the image).</p></div></div>`,
    mcqs:[
      {q:"What is the relationship between a Docker Image and a Docker Container?",opts:["A. They are the same thing","B. An Image is the read-only blueprint (the recipe). A Container is the live, running instance created from that Image (the baked cake).","C. Containers create Images","D. Images are for UI, Containers are for Backend"],ans:1,exp:"You can run 10 identical Containers from 1 single Image."},
      {q:"If you want to download a pre-built Image (like MySQL) from the internet, what command do you use?",opts:["A. docker get mysql","B. docker download mysql","C. docker pull mysql","D. docker fetch mysql"],ans:2,exp:"This pulls the image from Docker Hub to your local hard drive."},
      {q:"What does the 'docker run' command do?",opts:["A. Makes the computer run faster","B. It takes a Docker Image, creates a Container from it, and starts it","C. It deletes an Image","D. It compiles Java code"],ans:1,exp:"docker run = docker create + docker start."},
      {q:"If you delete a Docker Container, what happens to the Docker Image it was created from?",opts:["A. The Image is also deleted","B. Nothing. The Image remains safely on your hard drive, ready to spawn new containers.","C. The Image corrupts","D. The OS crashes"],ans:1,exp:"Images are immutable (read-only)."},
      {q:"What does the command 'docker ps' do?",opts:["A. Pauses the system","B. Lists all currently running containers on your machine","C. Prints the screen","D. Pushes to github"],ans:1,exp:"Add '-a' (docker ps -a) to see stopped containers as well."}
    ],
    flows:[
      {title:"The Docker Lifecycle",items:["start:Write Code","proc:Build an Image (Blueprint)","proc:Push Image to Registry (Docker Hub)","dec:Server Pulls Image","end:Server Runs Container (Live App)"]}
    ],
    game:{icon:"🐋",title:"The Captain",desc:"Master Images and Containers",badges:["🐋 Docker Captain","🖼️ Image Builder","🏃 Container Runner"],challenges:[{icon:"📝",title:"Analogy",desc:"Image : Container :: Class : ?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Run a Web Server",badge:"Deployer",desc:"Launch a live NGINX server in 1 command.",tags:["Docker","Terminal"],steps:[{title:"The Command",desc:"Run: docker run -d -p 8080:80 nginx"},{"title:"Breakdown 1",desc:"-d means Detached (runs in background)"},{"title:"Breakdown 2",desc:"-p 8080:80 maps your laptop port to container port"}],code:`# Run a fully configured Nginx web server instantly\ndocker run -d -p 8080:80 nginx\n\n# -d: Run in detached mode (background)\n# -p: Map Port 8080 on your Mac to Port 80 inside the container\n# nginx: The official Image name\n\n# Now, go to http://localhost:8080 in your browser!`}
  },
  t123: {
    tag:'Phase 4 · DevOps', num:123,
    title:'Dockerfile & Build Context',
    desc:'Writing the instructions to build your own custom Docker Images.',
    theory:`<div class="card"><h3>📜 The Recipe Book</h3><p>To create your own custom Docker Image (e.g., to package your Node.js app), you create a plain text file named exactly <strong>Dockerfile</strong>.</p><h4>Core Instructions</h4><ul><li><code>FROM ubuntu:20.04</code>: Every image starts from a base image.</li><li><code>WORKDIR /app</code>: Sets the folder inside the container where commands will run.</li><li><code>COPY . .</code>: Copies files from your laptop (the Build Context) into the container.</li><li><code>RUN npm install</code>: Executes commands <em>during</em> the build process (creates a new layer in the image).</li><li><code>CMD ["npm", "start"]</code>: The default command that executes <em>when the container starts</em>.</li></ul></div>`,
    mcqs:[
      {q:"What is a Dockerfile?",opts:["A. A zip file","B. A plain text file containing a sequence of instructions (like FROM, RUN, COPY) used to automatically build a Docker Image","C. A database table","D. An HTML file"],ans:1,exp:"It is the exact recipe for your environment."},
      {q:"What does the 'FROM' instruction do in a Dockerfile?",opts:["A. Tells Docker who wrote it","B. Defines the Base Image you are building on top of (e.g., FROM node:18-alpine). It must be the first instruction.","C. Sends an email","D. Copies a folder"],ans:1,exp:"You rarely start from scratch. You start from a pre-built OS or runtime."},
      {q:"What is the critical difference between the 'RUN' instruction and the 'CMD' instruction?",opts:["A. They are exactly the same","B. RUN executes a command DURING the image build process (like installing dependencies). CMD specifies the command to execute WHEN the live Container actually starts (like starting the web server).","C. RUN is for Windows, CMD is for Linux","D. CMD is faster"],ans:1,exp:"RUN is for the kitchen (building). CMD is for serving the meal (running)."},
      {q:"What does 'COPY . .' do in a Dockerfile?",opts:["A. Deletes all files","B. Copies all files from your local laptop's current directory (the build context) into the Container's current directory","C. Copies the database","D. Copies the internet"],ans:1,exp:"This is how your source code gets inside the Image."},
      {q:"How do you actually execute a Dockerfile to create an Image?",opts:["A. docker create","B. docker build -t my-app-name .","C. docker make","D. docker compile"],ans:1,exp:"The '.' at the end tells Docker to use the current directory as the Build Context."}
    ],
    flows:[
      {title:"Image Building Flow",items:["start:Create Dockerfile","proc:Run 'docker build -t my-app .'","proc:Docker downloads Base Image (FROM)","dec:Docker copies your files (COPY)","proc:Docker installs dependencies (RUN)","end:Outputs final immutable Image!"]}
    ],
    game:{icon:"📜",title:"The Chef",desc:"Master Dockerfiles",badges:["📜 Recipe Writer","🧱 Layer Builder","🏃 CMD Starter"],challenges:[{icon:"📝",title:"RUN vs CMD",desc:"Explain the difference",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Node.js Dockerfile",badge:"Packager",desc:"Write a Dockerfile for a Node app.",tags:["Docker","Dockerfile"],steps:[{title:"Base",desc:"FROM node:18-alpine"},{"title:"Files",desc:"WORKDIR /app, then COPY . ."},{"title:"Install & Run",desc:"RUN npm install, then CMD ['npm', 'start']"}],code:`# Standard Dockerfile for a Node.js App\n\n# 1. Start with a tiny Linux OS that already has Node installed\nFROM node:18-alpine\n\n# 2. Set the working directory inside the container\nWORKDIR /usr/src/app\n\n# 3. Copy our code from laptop to container\nCOPY package.json ./\nCOPY . .\n\n# 4. Install dependencies (Happens during BUILD)\nRUN npm install\n\n# 5. What to run when the container STARTS\nCMD ["npm", "start"]`}
  },
  t124: {
    tag:'Phase 4 · DevOps', num:124,
    title:'Docker Volumes',
    desc:'Persisting data outside the ephemeral container lifecycle.',
    theory:`<div class="card"><h3>💾 The Memory Drive</h3><p>By default, everything inside a Docker Container is <strong>Ephemeral (Temporary)</strong>. If you run a Postgres database container, save 100 users, and then delete the container... the database and all 100 users are permanently destroyed!</p><h4>Volumes to the Rescue</h4><p>A <strong>Docker Volume</strong> is a folder on your actual Host machine (your laptop or the AWS server) that is mapped into the container. When Postgres saves a user, it actually saves it to your laptop's hard drive. If the container is destroyed, the data safely remains on the Host, ready to be mounted to a new container!</p></div>`,
    mcqs:[
      {q:"What happens to the data inside a container when the container is deleted?",opts:["A. It is uploaded to the cloud","B. It is permanently destroyed (ephemeral storage)","C. It is emailed to you","D. It is saved to the desktop"],ans:1,exp:"Containers are meant to be disposable. Never store critical data purely inside a container."},
      {q:"How do you solve the ephemeral data problem for databases running in Docker?",opts:["A. Don't use Docker for databases","B. Use Docker Volumes to mount a directory from the Host OS into the container, allowing data to persist independently of the container's lifecycle","C. Run a cron job to backup the container every 5 seconds","D. Zip the container"],ans:1,exp:"Volumes bypass the container's Union File System, writing directly to the host."},
      {q:"What is a 'Bind Mount'?",opts:["A. Tying two containers together with rope","B. Mapping a specific, exact file path on your laptop (e.g., /Users/me/code) into the container (e.g., /app). Great for live-reloading code during development!","C. Mounting a USB drive","D. Binding an IP address"],ans:1,exp:"If you edit a file in a Bind Mount on your laptop, the container sees the change instantly."},
      {q:"What is the command flag used to attach a volume when running a container?",opts:["A. -attach","B. -v or --volume (e.g., docker run -v /my/data:/container/data)","C. -mount","D. -disk"],ans:1,exp:"The syntax is usually -v host_path:container_path."},
      {q:"Can multiple containers share the exact same Volume simultaneously?",opts:["A. Yes, making Volumes a great way to share data between containers","B. No, the Volume locks to one container","C. Only on Windows","D. Only if they are the same image"],ans:0,exp:"For example, a Web container could upload images to a Volume, and an AI container could read from that same Volume."}
    ],
    flows:[
      {title:"The Volume Lifeline",items:["start:Start DB Container (Mounts Volume)","proc:Insert 5 rows -> Writes to Volume on Host","dec:Delete DB Container!","proc:Data inside container dies. Volume survives!","end:Start NEW DB Container (Mounts same Volume) -> Data is still there!"]}
    ],
    game:{icon:"💾",title:"The Persister",desc:"Master data persistence",badges:["💾 Volume Creator","🔗 Bind Mounter","👻 Ephemeral Survivor"],challenges:[{icon:"📝",title:"The Danger",desc:"What happens if you don't use a volume for a DB?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Live Reload",badge:"Developer",desc:"Use a Bind Mount for local dev.",tags:["Docker","Dev"],steps:[{title:"The Problem",desc:"Rebuilding an image every time you change 1 line of JS is slow."},{"title:"The Mount",desc:"docker run -v $(pwd):/app node-server"},{"title:"The Magic",desc:"Edit code on laptop -> Container updates instantly!"}],code:`# Start a Node app, mapping your current laptop directory to /app\ndocker run -d -p 3000:3000 -v $(pwd):/app my-node-image\n\n# Now, if you change 'index.js' in VSCode on your Mac,\n# the container instantly sees the change without a rebuild!\n# (Usually paired with Nodemon for auto-restarting)`}
  },
  t125: {
    tag:'Phase 4 · DevOps', num:125,
    title:'Docker Compose',
    desc:'A tool for defining and running multi-container Docker applications.',
    theory:`<div class="card"><h3>🎼 The Orchestrator</h3><p>Real applications aren't just one container. You usually need a Frontend container, a Backend container, and a Database container. Running 3 massive <code>docker run -p 80:80 -v ... --network ...</code> commands in the terminal every time you boot up is a nightmare.</p><h4>docker-compose.yml</h4><p><strong>Docker Compose</strong> lets you define your entire multi-container architecture in a single, readable YAML file. With one command (<code>docker-compose up</code>), Docker will create a private network, build all images, attach all volumes, and start all the containers in the correct order!</p></div>`,
    mcqs:[
      {q:"What specific problem does Docker Compose solve?",opts:["A. It writes your code","B. It eliminates the need to run long, complex 'docker run' terminal commands by letting you define multi-container environments in a single declarative YAML file","C. It hosts your website on AWS","D. It replaces Kubernetes"],ans:1,exp:"It acts as documentation AND execution for your architecture."},
      {q:"What file format does Docker Compose use?",opts:["A. JSON","B. YAML (docker-compose.yml)","C. XML","D. HTML"],ans:1,exp:"YAML relies on strict indentation (spaces) to define structure."},
      {q:"If your docker-compose.yml defines a 'frontend' and a 'backend' service, how do they talk to each other?",opts:["A. They use public IP addresses","B. Docker Compose automatically creates a private virtual Network for them. The frontend can talk to the backend simply by making an HTTP request to 'http://backend'.","C. They can't talk","D. Through a text file"],ans:1,exp:"Docker Compose provides automatic DNS resolution based on the service names you define!"},
      {q:"What is the single command used to start all services defined in a docker-compose.yml file?",opts:["A. docker start all","B. docker-compose up","C. compose run","D. docker-compose play"],ans:1,exp:"Add the '-d' flag to run them in the background (detached)."},
      {q:"What does 'docker-compose down' do?",opts:["A. Shuts down your computer","B. Stops and completely removes all containers, networks, and (optionally) volumes created by 'up'","C. Downloads the code","D. Downgrades Docker"],ans:1,exp:"It perfectly cleans up your development environment."}
    ],
    flows:[
      {title:"Compose Magic Flow",items:["start:Run 'docker-compose up -d'","proc:Creates private virtual network","proc:Boots 'db' container (Postgres)","dec:Boots 'api' container (Node)","end:'api' connects to 'db' instantly via internal DNS!"]}
    ],
    game:{icon:"🎼",title:"The Conductor",desc:"Master multi-container setups",badges:["🎼 Composer","🕸️ Networker","📜 YAML Writer"],challenges:[{icon:"📝",title:"Internal DNS",desc:"How does Compose link containers?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"A Full Stack File",badge:"Architect",desc:"Write a basic docker-compose file.",tags:["Docker","Compose"],steps:[{title:"Version",desc:"version: '3.8'"},{"title:"Services",desc:"Define 'web' (nginx) and 'db' (postgres)"},{"title:"Ports",desc:"Map web port 8080:80"}],code:`version: '3.8'\nservices:\n  # Service 1: The Backend API\n  api:\n    build: .             # Builds the Dockerfile in current dir\n    ports:\n      - "8080:8080"\n    depends_on:\n      - database         # Waits for DB to start first\n\n  # Service 2: The Database\n  database:\n    image: postgres:14   # Pulls official image\n    environment:\n      POSTGRES_PASSWORD: secret\n    volumes:\n      - db_data:/var/lib/postgresql/data\n\nvolumes:\n  db_data: # Declares a persistent volume`}
  },
"""

start_marker = "};\n\nlet userXP"
inject_idx = content.find(start_marker)

if inject_idx != -1:
    new_content = content[:inject_idx] + ",\n" + rich_content + content[inject_idx:]
    with open(html_path, "w") as f:
        f.write(new_content)
    print("Successfully generated T121-T125 rich content!")
else:
    print("Could not find injection point.")
