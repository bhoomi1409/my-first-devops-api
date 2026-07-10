import re

syllabus_text = """
1. Programming Fundamentals

* Variables
* Data Types
* Operators
* Loops
* Conditionals
* Functions
* Scope
* Memory Management
* Stack vs Heap
* Recursion
* Time Complexity
* Space Complexity
* Big O Notation

2. Object-Oriented Programming (OOP)

* Classes
* Objects
* Constructors
* Encapsulation
* Inheritance
* Polymorphism
* Abstraction
* Interfaces
* Abstract Classes
* Method Overloading
* Method Overriding
* Composition vs Inheritance
* SOLID Principles

3. Data Structures

* Arrays
* Strings
* Linked Lists
* Stack
* Queue
* Circular Queue
* Deque
* HashMap
* HashSet
* TreeMap
* Heap
* Priority Queue
* Binary Trees
* BST
* AVL Tree
* Trie
* Graph
* Union Find

4. Algorithms

* Sorting
* Searching
* Binary Search
* DFS
* BFS
* Dynamic Programming
* Greedy Algorithms
* Sliding Window
* Two Pointers
* Backtracking
* Divide and Conquer
* Graph Algorithms
* Dijkstra
* Floyd Warshall
* Topological Sort

5. Java

* JVM
* JDK
* JRE
* Garbage Collection
* Memory Management
* Collections
* Streams API
* Lambda Expressions
* Functional Interfaces
* Optional
* Reflection
* Generics
* Records
* Sealed Classes
* Multithreading
* Synchronization
* Locks
* Executor Service
* CompletableFuture

6. Spring Boot

* Spring Core
* Spring Boot
* Spring MVC
* Spring Data JPA
* Spring Security
* Spring Validation
* Spring Profiles
* Spring Scheduler
* Spring Cache
* Bean Lifecycle
* Dependency Injection
* Auto Configuration
* Actuator

7. Databases

* MySQL
* PostgreSQL
* Oracle
* SQL Server
* CRUD
* Joins
* Group By
* Having
* Window Functions
* Indexes
* Views
* Triggers
* Transactions
* Locks
* Isolation Levels
* ACID
* Normalization
* Denormalization
* MongoDB
* Redis
* Cassandra
* DynamoDB

8. Backend Engineering

* REST APIs
* GraphQL
* gRPC
* CRUD APIs
* Authentication
* Authorization
* JWT
* OAuth2
* Sessions
* Cookies
* API Versioning
* Pagination
* Rate Limiting
* File Upload
* Logging
* Exception Handling

9. Frontend

* Semantic HTML
* Accessibility
* Flexbox
* Grid
* Responsive Design
* Animations
* Closures
* Hoisting
* Promises
* Async Await
* Event Loop
* Fetch API
* Modules
* ES6+
* TypeScript Types
* Interfaces
* Generics
* Utility Types
* React JSX
* Components
* Props
* State
* Hooks
* Context API
* Redux
* React Router
* Forms
* Lazy Loading
* Memoization
* Performance Optimization

10. Version Control

* Git
* GitHub
* GitLab
* Bitbucket
* Branching
* Merge
* Rebase
* Cherry Pick
* Pull Requests
* Merge Conflicts

11. DevOps

* Docker
* Docker Compose
* Kubernetes
* Helm
* Jenkins
* GitHub Actions
* Azure DevOps
* CI/CD
* Nginx

12. Cloud Computing

* AWS
* Azure
* GCP
* EC2
* Lambda
* S3
* RDS
* API Gateway
* IAM
* CloudWatch
* Azure Functions
* Azure Storage

13. Networking

* HTTP
* HTTPS
* TCP
* UDP
* DNS
* CDN
* Proxy
* Reverse Proxy
* VPN
* SSL/TLS
* Load Balancers
* WebSockets
* SSE
* CORS

14. Operating Systems

* Processes
* Threads
* Scheduling
* Deadlock
* Paging
* Virtual Memory
* Synchronization
* Mutex
* Semaphore

15. System Design

* Monolith
* Microservices
* Event Driven Architecture
* Load Balancing
* Caching
* Redis
* CDN
* Message Queues
* Kafka
* RabbitMQ
* Service Discovery
* API Gateway
* Circuit Breaker
* Scalability
* Availability
* CAP Theorem
* Database Sharding
* Replication

16. Design Patterns

* Singleton
* Factory
* Builder
* Strategy
* Observer
* Adapter
* Decorator
* Command
* Repository
* MVC
* CQRS

17. Software Architecture

* Layered Architecture
* Clean Architecture
* Hexagonal Architecture
* Onion Architecture
* Domain Driven Design (DDD)

18. Testing

* Unit Testing
* Integration Testing
* End-to-End Testing
* Mocking
* JUnit
* Mockito
* Cypress
* Playwright
* Postman Testing

19. Security

* OWASP Top 10
* SQL Injection
* XSS
* CSRF
* JWT Security
* Encryption
* Hashing
* HTTPS
* Secrets Management

20. AI/LLM

* AI vs ML vs Deep Learning
* Neural Networks
* Transformers
* Attention Mechanism
* Tokenization
* Embeddings
* Vector Databases
* Semantic Search
* RAG
* MCP
* AI Agents
* Function Calling
* Tool Calling
* Prompt Engineering
* Fine-Tuning
* LoRA
* Quantization
* Hallucinations
* Context Window
* Multi-Agent Systems
* LangChain
* LangGraph
* FastAPI
* Ollama
* vLLM
* Hugging Face
* FAISS
* ChromaDB
* Pinecone
* Milvus

21. Product Engineering

* Product Thinking
* Agile
* Scrum
* Sprint Planning
* User Stories
* Acceptance Criteria
* Wireframing
* PRD (Product Requirements Document)
* BRD (Business Requirements Document)
* TSD (Technical Specification Document)
* HLD (High-Level Design)
* LLD (Low-Level Design)

22. Observability

* Logging
* Monitoring
* Metrics
* Tracing
* Grafana
* Prometheus
* ELK Stack
* OpenTelemetry

23. Performance

* Profiling
* Memory Leaks
* Caching
* Lazy Loading
* Compression
* CDN
* Query Optimization

24. Common Interview Questions

* Explain your project end-to-end
* Why did you choose this tech stack?
* How does a request travel from the browser to the database and back?
* What happens when you type a URL into a browser?
* Explain authentication vs authorization
* How does JWT work?
* Why use Spring Boot instead of plain Spring?
* Why React over Angular?
* What is the Virtual DOM?
* How do you debug production issues?
* How do you optimize a slow API?
* How do you design a scalable notification service?
* How would you build a URL shortener chat app or file storage system?
"""

