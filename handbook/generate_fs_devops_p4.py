import re

html_path = "/Users/bhoomim/devops CI:CD/handbook/fullstack_ai_handbook.html"
with open(html_path, "r") as f:
    content = f.read()

rich_content = r"""
  t136: {
    tag:'Phase 4 · Cloud', num:136,
    title:'AWS Core Services',
    desc:'The holy trinity of Amazon Web Services: Compute, Storage, and Databases.',
    theory:`<div class="card"><h3>☁️ The Cloud Giants</h3><p>In the 2000s, companies bought physical servers for $10,000. It took weeks to ship and install. <strong>AWS (Amazon Web Services)</strong> revolutionized this by renting servers by the second (Cloud Computing).</p><h4>The Big Three</h4><ul><li><strong>EC2 (Elastic Compute Cloud):</strong> Virtual Machines. You rent a Linux or Windows server, SSH into it, and install whatever you want. This is raw compute power.</li><li><strong>S3 (Simple Storage Service):</strong> Object Storage. A limitless hard drive in the cloud for files (images, videos, backups). Not for OS files.</li><li><strong>RDS (Relational Database Service):</strong> Managed SQL databases (Postgres, MySQL). AWS handles the backups, patches, and failovers automatically.</li></ul></div>`,
    mcqs:[
      {q:"What does AWS EC2 provide?",opts:["A. A managed database","B. Virtual Machines (Servers) that you can rent by the second to run your applications. You have full OS access.","C. Cloud storage for images","D. A domain name"],ans:1,exp:"EC2 instances are the workhorses of the internet."},
      {q:"If you are building an Instagram clone and users upload millions of photos, which AWS service is best suited to store those image files?",opts:["A. EC2","B. RDS","C. Amazon S3 (Simple Storage Service)","D. Amazon VPC"],ans:2,exp:"S3 is incredibly cheap, infinitely scalable object storage. Never store images on an EC2 instance's local hard drive."},
      {q:"What is the primary benefit of using Amazon RDS over installing PostgreSQL yourself on an EC2 instance?",opts:["A. RDS is free","B. RDS is a 'Managed Service'. AWS automatically handles OS patching, database backups, replication, and disaster recovery.","C. RDS is NoSQL","D. RDS runs locally"],ans:1,exp:"While you could host it yourself, the administrative overhead is usually not worth the cost savings."},
      {q:"What does 'Elastic' mean in the context of Cloud Computing (like EC2)?",opts:["A. It uses rubber bands","B. The ability of the infrastructure to automatically scale UP (add servers) when traffic spikes, and scale DOWN (remove servers) when traffic drops to save money","C. The database is flexible","D. The code is Javascript"],ans:1,exp:"This completely eliminated the need for companies to buy massive servers 'just in case' they had a busy Black Friday."},
      {q:"Which AWS service acts as a Content Delivery Network (CDN), caching your S3 images and Next.js HTML on edge servers globally?",opts:["A. AWS CloudFront","B. AWS Lambda","C. Amazon RDS","D. Amazon Route 53"],ans:0,exp:"CloudFront ensures a user in Tokyo downloads your image from a Tokyo server, not a New York server."}
    ],
    flows:[
      {title:"AWS Web Architecture",items:["start:User visits site (Route 53 DNS)","proc:Request hits CloudFront (CDN)","dec:CloudFront hits Application Load Balancer","proc:ALB routes to EC2 instance (Node.js)","end:EC2 queries RDS (Database) and fetches image from S3!"]}
    ],
    game:{icon:"☁️",title:"The Cloud Native",desc:"Master core AWS services",badges:["☁️ Compute Renter","🪣 S3 Bucket Master","🗃️ Managed DB User"],challenges:[{icon:"📝",title:"S3 vs EC2",desc:"Where do you store a 1GB video?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"AWS Mind Map",badge:"Architect",desc:"Map out the Holy Trinity.",tags:["AWS","Concepts"],steps:[{title:"Compute",desc:"EC2: Running the Spring Boot or Node API"},{"title:"Database",desc:"RDS: Storing user credentials and orders"},{"title:"Storage",desc:"S3: Storing profile pictures and static assets"}],code:`// Mental mapping for AWS Services
// EC2  = Your Computer's CPU / RAM
// S3   = An infinite, cheap USB Flash Drive
// RDS  = A highly secure, managed SQL Database
// EBS  = The actual 'C: Drive' attached to your EC2 VM`}
  },
  t137: {
    tag:'Phase 4 · Cloud', num:137,
    title:'VPC & Subnets',
    desc:'Virtual Private Cloud: The fundamental networking and security layer of AWS.',
    theory:`<div class="card"><h3>🏰 The Moat and the Castle</h3><p>If you put your Database on the public internet, it WILL be hacked in minutes. A <strong>VPC (Virtual Private Cloud)</strong> is your private, isolated slice of AWS.</p><h4>Subnets</h4><p>You divide your VPC into <strong>Subnets</strong> (sub-networks).</p><ul><li><strong>Public Subnet:</strong> Has a route to the Internet Gateway. Your Load Balancers and Bastion Hosts go here.</li><li><strong>Private Subnet:</strong> NO direct access from the internet. Your Backend APIs and Databases MUST go here. They can only be accessed by the Load Balancer in the Public Subnet.</li></ul></div>`,
    mcqs:[
      {q:"What is an Amazon VPC?",opts:["A. A database","B. A logically isolated, private virtual network in the AWS cloud where you launch your resources (EC2, RDS) securely","C. A content delivery network","D. A programming language"],ans:1,exp:"Without a VPC, all your servers would be sitting exposed on the public internet."},
      {q:"What is the fundamental difference between a Public Subnet and a Private Subnet?",opts:["A. Public is free, Private costs money","B. A Public Subnet has a Route Table entry pointing to an Internet Gateway (IGW), allowing incoming/outgoing internet traffic. A Private Subnet does not.","C. Public is for Linux, Private is for Windows","D. Public is faster"],ans:1,exp:"This is the most critical concept in cloud security."},
      {q:"Where should you place your Amazon RDS Database in a VPC?",opts:["A. In a Public Subnet so you can access it easily","B. In a Private Subnet. Databases should NEVER have public IP addresses or be accessible from the internet.","C. Outside the VPC","D. In an S3 Bucket"],ans:1,exp:"Only your backend API servers (also in a private subnet) should be allowed to talk to the database."},
      {q:"If your backend API is in a Private Subnet (no internet access), how can it download a software update or make a Stripe API call?",opts:["A. It cannot","B. By routing its outbound traffic through a NAT Gateway (Network Address Translation) placed in the Public Subnet","C. By using a VPN","D. By using an IAM Role"],ans:1,exp:"A NAT Gateway allows servers in a private subnet to reach out to the internet, but prevents the internet from reaching in."},
      {q:"What acts as a virtual firewall for your EC2 instances, controlling exact inbound and outbound traffic at the instance level?",opts:["A. VPC","B. Security Groups (e.g., Allow Inbound Port 80, Deny Port 22)","C. Route 53","D. IAM"],ans:1,exp:"Security Groups are stateful firewalls applied directly to the VM."}
    ],
    flows:[
      {title:"VPC Architecture Flow",items:["start:Hacker tries to hit Database IP directly","proc:Request hits VPC perimeter","dec:Database is in Private Subnet (No Internet Route!)","proc:Request DROPPED. DB is safe.","end:Only the Load Balancer (Public) can talk to the DB (Private)."]}
    ],
    game:{icon:"🏰",title:"The Warden",desc:"Master Cloud Security",badges:["🏰 VPC Architect","🔒 Subnet Isolator","🛡️ Firewall Admin"],challenges:[{icon:"📝",title:"Private Subnet",desc:"How does it access the internet?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Network Design",badge:"Securer",desc:"Mentally place resources in subnets.",tags:["AWS","VPC"],steps:[{title:"Public Subnet",desc:"Contains: Application Load Balancer, NAT Gateway"},{"title:"Private Subnet (App)",desc:"Contains: Node.js EC2 instances"},{"title:"Private Subnet (Data)",desc:"Contains: RDS Postgres, ElastiCache Redis"}],code:`// Secure Cloud Architecture Rule #1:
// NEVER PUT A DATABASE ON A PUBLIC SUBNET.
// 
// Only the Load Balancer should be public. 
// It accepts HTTPS traffic from users and forwards it 
// safely to the internal Private Subnet servers.`}
  },
  t138: {
    tag:'Phase 4 · Cloud', num:138,
    title:'IAM Roles & Policies',
    desc:'Identity and Access Management: Securely controlling who and what can access your AWS resources.',
    theory:`<div class="card"><h3>🔑 The Bouncer</h3><p>By default, everything in AWS is locked down. An EC2 server cannot read an S3 bucket unless you explicitly grant it permission.</p><h4>IAM Concepts</h4><ul><li><strong>Users:</strong> Actual humans logging into the AWS Console.</li><li><strong>Policies:</strong> JSON documents that define exactly what actions are allowed (e.g., <code>"Action": "s3:GetObject"</code>).</li><li><strong>Roles:</strong> Temporary hats that AWS Services (like EC2 or Lambda) can wear. You attach a Policy to a Role, and give the Role to an EC2 instance. Now the instance has permission to read the bucket without hardcoding any passwords!</li></ul></div>`,
    mcqs:[
      {q:"What is AWS IAM?",opts:["A. Internet Access Manager","B. Identity and Access Management. The service that controls authentication (who is this?) and authorization (what can they do?) across all of AWS.","C. An AI service","D. A database"],ans:1,exp:"IAM is the core security foundation of AWS."},
      {q:"What is the Principle of Least Privilege?",opts:["A. Giving everyone admin access to save time","B. Granting an entity (User or Role) the absolute minimum permissions necessary to perform its job, and nothing more.","C. Restricting database size","D. Denying all access"],ans:1,exp:"If an app only needs to READ from S3, do not give it WRITE access. If it is hacked, the hacker can't delete your files."},
      {q:"If your Node.js app running on an EC2 instance needs to download a file from an S3 bucket, what is the MOST SECURE way to grant it permission?",opts:["A. Hardcode your AWS Admin Username and Password in the Node.js code","B. Create an IAM Role with a policy allowing 's3:GetObject', and attach that Role to the EC2 instance. The AWS SDK handles the rest automatically.","C. Make the S3 bucket public to the whole world","D. Email AWS support"],ans:1,exp:"Never hardcode credentials (Access Keys) on a server. Roles provide temporary, auto-rotating credentials safely."},
      {q:"What format are IAM Policies written in?",opts:["A. XML","B. JSON (JavaScript Object Notation)","C. YAML","D. CSV"],ans:1,exp:"A policy contains 'Effect' (Allow/Deny), 'Action' (s3:PutObject), and 'Resource' (arn:aws:s3:::my-bucket)."},
      {q:"What is an IAM User's 'Access Key ID' and 'Secret Access Key'?",opts:["A. Website passwords","B. Long cryptographic strings used for programmatic access (e.g., using the AWS CLI or SDKs) instead of a username/password.","C. Database keys","D. SSH keys"],ans:1,exp:"The Secret Key is only shown to you once. If you lose it, you must generate a new one. Treat it like a credit card number."}
    ],
    flows:[
      {title:"IAM Role Assumption",items:["start:EC2 Server boots up","proc:Assumes IAM Role 'S3-Reader-Role'","proc:AWS Security Token Service (STS) grants temporary credentials","dec:App tries to upload (PUT) to S3","end:DENIED! Policy only allows GET. Least Privilege!"]}
    ],
    game:{icon:"🔑",title:"The Keymaster",desc:"Master IAM security",badges:["🔑 Policy Writer","🎩 Role Assumer","🛡️ Least Privilege"],challenges:[{icon:"📝",title:"Hardcoding Keys",desc:"Why is it a fatal mistake?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"JSON Policy",badge:"Bouncer",desc:"Write a basic IAM Policy.",tags:["AWS","Security"],steps:[{title:"Effect",desc:"'Effect': 'Allow'"},{"title:"Action",desc:"'Action': ['s3:GetObject']"},{"title:"Resource",desc:"'Resource': 'arn:aws:s3:::my-images/*'"}],code:`{\n  "Version": "2012-10-17",\n  "Statement": [\n    {\n      "Effect": "Allow",\n      "Action": "s3:GetObject",\n      "Resource": "arn:aws:s3:::my-bucket-name/*"\n    }\n  ]\n}\n// Attach this to a Role, give the Role to EC2.\n// Now the EC2 can ONLY read from this specific bucket.`}
  },
  t139: {
    tag:'Phase 4 · Cloud', num:139,
    title:'Infrastructure as Code (Terraform)',
    desc:'Automating the creation of cloud infrastructure using code instead of clicking through a UI.',
    theory:`<div class="card"><h3>🏗️ The Code Architect</h3><p>Clicking through the AWS Console to manually create a VPC, 5 Subnets, an RDS database, and 10 EC2 instances takes hours. If you make a mistake, you're doomed. What if you need to replicate it for a QA environment?</p><h4>Infrastructure as Code (IaC)</h4><p>With <strong>Terraform</strong>, you write your infrastructure in code (HCL syntax). You declare: "I want an AWS EC2 instance of type t2.micro". When you run <code>terraform apply</code>, Terraform talks to the AWS API and builds it for you. You can commit this code to GitHub! If disaster strikes, you can rebuild your entire datacenter in 5 minutes.</p></div>`,
    mcqs:[
      {q:"What is Infrastructure as Code (IaC)?",opts:["A. Writing HTML for a server","B. The practice of managing and provisioning computing infrastructure (servers, networks, databases) through machine-readable configuration files (code), rather than physical hardware configuration or interactive configuration tools.","C. Compiling Java to machine code","D. Using Docker"],ans:1,exp:"IaC applies Software Engineering principles (version control, CI/CD, testing) to physical infrastructure."},
      {q:"Why is Terraform so widely used compared to AWS CloudFormation?",opts:["A. It is owned by AWS","B. It is Cloud Agnostic. You can use Terraform to provision resources on AWS, Google Cloud, Azure, and even Kubernetes, all using the same HCL syntax.","C. It is faster","D. It runs in the browser"],ans:1,exp:"CloudFormation ONLY works on AWS. Terraform works everywhere."},
      {q:"What does it mean that Terraform is 'Declarative'?",opts:["A. You have to write 'IF' statements to check if the server exists","B. You declare the DESIRED END STATE (e.g., 'I want 5 servers'). Terraform automatically figures out the steps to achieve that state (e.g., 'Only 3 exist, I will create 2 more').","C. It talks out loud","D. It requires manual input"],ans:1,exp:"Imperative code says HOW to do it. Declarative code says WHAT you want."},
      {q:"What is the Terraform 'State' file?",opts:["A. A log of errors","B. A critical JSON file (terraform.tfstate) that Terraform uses to map the resources it created in the real world to the code you wrote. It is the single source of truth.","C. A database table","D. A Docker image"],ans:1,exp:"Never lose your state file! Teams usually store it securely in an S3 bucket with versioning enabled."},
      {q:"Which command actually provisions/creates the resources in the cloud provider?",opts:["A. terraform init","B. terraform plan","C. terraform apply","D. terraform build"],ans:2,exp:"'plan' shows you what it WILL do. 'apply' actually DOES it."}
    ],
    flows:[
      {title:"The Terraform Lifecycle",items:["start:Write main.tf (Desire: 2 EC2 Instances)","proc:Run 'terraform plan' (Diff: +2 to add)","dec:Run 'terraform apply'","proc:Terraform API calls AWS -> Creates VMs","end:Saves mapping to 'terraform.tfstate' file"]}
    ],
    game:{icon:"🏗️",title:"The Provisioner",desc:"Master Infrastructure as Code",badges:["🏗️ Builder","📜 Declarative Thinker","☁️ Cloud Agnostic"],challenges:[{icon:"📝",title:"Declarative",desc:"What does Declarative mean?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"HCL Syntax",badge:"Scripter",desc:"Read HashiCorp Configuration Language.",tags:["DevOps","Terraform"],steps:[{title:"Provider",desc:"provider 'aws' { region = 'us-east-1' }"},{"title:"Resource",desc:"resource 'aws_instance' 'web' { ... }"},{"title:"AMI",desc:"ami = 'ami-0abcd' (The OS image)"}],code:`# Terraform HCL Syntax Example\n\nprovider "aws" {\n  region = "us-east-1"\n}\n\n# Create a single EC2 Virtual Machine\nresource "aws_instance" "my_web_server" {\n  ami           = "ami-0c55b159cbfafe1f0" # Ubuntu Linux\n  instance_type = "t2.micro"\n\n  tags = {\n    Name = "HelloWorldServer"\n  }\n}\n\n# Run \`terraform apply\` and this server is created instantly!`}
  },
  t140: {
    tag:'Phase 4 · Cloud', num:140,
    title:'Serverless (AWS Lambda)',
    desc:'Running code without provisioning or managing servers.',
    theory:`<div class="card"><h3>⚡ Function as a Service</h3><p>If you run a Node.js API on an EC2 server, you pay for that server 24/7, even if nobody visits your site at 3 AM. You also have to patch the OS and scale it.</p><h4>AWS Lambda (Serverless)</h4><p>With <strong>Serverless</strong> architecture, you just upload your JavaScript function to AWS. AWS completely manages the infrastructure. <br>If an HTTP request comes in, AWS instantly spins up your function, runs it, and kills it. <strong>You only pay for the exact milliseconds your code was executing.</strong> If nobody visits at 3 AM, you pay $0.00.</p></div>`,
    mcqs:[
      {q:"What is the primary financial advantage of Serverless computing (like AWS Lambda) over EC2 servers?",opts:["A. It is entirely free","B. You pay purely for execution time (milliseconds). If your code is not actively running, you pay $0.00. EC2 charges you 24/7 regardless of traffic.","C. It uses less electricity","D. It mines cryptocurrency"],ans:1,exp:"This 'Pay-as-you-go' model is revolutionary for startups with unpredictable traffic."},
      {q:"Does 'Serverless' actually mean there are no servers involved?",opts:["A. Yes, it runs on magic","B. No, the code still runs on physical servers in an AWS datacenter. It just means YOU (the developer) don't have to provision, patch, or manage those servers.","C. It runs on the user's phone","D. It runs on a satellite"],ans:1,exp:"Serverless abstracts the infrastructure away completely."},
      {q:"What is a 'Cold Start' in AWS Lambda?",opts:["A. When the datacenter gets too cold","B. The latency/delay (e.g., 1-2 seconds) experienced on the very first request to a function because AWS has to boot up a fresh container and load your code into memory","C. A database error","D. A reboot process"],ans:1,exp:"After the cold start, subsequent requests are 'Warm' and execute instantly (until the container scales down after inactivity)."},
      {q:"How does AWS Lambda handle a sudden spike from 10 users to 10,000 users?",opts:["A. It crashes","B. It queues the requests","C. It automatically and instantly scales out, spinning up 10,000 parallel instances of your function to handle the requests simultaneously","D. It ignores them"],ans:2,exp:"Lambda handles horizontal scaling completely automatically without any load balancers or configuration."},
      {q:"Which AWS service is typically paired with Lambda to provide HTTP REST API endpoints that trigger the functions?",opts:["A. Amazon S3","B. Amazon API Gateway","C. AWS IAM","D. Amazon RDS"],ans:1,exp:"API Gateway receives the HTTP request and triggers the Lambda function."}
    ],
    flows:[
      {title:"The Serverless Flow",items:["start:User hits 'api.myapp.com/upload'","proc:API Gateway receives HTTP Request","proc:API Gateway triggers Lambda Function","dec:Lambda spins up (Cold Start) -> Processes image","end:Lambda saves to S3 -> Lambda terminates. Billed: 200ms."]}
    ],
    game:{icon:"⚡",title:"The Minimalist",desc:"Master Serverless concepts",badges:["⚡ Function Writer","🥶 Cold Starter","💰 Penny Pincher"],challenges:[{icon:"📝",title:"Scaling",desc:"How does Lambda handle 10k users?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"A Simple Lambda",badge:"FaaS",desc:"Understand the Lambda handler structure.",tags:["AWS","Serverless"],steps:[{title:"Handler",desc:"exports.handler = async (event) => {}"},{"title:"Event",desc:"The event object contains the HTTP request data"},{"title:"Return",desc:"Return a status code and JSON body"}],code:`// A standard Node.js AWS Lambda Function\n// No Express.js, no port listening. Just a pure function.\n\nexports.handler = async (event) => {\n  // Extract data from the incoming HTTP request\n  const name = event.queryStringParameters.name || 'World';\n\n  // Return an HTTP response object\n  return {\n    statusCode: 200,\n    body: JSON.stringify(` + "`Hello, ${name}!`" + `),\n  };\n};`}
  }
"""

start_marker = "};\n\nlet userXP"
inject_idx = content.find(start_marker)

if inject_idx != -1:
    new_content = content[:inject_idx] + ",\n" + rich_content + content[inject_idx:]
    with open(html_path, "w") as f:
        f.write(new_content)
    print("Successfully generated T136-T140 rich content!")
else:
    print("Could not find injection point.")
