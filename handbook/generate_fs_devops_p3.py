import re

html_path = "/Users/bhoomim/devops CI:CD/handbook/fullstack_ai_handbook.html"
with open(html_path, "r") as f:
    content = f.read()

rich_content = r"""
  t131: {
    tag:'Phase 4 · DevOps', num:131,
    title:'Kubernetes (K8s) Architecture',
    desc:'The industry-standard container orchestration platform.',
    theory:`<div class="card"><h3>🚢 The Orchestrator</h3><p>Docker is great for running 1 or 2 containers on your laptop. But what if you have 500 containers spread across 50 physical servers? How do you know which server has free RAM? What happens if a server catches fire? You need an Orchestrator.</p><h4>K8s Architecture</h4><p><strong>Kubernetes (K8s)</strong> solves this. It acts as the brain of your datacenter.</p><ul><li><strong>Master Node (Control Plane):</strong> The brain. It exposes the API, schedules containers, and monitors cluster health.</li><li><strong>Worker Nodes:</strong> The actual physical servers (or VMs) that run your application containers.</li><li><strong>Kubelet:</strong> The agent running on every Worker Node that takes orders from the Master.</li></ul></div>`,
    mcqs:[
      {q:"What is the primary purpose of Kubernetes (K8s)?",opts:["A. To write Dockerfiles","B. To automate the deployment, scaling, networking, and management of thousands of containerized applications across a cluster of servers","C. To host static websites","D. To compile code"],ans:1,exp:"K8s turns a fleet of 100 separate servers into one giant, logical computer."},
      {q:"In Kubernetes architecture, what does the Master Node (Control Plane) do?",opts:["A. It runs your application code","B. It acts as the brain: managing the cluster state, scheduling containers onto Worker Nodes, and exposing the Kubernetes API","C. It hosts the database","D. It writes logs"],ans:1,exp:"You never run your own app code on the Master Node. It is reserved purely for K8s administrative tasks."},
      {q:"What happens if a Worker Node (physical server) suddenly loses power and dies in a Kubernetes cluster?",opts:["A. The app goes offline forever","B. The Master Node detects the failure, and automatically reschedules the dead containers onto healthy Worker Nodes (Self-Healing)","C. Kubernetes crashes","D. The database is wiped"],ans:1,exp:"This self-healing capability is the primary reason enterprises use K8s. It guarantees high availability."},
      {q:"Why is Kubernetes often abbreviated as 'K8s'?",opts:["A. Because it was the 8th version","B. It's a numeronym: 'K' followed by 8 letters, followed by 's'","C. Because it requires 8 servers","D. It stands for Kubernetes 8 Servers"],ans:1,exp:"A common tech naming convention (like i18n for internationalization)."},
      {q:"What is the command-line tool used by developers to interact with the Kubernetes Master Node API?",opts:["A. docker","B. kubectl (kube-control)","C. k8s-cli","D. kube-run"],ans:1,exp:"kubectl apply -f deployment.yaml is the most common command in DevOps."}
    ],
    flows:[
      {title:"K8s Self-Healing Flow",items:["start:Desired State: 3 Web Containers","proc:Node 2 Catches Fire (1 Container dies)","dec:Master Node detects Current State = 2","proc:Master Node schedules new container on Node 3","end:Current State = 3. Cluster is healed!"]}
    ],
    game:{icon:"🚢",title:"The Captain",desc:"Master K8s architecture",badges:["🚢 Orchestrator","🧠 Control Plane","🩹 Self-Healer"],challenges:[{icon:"📝",title:"K8s Meaning",desc:"Why K8s?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Cluster Visualization",badge:"Admin",desc:"Understand Master vs Worker.",tags:["Kubernetes","Architecture"],steps:[{title:"Master",desc:"API Server, Scheduler, Controller Manager"},{"title:"Worker 1",desc:"Kubelet running 2 Node.js containers"},{"title:"Worker 2",desc:"Kubelet running 1 Postgres container"}],code:`// Mental Model of a K8s Cluster\n// [ Master Node (The Brain) ]\n//       |               |\n// [ Worker Node 1 ] [ Worker Node 2 ]\n// (Runs App Code)   (Runs App Code)`}
  },
  t132: {
    tag:'Phase 4 · DevOps', num:132,
    title:'Pods & Deployments',
    desc:'The fundamental building blocks and controllers of Kubernetes applications.',
    theory:`<div class="card"><h3>🫛 The Atomic Unit</h3><p>Kubernetes does NOT run Docker Containers directly. It wraps them in a higher-level abstraction called a <strong>Pod</strong>.</p><h4>Pods</h4><p>A Pod is the smallest deployable unit in K8s. A Pod usually contains exactly 1 container (e.g., a Node.js app). Pods are ephemeral; if they die, they are never resurrected, they are replaced.</p><h4>Deployments</h4><p>You almost never create a Pod manually. You create a <strong>Deployment</strong>. A Deployment is a YAML file where you declare the <em>Desired State</em>. "I want 3 replicas of the Node.js Pod." The Deployment Controller ensures exactly 3 Pods are running at all times. If you want to update to v2.0, the Deployment handles the Rolling Update automatically!</p></div>`,
    mcqs:[
      {q:"What is the smallest, most basic deployable object in Kubernetes?",opts:["A. A Container","B. A Pod (which wraps one or more closely related containers)","C. A Node","D. A Service"],ans:1,exp:"K8s abstracts away the container runtime (Docker, containerd) by interacting with Pods."},
      {q:"Can a single Pod contain multiple Docker containers?",opts:["A. No, strictly one","B. Yes, though it's an advanced pattern (like a 'Sidecar' container handling logging while the main container handles the app). They share the same IP and localhost.","C. Only in Windows","D. Yes, but they can't communicate"],ans:1,exp:"Because they share localhost, the main app can just talk to the sidecar via 127.0.0.1."},
      {q:"Why should you rarely create standalone Pods using 'kubectl run'?",opts:["A. It is illegal","B. Standalone pods are unmanaged. If the node dies, the pod dies forever. You should use a Deployment, which automatically manages and replaces dead pods.","C. It costs money","D. It is too slow"],ans:1,exp:"Deployments provide the self-healing and scaling magic of K8s."},
      {q:"In a K8s Deployment YAML, what does 'replicas: 5' mean?",opts:["A. Run the code 5 times faster","B. The Deployment will ensure exactly 5 identical Pods are running across the cluster at all times, providing high availability and load balancing","C. Create 5 databases","D. Backup the data 5 times"],ans:1,exp:"If you want to scale up for Black Friday, just change it to 'replicas: 100' and apply it!"},
      {q:"How does a Deployment handle a software update (e.g., v1.0 to v2.0)?",opts:["A. It deletes everything and causes downtime","B. It performs a Rolling Update. It starts one v2.0 pod, waits for it to be healthy, then kills one v1.0 pod, repeating until all pods are updated with zero downtime.","C. It asks the user","D. It opens a PR"],ans:1,exp:"Zero-downtime deployments are built directly into the core of K8s."}
    ],
    flows:[
      {title:"Deployment Rolling Update",items:["start:Current: 3 Pods (v1.0)","proc:Admin applies Deployment (v2.0)","proc:K8s spins up 1 Pod (v2.0)","dec:Is v2.0 Pod healthy? (Yes)","end:K8s kills 1 Pod (v1.0). Repeats until finished!"]}
    ],
    game:{icon:"🫛",title:"The Pod Caster",desc:"Master Pods and Deployments",badges:["🫛 Pod Wrapper","📜 YAML Declarer","🔄 Rolling Updater"],challenges:[{icon:"📝",title:"Sidecar",desc:"What is a Sidecar container?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Deployment YAML",badge:"Declarer",desc:"Write a K8s Deployment configuration.",tags:["Kubernetes","YAML"],steps:[{title:"Header",desc:"kind: Deployment"},{"title:"Spec",desc:"replicas: 3"},{"title:"Template",desc:"image: my-node-app:v1"}],code:`apiVersion: apps/v1\nkind: Deployment\nmetadata:\n  name: my-web-app\nspec:\n  replicas: 3 # The Magic Number!\n  selector:\n    matchLabels:\n      app: web\n  template: # The Pod Blueprint\n    metadata:\n      labels:\n        app: web\n    spec:\n      containers:\n      - name: my-node-container\n        image: my-node-app:v1.0`}
  },
  t133: {
    tag:'Phase 4 · DevOps', num:133,
    title:'Services & Ingress',
    desc:'Exposing your Kubernetes Pods to the internal network and the outside world.',
    theory:`<div class="card"><h3>🌐 The Network Map</h3><p>Pods are mortal. They die and are reborn with <strong>brand new IP addresses</strong> constantly. If your Frontend Pod tries to talk to a Backend Pod via its IP address, it will break immediately when the Backend Pod dies.</p><h4>K8s Services</h4><p>A <strong>Service</strong> provides a static, permanent IP address and a DNS name (e.g., <code>http://backend-svc</code>) for a group of Pods. It acts as an internal load balancer. The Frontend talks to the Service, and the Service routes traffic to whatever Backend Pods are currently alive.</p><h4>Ingress</h4><p>A Service only works <em>inside</em> the cluster. To let a user on the internet access your app, you use an <strong>Ingress</strong>. It acts as the API Gateway, handling external HTTP routing and SSL certificates.</p></div>`,
    mcqs:[
      {q:"Why is it a terrible idea for one Pod to communicate with another Pod using its direct IP address?",opts:["A. IP addresses are too long","B. Pods are ephemeral; when they die and get recreated by a Deployment, they get a completely new, unpredictable IP address","C. Pods don't have IP addresses","D. It violates security"],ans:1,exp:"You need an abstraction layer to handle the dynamic IPs."},
      {q:"What is a Kubernetes Service?",opts:["A. A customer support ticket","B. A stable, permanent networking abstraction (with a static IP and DNS name) that acts as an internal load balancer across a dynamic group of Pods","C. A database table","D. A container image"],ans:1,exp:"If the frontend calls 'http://billing-service', K8s DNS automatically routes it to a live billing Pod."},
      {q:"How does a Service know WHICH Pods it is supposed to route traffic to?",opts:["A. Using MAC addresses","B. Using Label Selectors. The Service looks for any Pods that have matching labels (e.g., app: billing) and routes traffic to them.","C. Using GPS","D. Using port numbers"],ans:1,exp:"Labels and Selectors are the core way objects connect to each other in Kubernetes."},
      {q:"What is the difference between a ClusterIP Service and a NodePort/LoadBalancer Service?",opts:["A. ClusterIP is for Windows, NodePort is for Linux","B. ClusterIP is strictly INTERNAL to the cluster. NodePort/LoadBalancer expose the Service to the OUTSIDE internet.","C. ClusterIP is faster","D. There is no difference"],ans:1,exp:"Never expose a database Service to the outside internet! Keep it ClusterIP."},
      {q:"What is a K8s Ingress?",opts:["A. An exit door","B. An advanced HTTP routing layer (API Gateway) that sits at the edge of the cluster, mapping domain names (e.g. api.myapp.com) to internal Services, handling SSL termination","C. A security firewall","D. A storage volume"],ans:1,exp:"Ingress is much more powerful and cost-effective than creating an expensive Cloud Load Balancer for every single microservice."}
    ],
    flows:[
      {title:"External Network Flow",items:["start:User visits myapp.com","proc:Hits K8s Ingress Controller","dec:Ingress routes '/api' to Backend-Service","proc:Backend-Service load balances to Pod 2","end:Pod 2 processes request!"]}
    ],
    game:{icon:"🌐",title:"The Router",desc:"Master K8s networking",badges:["🌐 DNS Master","🏷️ Label Selector","🚪 Ingress Gatekeeper"],challenges:[{icon:"📝",title:"Ephemeral IPs",desc:"Why do we need Services?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Service YAML",badge:"Connector",desc:"Write a Service to expose a Deployment.",tags:["Kubernetes","YAML"],steps:[{title:"Kind",desc:"kind: Service"},{"title:"Selector",desc:"selector: app: my-backend (Matches Pod labels)"},{"title:"Ports",desc:"port: 80, targetPort: 8080"}],code:`apiVersion: v1\nkind: Service\nmetadata:\n  name: my-backend-service\nspec:\n  type: ClusterIP # Internal network only!\n  selector:\n    app: web # Routes to ANY pod with this label\n  ports:\n    - port: 80       # The Service's port\n      targetPort: 3000 # The Pod's actual port`}
  },
  t134: {
    tag:'Phase 4 · DevOps', num:134,
    title:'ConfigMaps & Secrets',
    desc:'Decoupling configuration and sensitive data from your container images.',
    theory:`<div class="card"><h3>🔐 Environment Variables</h3><p>If you hardcode your database URL or API Key directly into your Node.js code, you have to build a completely new Docker Image just to change the password. This is a massive anti-pattern.</p><h4>ConfigMaps</h4><p>A <strong>ConfigMap</strong> is a K8s object that stores non-confidential data in key-value pairs (like <code>DB_HOST=10.0.0.5</code>). You can inject this map into your Pods as Environment Variables. Now, one Docker Image can run in Dev, QA, and Prod just by changing the ConfigMap!</p><h4>Secrets</h4><p>A <strong>Secret</strong> is exactly like a ConfigMap, but it is meant for passwords and API keys. It is base64 encoded and can be encrypted at rest.</p></div>`,
    mcqs:[
      {q:"Why is it an anti-pattern to hardcode configuration data (like database URLs) into your Docker Image?",opts:["A. It makes the image too large","B. It violates the 'Build Once, Deploy Anywhere' rule. You should inject config at runtime so the exact same Image can be tested in QA and deployed to Prod.","C. It breaks the compiler","D. It causes memory leaks"],ans:1,exp:"The Twelve-Factor App methodology states configuration should be strictly separated from code."},
      {q:"What is a Kubernetes ConfigMap?",opts:["A. A map of the cluster layout","B. An API object used to store non-confidential data in key-value pairs, which can be injected into Pods as Environment Variables or files","C. A routing table","D. A database schema"],ans:1,exp:"You can update a ConfigMap and the Pod will receive the new environment variables upon restart."},
      {q:"What is the difference between a ConfigMap and a Secret in Kubernetes?",opts:["A. They are identical","B. Secrets are specifically designed for sensitive data (passwords, SSH keys). They are base64 encoded, can be encrypted at rest, and have tighter access controls.","C. Secrets are for Windows, ConfigMaps for Linux","D. Secrets are faster"],ans:1,exp:"Never put a database password in a plain text ConfigMap."},
      {q:"How is data stored inside a standard K8s Secret by default?",opts:["A. AES-256 Encrypted","B. Plain text","C. Base64 Encoded (which is NOT encryption and easily decoded)","D. Hashed"],ans:2,exp:"This is a common gotcha! Base64 is just formatting. Anyone with access to the K8s API can decode it instantly. You must configure 'Encryption at Rest' for true security."},
      {q:"How can a Pod consume a ConfigMap or Secret?",opts:["A. By querying the database","B. By injecting them as Environment Variables (e.g., process.env.DB_PASS), or mounting them as files in a Volume inside the container","C. By sending an email","D. Through a URL parameter"],ans:1,exp:"Environment variables are the most common and easiest method."}
    ],
    flows:[
      {title:"The Config Injection Flow",items:["start:Create ConfigMap (ENV=prod)","proc:Create Secret (DB_PASS=123)","dec:Apply Pod YAML (References both)","proc:Pod boots up","end:Node.js reads process.env.DB_PASS instantly!"]}
    ],
    game:{icon:"🔐",title:"The Vault",desc:"Master K8s configuration",badges:["🔐 Secret Keeper","🗺️ Config Mapper","💉 Environment Injector"],challenges:[{icon:"📝",title:"Base64",desc:"Is Base64 secure encryption?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Inject Env Vars",badge:"Configurator",desc:"Link a ConfigMap to a Pod.",tags:["Kubernetes","YAML"],steps:[{title:"ConfigMap",desc:"Create cm with 'DB_HOST: aws-rds'"},{"title:"Pod Spec",desc:"envFrom: - configMapRef: name: my-config"},{"title:"App",desc:"App connects to aws-rds seamlessly"}],code:`# Example of injecting a Secret into a Pod's environment\napiVersion: v1\nkind: Pod\nmetadata:\n  name: my-app\nspec:\n  containers:\n  - name: node-app\n    image: node-app:v1\n    env:\n      - name: DATABASE_PASSWORD\n        valueFrom:\n          secretKeyRef: \n            name: db-secret # Links to the Secret object\n            key: password`}
  },
  t135: {
    tag:'Phase 4 · DevOps', num:135,
    title:'Helm Charts',
    desc:'The package manager for Kubernetes, enabling templated, reusable deployments.',
    theory:`<div class="card"><h3>📦 The K8s Package Manager</h3><p>If you want to deploy a WordPress site to Kubernetes, you have to write a Deployment YAML, a Service YAML, a ConfigMap YAML, a Secret YAML, and an Ingress YAML. That's 5 complex files. What if you want to deploy it again for a different client?</p><h4>Enter Helm</h4><p><strong>Helm</strong> is like <code>npm</code> or <code>apt</code> but for Kubernetes. A <strong>Helm Chart</strong> bundles all those YAML files together into a single package. It uses variables (templates), so you can deploy a fresh WordPress site with one command: <code>helm install my-blog bitnami/wordpress</code>.</p></div>`,
    mcqs:[
      {q:"What is Helm?",opts:["A. A ship steering wheel","B. The package manager for Kubernetes. It allows you to define, install, and upgrade complex K8s applications using 'Charts'.","C. A container registry","D. A database"],ans:1,exp:"Helm drastically simplifies deploying 3rd party tools (like Redis, Kafka, or WordPress) into your cluster."},
      {q:"What problem does Helm solve regarding K8s YAML files?",opts:["A. It deletes them","B. Pure YAML is static. Helm introduces Templating (variables, if-statements, loops), allowing you to reuse the exact same YAML files for Dev, QA, and Prod just by passing in different values.","C. It converts them to JSON","D. It encrypts them"],ans:1,exp:"Templating is Helm's killer feature."},
      {q:"In a Helm Chart, what is the purpose of the 'values.yaml' file?",opts:["A. It stores passwords securely","B. It acts as the default configuration file where you define all the variables (e.g., replicaCount: 3) that will be injected into the templates","C. It lists dependencies","D. It writes the code"],ans:1,exp:"You can override values.yaml from the command line: helm install --set replicaCount=5."},
      {q:"What command is used to upgrade a running application to a new version using Helm?",opts:["A. helm restart","B. helm upgrade [release-name] [chart]","C. helm deploy","D. kubectl apply"],ans:1,exp:"Helm keeps track of release history, allowing for incredibly easy rollbacks (helm rollback)."},
      {q:"What is a Helm 'Release'?",opts:["A. A software bug","B. A specific, running instance of a Chart deployed to the cluster. You can install the same Chart multiple times, creating multiple Releases.","C. A GitHub tag","D. A deleted chart"],ans:1,exp:"You could install the Redis chart 5 times (5 Releases) for 5 different microservices."}
    ],
    flows:[
      {title:"Helm Templating Flow",items:["start:values.yaml: { replicas: 3 }","proc:deployment.yaml: replicas: {{ .Values.replicas }}","dec:Run: helm install...","proc:Helm Engine injects the '3' into the YAML","end:Sends finalized YAML to K8s API!"]}
    ],
    game:{icon:"📦",title:"The Packager",desc:"Master Helm Charts",badges:["📦 Chart Maker","📝 Templater","🚀 Release Manager"],challenges:[{icon:"📝",title:"values.yaml",desc:"What is its purpose?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Helm Templating",badge:"Templater",desc:"See how Helm injects variables.",tags:["Kubernetes","Helm"],steps:[{title:"Template",desc:"image: '{{ .Values.image.name }}'"},{"title:"Values",desc:"In values.yaml -> image: { name: 'nginx' }"},{"title:"Result",desc:"Helm renders: image: 'nginx'"}],code:`# Example of a Helm Template (deployment.yaml)\n\napiVersion: apps/v1\nkind: Deployment\nspec:\n  # Helm replaces this variable with whatever is in values.yaml!\n  replicas: {{ .Values.replicaCount }}\n  template:\n    spec:\n      containers:\n        - name: my-app\n          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"`}
  },
"""

start_marker = "};\n\nlet userXP"
inject_idx = content.find(start_marker)

if inject_idx != -1:
    new_content = content[:inject_idx] + ",\n" + rich_content + content[inject_idx:]
    with open(html_path, "w") as f:
        f.write(new_content)
    print("Successfully generated T131-T135 rich content!")
else:
    print("Could not find injection point.")