phases = {
    1: "Phase 1: Core Foundations",
    2: "Phase 1: Core Foundations",
    3: "Phase 1: Core Foundations",
    4: "Phase 1: Core Foundations",
    14: "Phase 1: Core Foundations",
    13: "Phase 1: Core Foundations",
    5: "Phase 2: Backend & Data",
    6: "Phase 2: Backend & Data",
    7: "Phase 2: Backend & Data",
    8: "Phase 2: Backend & Data",
    19: "Phase 2: Backend & Data",
    23: "Phase 2: Backend & Data",
    9: "Phase 3: Frontend & Product",
    21: "Phase 3: Frontend & Product",
    10: "Phase 3: Frontend & Product",
    18: "Phase 3: Frontend & Product",
    11: "Phase 4: Architecture & Cloud",
    12: "Phase 4: Architecture & Cloud",
    15: "Phase 4: Architecture & Cloud",
    16: "Phase 4: Architecture & Cloud",
    17: "Phase 4: Architecture & Cloud",
    22: "Phase 4: Architecture & Cloud",
    20: "Phase 5: AI & Interviews",
    24: "Phase 5: AI & Interviews"
}

category_names = {
    1: "Programming Fundamentals",
    2: "OOP",
    3: "Data Structures",
    4: "Algorithms",
    5: "Java",
    6: "Spring Boot",
    7: "Databases",
    8: "Backend",
    9: "Frontend",
    10: "Version Control",
    11: "DevOps",
    12: "Cloud",
    13: "Networking",
    14: "Operating Systems",
    15: "System Design",
    16: "Design Patterns",
    17: "Architecture",
    18: "Testing",
    19: "Security",
    20: "AI/LLM",
    21: "Product Eng",
    22: "Observability",
    23: "Performance",
    24: "Interviews"
}


nav_entries = ["  {id:'welcome',num:'🏠',title:'Syllabus Overview',part:''},"]
topic_idx = 1
current_category = None
current_phase = ""
cat_name = ""

for line in syllabus_text.strip().split('\n'):
    line = line.strip()
    if not line:
        continue
    
    # Check if category header
    m = re.match(r'^(\d+)\.\s+(.*)$', line)
    if m:
        cat_id = int(m.group(1))
        current_category = cat_id
        current_phase = phases.get(cat_id, "Unknown Phase")
        cat_name = category_names.get(cat_id, m.group(2))
        continue
    
    # Check if bullet point
    if line.startswith('* '):
        topic_title = line[2:].strip().replace("'", "\\'")
        # Include category prefix to make it clear (e.g. OOP: Classes)
        title = f"{cat_name}: {topic_title}"
        nav_entries.append(f"  {{id:'t{topic_idx}',num:{topic_idx},title:'{title}',part:'{current_phase}'}},")
        topic_idx += 1

all_nav_str = "const ALL_NAV = [\n" + "\n".join(nav_entries)[:-1] + "\n];"

html_path = "/Users/bhoomim/devops CI:CD/handbook/fullstack_ai_handbook.html"
with open(html_path, "r") as f:
    content = f.read()

# Replace the ALL_NAV block
start_marker = "const ALL_NAV = ["
end_marker = "];\n\nconst RICH_TOPICS = {"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker) + 2

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + all_nav_str + content[end_idx:]
    with open(html_path, "w") as f:
        f.write(new_content)
    print(f"Successfully generated {topic_idx-1} topics!")
else:
    print("Could not find ALL_NAV block.")
