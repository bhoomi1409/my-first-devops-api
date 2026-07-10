import re

html_path = "/Users/bhoomim/devops CI:CD/handbook/fullstack_ai_handbook.html"
with open(html_path, "r") as f:
    content = f.read()

rich_content = r"""
  t126: {
    tag:'Phase 4 · DevOps', num:126,
    title:'Container Registries',
    desc:'Where Docker Images are stored, distributed, and versioned.',
    theory:`<div class="card"><h3>☁️ The Image Cloud</h3><p>Once you build a Docker Image on your laptop (<code>docker build</code>), how do you get it to your AWS production server? You don't email it. You <strong>Push</strong> it to a <strong>Container Registry</strong>.</p><h4>Docker Hub & ECR</h4><p>A Container Registry is exactly like GitHub, but for compiled Docker Images instead of source code. <strong>Docker Hub</strong> is the default public registry. Enterprise companies use private registries like AWS ECR (Elastic Container Registry) to keep their proprietary app images secure.</p><div class="box b-vi"><h5>Tagging</h5><p>Just like Git commits, you should "Tag" your images (e.g., <code>myapp:v1.0</code>, <code>myapp:v1.1</code>). If v1.1 crashes in production, you can instantly pull and run v1.0 to rollback!</p></div></div>`,
    mcqs:[
      {q:"What is a Container Registry?",opts:["A. A database for user data","B. A centralized cloud storage repository where you push, pull, and version your compiled Docker Images","C. A tool for writing Dockerfiles","D. A load balancer"],ans:1,exp:"It acts exactly like GitHub, but for Docker Images."},
      {q:"What is the default, massive public registry provided by Docker?",opts:["A. AWS ECR","B. GitHub","C. Docker Hub","D. Google Cloud Storage"],ans:2,exp:"When you run 'docker pull ubuntu', it automatically fetches it from Docker Hub."},
      {q:"Why do enterprise companies use AWS ECR or Google GCR instead of Docker Hub?",opts:["A. Docker Hub is illegal for businesses","B. They need Private, highly secure registries tightly integrated with their cloud infrastructure to prevent their proprietary source code from being public","C. ECR is faster","D. ECR is free"],ans:1,exp:"You don't want competitors downloading your backend API's Docker Image!"},
      {q:"What does it mean to 'Tag' a Docker Image?",opts:["A. Adding a description to it","B. Assigning a version number or label to it (e.g., myapp:v2.0 or myapp:latest) so you can track changes and rollback if necessary","C. Deleting it","D. Encrypting it"],ans:1,exp:"If you don't provide a tag, Docker automatically applies the default tag ':latest'."},
      {q:"Which commands represent the correct workflow for sharing an image?",opts:["A. docker start -> docker upload","B. docker build -> docker push -> docker pull (on server)","C. docker pull -> docker build","D. docker compose -> docker down"],ans:1,exp:"Build it locally. Push it to the cloud. Pull it down to the server."}
    ],
    flows:[
      {title:"The Registry Workflow",items:["start:Laptop: docker build -t app:v1 .","proc:Laptop: docker push app:v1","dec:Image is stored in AWS ECR!","proc:Production Server: docker pull app:v1","end:Production Server: docker run app:v1"]}
    ],
    game:{icon:"☁️",title:"The Cloud Courier",desc:"Master Image distribution",badges:["☁️ Registry Pusher","🏷️ Tagger","🔙 Rollback Hero"],challenges:[{icon:"📝",title:"The Tag",desc:"What is the default tag?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Tag & Push",badge:"Distributor",desc:"Understand the push command sequence.",tags:["Docker","Terminal"],steps:[{title:"Build",desc:"docker build -t bhoomi/myapp:v1 ."},{"title:"Login",desc:"docker login (Auth with Hub)"},{"title:"Push",desc:"docker push bhoomi/myapp:v1"}],code:`# 1. Build the image and tag it with your DockerHub username\ndocker build -t myusername/my-api:v2.0 .\n\n# 2. Upload it to the cloud!\ndocker push myusername/my-api:v2.0\n\n# 3. On your AWS Server, pull it down and run it!\ndocker run -d -p 80:80 myusername/my-api:v2.0`}
  },
  t127: {
    tag:'Phase 4 · DevOps', num:127,
    title:'CI/CD Fundamentals',
    desc:'Continuous Integration and Continuous Deployment: Automating the software release process.',
    theory:`<div class="card"><h3>🤖 The Automation Pipeline</h3><p>In the old days, deploying a website meant a human developer manually running tests, building a ZIP file, logging into a server via FTP, and dragging files over. This was slow and error-prone.</p><h4>Continuous Integration (CI)</h4><p>Every time a developer pushes code to GitHub, an automated server instantly runs all Unit Tests and Security checks. If a test fails, the code is blocked from merging. This ensures the <code>main</code> branch is always perfectly stable.</p><h4>Continuous Deployment (CD)</h4><p>Once CI passes, the pipeline automatically builds the Docker Image, pushes it to the Registry, and deploys it to the Production Server without a human ever touching a button.</p></div>`,
    mcqs:[
      {q:"What is the primary goal of Continuous Integration (CI)?",opts:["A. To write code automatically","B. To automatically build and test code every time a developer commits changes to version control, catching bugs instantly before they reach the main branch","C. To deploy code to production","D. To hack servers"],ans:1,exp:"CI ensures that multiple developers working on the same project don't accidentally break each other's code."},
      {q:"What is the primary goal of Continuous Deployment (CD)?",opts:["A. To test code locally","B. To automatically release validated code from the repository directly to the Production environment without manual human intervention","C. To design UI","D. To manage databases"],ans:1,exp:"High-performing tech companies (like Amazon) deploy code to production thousands of times a day using CD."},
      {q:"If a Unit Test fails during the CI pipeline, what happens?",opts:["A. The pipeline ignores it","B. The pipeline fails (turns red), and the code is blocked from being merged or deployed until the developer fixes the bug","C. The database deletes itself","D. The app is deployed anyway"],ans:1,exp:"The pipeline acts as an automated quality control gatekeeper."},
      {q:"What is the difference between Continuous Delivery and Continuous Deployment?",opts:["A. They are identical","B. In Delivery, the code is ready to deploy, but a human must click an 'Approve' button. In Deployment, the deployment to production is 100% automated.","C. Delivery is for mail, Deployment is for code","D. Delivery is faster"],ans:1,exp:"Many banks use Delivery because regulatory compliance requires a human sign-off."},
      {q:"Why is CI/CD considered a massive competitive advantage for businesses?",opts:["A. It reduces the need for servers","B. It drastically reduces the 'Time to Market' for new features and bug fixes, transforming deployment from a scary monthly event into a boring, daily routine","C. It writes marketing copy","D. It replaces developers"],ans:1,exp:"Agility is everything in modern software."}
    ],
    flows:[
      {title:"The Complete CI/CD Pipeline",items:["start:Dev pushes code to GitHub PR","proc:CI: Runs Unit Tests & Linter","dec:Did Tests Pass? (Yes)","proc:Merge to 'main' branch","proc:CD: Builds Docker Image & Pushes to ECR","end:CD: Deploys to Kubernetes/AWS Server!"]}
    ],
    game:{icon:"🤖",title:"The Automator",desc:"Master CI/CD theory",badges:["🤖 Pipeline Builder","🛑 Gatekeeper","🚀 Instant Deployer"],challenges:[{icon:"📝",title:"Delivery vs Deployment",desc:"Explain the difference",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Pipeline Design",badge:"Architect",desc:"Mentally design a deployment pipeline.",tags:["DevOps","Concepts"],steps:[{title:"Trigger",desc:"On push to 'main' branch"},{"title:"Test",desc:"Run 'npm run test'. If fail, halt."},{"title:"Deploy",desc:"Run 'docker push' and restart server."}],code:`// The Philosophy of CI/CD:\n// Humans are terrible at doing repetitive tasks without making mistakes.\n// Computers are perfect at it.\n// Therefore, humans should write code, and computers should deploy it.`}
  },
  t128: {
    tag:'Phase 4 · DevOps', num:128,
    title:'GitHub Actions',
    desc:'The native CI/CD and automation tool built directly into GitHub.',
    theory:`<div class="card"><h3>🎬 Action!</h3><p>Historically, companies had to set up dedicated Jenkins servers to run their CI/CD pipelines. <strong>GitHub Actions</strong> revolutionized this by putting the CI/CD engine directly inside your GitHub repository.</p><h4>How it works</h4><p>You create a YAML file in the <code>.github/workflows/</code> directory. You define a <strong>Trigger</strong> (e.g., <code>on: push to main</code>). When triggered, GitHub spins up a temporary virtual machine in the cloud, checks out your code, and executes the <strong>Steps</strong> you defined (e.g., <code>npm install</code>, <code>npm test</code>).</p></div>`,
    mcqs:[
      {q:"What is the primary advantage of GitHub Actions over older tools like Jenkins?",opts:["A. It is faster","B. It requires zero server setup or maintenance. It is fully integrated into GitHub and runs your pipelines on Microsoft's cloud infrastructure.","C. It uses HTML instead of YAML","D. It replaces Docker"],ans:1,exp:"Jenkins requires you to manage your own servers, plugins, and security. Actions is Serverless CI/CD."},
      {q:"Where must your GitHub Actions YAML workflow files be stored in your repository?",opts:["A. In the root directory","B. Inside the .github/workflows/ directory","C. In the src/ folder","D. Inside a Dockerfile"],ans:1,exp:"GitHub automatically scans this specific folder for workflow files."},
      {q:"What does the 'on:' key do in a GitHub Actions workflow file?",opts:["A. Turns the server on","B. Defines the Trigger (the Event) that causes the workflow to run (e.g., on: push, on: pull_request, or on a cron schedule)","C. Specifies the operating system","D. Turns on debugging"],ans:1,exp:"You can trigger workflows on almost any GitHub event, even when an issue is created!"},
      {q:"If your workflow needs a secret API key to deploy to AWS, where should you store it?",opts:["A. Hardcode it in the YAML file","B. In the repository's 'GitHub Secrets' settings, then reference it in the YAML using ${{ secrets.AWS_KEY }}","C. In a public text file","D. In the README.md"],ans:1,exp:"Never commit secrets to version control. GitHub Secrets are encrypted and injected at runtime."},
      {q:"What is a 'Runner' in GitHub Actions?",opts:["A. The developer writing the code","B. The virtual machine (e.g., ubuntu-latest) that GitHub spins up to execute your workflow steps","C. A fast database","D. A testing framework"],ans:1,exp:"GitHub provides hosted runners, but you can also host your own runners if you need custom hardware."}
    ],
    flows:[
      {title:"GitHub Actions Flow",items:["start:.github/workflows/deploy.yml","proc:Trigger: on: push to main","dec:GitHub spins up 'ubuntu-latest' Runner","proc:Step 1: actions/checkout (Downloads code)","proc:Step 2: npm test","end:Step 3: Deploy to AWS!"]}
    ],
    game:{icon:"🎬",title:"The Director",desc:"Master GitHub Actions",badges:["🎬 Action Star","🏃 Runner Spawner","🤫 Secret Keeper"],challenges:[{icon:"📝",title:"The Trigger",desc:"How do you trigger on a pull request?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Basic Workflow",badge:"Scripter",desc:"Write a simple CI workflow.",tags:["CI/CD","GitHub"],steps:[{title:"Location",desc:".github/workflows/test.yml"},{"title:"Trigger",desc:"on: [push]"},{"title:"Jobs",desc:"runs-on: ubuntu-latest, steps: run npm test"}],code:`# .github/workflows/ci.yml\nname: Node.js CI\n\n# Trigger on pushes to main\non:\n  push:\n    branches: [ "main" ]\n\njobs:\n  build:\n    # Spin up an Ubuntu virtual machine\n    runs-on: ubuntu-latest\n\n    steps:\n    # Step 1: Download the code\n    - uses: actions/checkout@v3\n    \n    # Step 2: Install Node\n    - uses: actions/setup-node@v3\n      with: { node-version: 18 }\n      \n    # Step 3: Run the tests! If they fail, the workflow turns red!\n    - run: npm install\n    - run: npm test`}
  },
  t129: {
    tag:'Phase 4 · DevOps', num:129,
    title:'Jenkins vs GitLab CI',
    desc:'Comparing enterprise CI/CD solutions and their architectural philosophies.',
    theory:`<div class="card"><h3>🏭 The Factories</h3><p>While GitHub Actions is great for modern/small projects, massive enterprises often use different tools.</p><h4>Jenkins</h4><p>The grandfather of CI/CD. It is open-source, wildly customizable via thousands of plugins, but requires you to manage your own servers (Master/Worker nodes). Pipelines are written in a Groovy <code>Jenkinsfile</code>.</p><h4>GitLab CI</h4><p>Like GitHub Actions, it is deeply integrated into the GitLab version control system. It is heavily container-native (every step runs inside a Docker container) and relies on a clean <code>.gitlab-ci.yml</code> file. Highly favored by modern DevOps teams.</p></div>`,
    mcqs:[
      {q:"What is a major architectural difference between Jenkins and GitHub Actions/GitLab CI?",opts:["A. Jenkins only works with Java","B. Jenkins is a standalone server you must host and maintain yourself. Actions/GitLab CI are integrated seamlessly into the source control platform as a managed service.","C. Jenkins doesn't support Docker","D. Jenkins is faster"],ans:1,exp:"Maintaining a Jenkins server (updating plugins, securing it) is practically a full-time job."},
      {q:"What language/file format is traditionally used to define a Jenkins Pipeline?",opts:["A. YAML","B. A 'Jenkinsfile' written in Groovy syntax","C. JSON","D. XML"],ans:1,exp:"Groovy allows for complex programming logic inside the pipeline, but has a steep learning curve compared to simple YAML."},
      {q:"What is a core philosophy of GitLab CI?",opts:["A. It avoids using containers","B. It is heavily container-native. Every single 'job' in the pipeline can easily run inside its own isolated Docker container (e.g., image: node:18).","C. It requires Jenkins plugins","D. It only works on Windows"],ans:1,exp:"This guarantees that the environment running your tests is identical to production."},
      {q:"Why do many huge enterprises still use Jenkins today despite the maintenance overhead?",opts:["A. Because it's required by law","B. Because its massive ecosystem of plugins allows it to integrate with ancient legacy systems (mainframes, old testing suites) that modern tools ignore","C. Because it has the best UI","D. Because it is serverless"],ans:1,exp:"Jenkins can do absolutely anything, provided you spend the time configuring the plugins."},
      {q:"In CI/CD terminology, what is an 'Artifact'?",opts:["A. An old piece of code","B. A file (like a compiled .jar, a ZIP file, or test reports) generated during a pipeline run that is saved and passed to the next stage or stored for download","C. A database backup","D. A type of container"],ans:1,exp:"For example, the 'Build' stage creates a .jar artifact, and the 'Deploy' stage uses that artifact."}
    ],
    flows:[
      {title:"GitLab CI Architecture",items:["start:Developer pushes to GitLab","proc:GitLab Server reads .gitlab-ci.yml","proc:Sends Job to GitLab Runner (Agent)","dec:Runner boots a Docker container","end:Executes tests inside container, reports back!"]}
    ],
    game:{icon:"🏭",title:"The Factory Manager",desc:"Master enterprise CI/CD",badges:["🏭 Jenkins Master","🦊 GitLab Fan","📦 Artifact Collector"],challenges:[{icon:"📝",title:"Jenkinsfile",desc:"What language does it use?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"GitLab CI File",badge:"YAMLer",desc:"Write a basic GitLab CI config.",tags:["CI/CD","GitLab"],steps:[{title:"File",desc:".gitlab-ci.yml"},{"title:"Image",desc:"Specify default docker image: node:18"},{"title:"Script",desc:"Write the bash script to execute"}],code:`# .gitlab-ci.yml\n\n# Every job runs inside this Docker image!\nimage: node:18\n\nstages:\n  - test\n\nrun_unit_tests:\n  stage: test\n  script:\n    - echo "Installing dependencies..."\n    - npm install\n    - echo "Running tests..."\n    - npm test`}
  },
  t130: {
    tag:'Phase 4 · DevOps', num:130,
    title:'Blue/Green & Canary',
    desc:'Advanced zero-downtime deployment strategies to minimize risk in production.',
    theory:`<div class="card"><h3>🚦 Safe Rollouts</h3><p>Deploying new code to production is terrifying. If v2.0 has a fatal bug, you don't want all 100% of your users to crash instantly.</p><h4>Blue/Green Deployment</h4><p>You have two identical production environments. <strong>Blue</strong> is currently live running v1.0. You deploy v2.0 to <strong>Green</strong>. Once Green is fully tested, you flip the router switch. Green becomes live, Blue becomes standby. Zero downtime, instant rollback.</p><h4>Canary Deployment</h4><p>You deploy v2.0 to just a single server (or 5% of traffic) like a "canary in a coal mine". If the canary dies (error rates spike), you abort. If it survives, you slowly roll it out to 10%, 50%, 100%.</p></div>`,
    mcqs:[
      {q:"What is the primary goal of Blue/Green and Canary deployments?",opts:["A. To make the code compile faster","B. To achieve Zero-Downtime deployments and drastically reduce the risk of a new bug impacting 100% of the user base","C. To save money on servers","D. To encrypt the database"],ans:1,exp:"These strategies separate 'Deployment' (putting code on a server) from 'Release' (routing user traffic to that code)."},
      {q:"In a Blue/Green deployment, how do you rollback if the newly live 'Green' environment has a critical bug?",opts:["A. You have to recompile the old code","B. You simply flip the Load Balancer switch back to the 'Blue' environment (which is still sitting there untouched, running the old code)","C. You delete the database","D. You call AWS support"],ans:1,exp:"Rollbacks are nearly instantaneous, turning a panic situation into a minor hiccup."},
      {q:"What is a major downside or cost of a true Blue/Green deployment?",opts:["A. It is very slow","B. It requires you to temporarily provision and pay for 2x the amount of production infrastructure (two identical environments)","C. It only works for static sites","D. It causes downtime"],ans:1,exp:"This is why Kubernetes and containers made Blue/Green popular; spinning up virtual environments is cheap and fast."},
      {q:"How does a Canary deployment differ from Blue/Green?",opts:["A. It uses birds","B. Blue/Green is a 100% traffic flip. Canary slowly shifts a tiny percentage of traffic (e.g., 5%) to the new version to monitor metrics before a full rollout.","C. Canary requires downtime","D. Canary is only for databases"],ans:1,exp:"Canary is perfect for massive systems where synthetic testing isn't enough, and you need to see how real users interact with the new code safely."},
      {q:"What component is absolutely essential to orchestrate these advanced deployment strategies?",opts:["A. A CSS framework","B. An intelligent Load Balancer / API Gateway that can precisely route and split incoming HTTP traffic","C. A massive database","D. A message broker"],ans:1,exp:"The Load Balancer acts as the traffic cop, deciding who goes to Blue and who goes to Green."}
    ],
    flows:[
      {title:"Canary Rollout Flow",items:["start:100% Traffic -> Version 1.0","proc:Deploy Version 2.0 (Silent)","dec:Route 5% Traffic -> Version 2.0","proc:Monitor Error Logs on V2.0 for 10 mins","end:(If Safe) Route 100% -> Version 2.0"]}
    ],
    game:{icon:"🚦",title:"The Strategist",desc:"Master zero-downtime releases",badges:["🚦 Traffic Cop","🐦 Canary Miner","🔵🟢 Color Switcher"],challenges:[{icon:"📝",title:"The Flip",desc:"How is a Blue/Green rollback instant?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Strategy Selection",badge:"Architect",desc:"Pick the right deployment strategy.",tags:["DevOps","Concepts"],steps:[{title:"Scenario 1",desc:"Small app, need instant rollback -> Blue/Green"},{"title:"Scenario 2",desc:"Huge app, need to test UI on real users -> Canary"},{"title:"Scenario 3",desc:"Background worker task -> Rolling Update"}],code:`// Mental Architecture\n// Deployment != Release.\n// You should be able to Deploy code to production at 2 PM on a Friday.\n// You don't Release (route traffic) until Monday morning.`}
  },
"""

start_marker = "};\n\nlet userXP"
inject_idx = content.find(start_marker)

if inject_idx != -1:
    new_content = content[:inject_idx] + ",\n" + rich_content + content[inject_idx:]
    with open(html_path, "w") as f:
        f.write(new_content)
    print("Successfully generated T126-T130 rich content!")
else:
    print("Could not find injection point.")
