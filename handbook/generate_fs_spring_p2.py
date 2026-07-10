import re

html_path = "/Users/bhoomim/devops CI:CD/handbook/fullstack_ai_handbook.html"
with open(html_path, "r") as f:
    content = f.read()

rich_content = r"""
  t78: {
    tag:'Phase 2 · Backend (Spring)', num:78,
    title:'RESTful API Principles',
    desc:'Representational State Transfer: The standard architectural style for web APIs.',
    theory:`<div class="card"><h3>🌐 The API Standard</h3><p><strong>REST (Representational State Transfer)</strong> is a set of rules for building web APIs. It relies on standard HTTP methods to perform CRUD (Create, Read, Update, Delete) operations on <strong>Resources</strong>.</p><h4>The Core Rules</h4><ol><li><strong>Stateless:</strong> The server remembers NOTHING between requests. Every single request from the client must contain all the information (like an Auth token) needed to process it.</li><li><strong>Resource-Based URLs:</strong> URLs should represent <em>nouns</em> (things), not verbs (actions).<ul><li>Good: <code>GET /users</code>, <code>POST /users</code></li><li>Bad: <code>GET /getAllUsers</code>, <code>POST /createNewUser</code></li></ul></li><li><strong>Use standard HTTP Methods:</strong> GET (Read), POST (Create), PUT (Update full), PATCH (Update partial), DELETE.</li></ol></div>`,
    mcqs:[
      {q:"What does it mean for a REST API to be 'Stateless'?",opts:["A. The API has no database","B. The server does not store any client context/session between requests; every request must contain all necessary authentication and data","C. The client does not exist","D. The API cannot return errors"],ans:1,exp:"Statelessness makes APIs incredibly easy to scale horizontally. You can bounce a user's request between 5 different servers and it still works."},
      {q:"According to REST principles, what is the correct URL to fetch a specific user with ID 5?",opts:["A. GET /getUser?id=5","B. POST /users/5","C. GET /users/5","D. GET /users/get/5"],ans:2,exp:"URLs should be clean nouns representing the resource hierarchy."},
      {q:"Which HTTP method is traditionally used to completely REPLACE an existing resource?",opts:["A. POST","B. GET","C. PUT","D. PATCH"],ans:2,exp:"POST creates new. PUT replaces. PATCH partially updates. DELETE removes."},
      {q:"What format is most commonly used to transfer data in a modern REST API?",opts:["A. XML","B. JSON (JavaScript Object Notation)","C. HTML","D. CSV"],ans:1,exp:"JSON is lightweight, readable, and native to JavaScript, making it the industry standard."},
      {q:"If a client requests a resource that does not exist, what HTTP Status Code should the REST API return?",opts:["A. 200 OK","B. 500 Internal Server Error","C. 404 Not Found","D. 401 Unauthorized"],ans:2,exp:"Using standard HTTP status codes is a core requirement of a good REST API."}
    ],
    flows:[
      {title:"CRUD HTTP Mapping",items:["start:Resource: '/books'","proc:Create: POST /books","proc:Read All: GET /books","proc:Read One: GET /books/1","dec:Update: PUT /books/1","end:Delete: DELETE /books/1"]}
    ],
    game:{icon:"🌐",title:"The REST API",desc:"Master standard web protocols",badges:["🌐 Standardizer","📇 Noun User","🛑 Stateless Purist"],challenges:[{icon:"📝",title:"Bad URLs",desc:"Why is /deleteUser bad?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"RESTful Controller",badge:"API Designer",desc:"Design a proper REST controller in Spring.",tags:["Spring","REST"],steps:[{title:"Base Route",desc:"Add @RequestMapping('/api/users') to class"},{"title:"GET All",desc:"@GetMapping for all users"},{"title:"GET One",desc:"@GetMapping('/{id}') using @PathVariable"}],code:`@RestController\n@RequestMapping("/api/users") // Base Noun\npublic class UserController {\n\n  @GetMapping // Inherits "/api/users"\n  public List<User> getAll() { ... }\n\n  @PostMapping\n  public User create(@RequestBody User u) { ... }\n\n  @GetMapping("/{id}")\n  public User getOne(@PathVariable int id) { ... }\n}`}
  },
  t79: {
    tag:'Phase 2 · Backend (Spring)', num:79,
    title:'JPA & Hibernate',
    desc:'Java Persistence API: Bridging the gap between Object-Oriented Java and Relational SQL Databases.',
    theory:`<div class="card"><h3>🌉 The ORM Bridge</h3><p>Java is an Object-Oriented language (Classes, Objects, Inheritance). SQL databases are Relational (Tables, Rows, Foreign Keys). They speak completely different languages. This is called the <em>Object-Relational Impedance Mismatch</em>.</p><h4>Object-Relational Mapping (ORM)</h4><p>An ORM tool translates Java Objects into SQL queries automatically. You just say <code>database.save(userObject)</code>, and the ORM generates the massive <code>INSERT INTO users (name, email) VALUES (...)</code> SQL string for you!</p><ul><li><strong>JPA (Java Persistence API):</strong> The theoretical specification (the rulebook). It is just an interface.</li><li><strong>Hibernate:</strong> The most popular actual implementation of JPA. It does the heavy lifting of generating the SQL.</li></ul></div>`,
    mcqs:[
      {q:"What is the primary purpose of an ORM (Object-Relational Mapper)?",opts:["A. To make SQL run faster","B. To automatically map Object-Oriented code (Classes/Objects) to Relational Database structures (Tables/Rows), writing the SQL for you","C. To encrypt the database","D. To host the website"],ans:1,exp:"ORMs save developers from writing thousands of lines of repetitive boilerplate SQL code."},
      {q:"What is the relationship between JPA and Hibernate?",opts:["A. They are competitors","B. JPA is the interface/specification (the rules), Hibernate is the concrete implementation (the actual code that does the work)","C. Hibernate is for Java, JPA is for Python","D. They are both databases"],ans:1,exp:"You write your code against the JPA standard. Under the hood, Hibernate executes it."},
      {q:"What is the 'Impedance Mismatch' that ORMs solve?",opts:["A. Different server voltages","B. The fundamental difference in how data is represented in Java (Objects, Inheritance, Collections) vs SQL Databases (Tables, Rows, Foreign Keys)","C. Network latency","D. Different Java versions"],ans:1,exp:"Translating a Java List<Address> into SQL requires complex Join tables. Hibernate handles this translation automatically."},
      {q:"Does using an ORM mean you don't need to know SQL?",opts:["A. Yes, never learn SQL","B. No. While ORMs handle 90% of simple queries, you must know SQL to optimize complex queries, fix N+1 performance bugs, and understand what the ORM is actually doing to your database","C. Yes, SQL is dead","D. Only if you use NoSQL"],ans:1,exp:"A bad Hibernate mapping can accidentally generate thousands of SQL queries for a simple page load (The N+1 problem)."},
      {q:"What is a major advantage of using JPA/Hibernate over raw JDBC (Java Database Connectivity)?",opts:["A. It is faster","B. Database Agnosticism: You can switch from MySQL to PostgreSQL just by changing a config file; Hibernate will automatically translate your Java code into the correct SQL dialect for the new DB","C. It uses less memory","D. It works offline"],ans:1,exp:"Raw SQL is often database-specific. Hibernate's HQL is database-agnostic."}
    ],
    flows:[
      {title:"The ORM Translation",items:["start:Java: save(new User('Bhoomi'))","proc:JPA Interface receives call","proc:Hibernate analyzes User class annotations","dec:Hibernate generates SQL string","end:Executes: INSERT INTO users VALUES ('Bhoomi')"]}
    ],
    game:{icon:"🌉",title:"The Bridge Builder",desc:"Master object-relational mapping",badges:["🌉 Impedance Matcher","🗃️ ORM Wizard","🗺️ Dialect Agnostic"],challenges:[{icon:"📝",title:"JPA vs Hibernate",desc:"Explain the relationship",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"ORM Concept",badge:"Translator",desc:"Understand how an object maps to a table.",tags:["Database","ORM"],steps:[{title:"Java Object",desc:"User object with fields: id, name, email"},{"title:"SQL Table",desc:"Table 'users' with columns: id, name, email"},{"title:"The Magic",desc:"ORM maps the fields to columns automatically"}],code:`// Mentally translate this Java to SQL:\n\nUser u = new User();\nu.setName("Bhoomi");\nu.setEmail("bhoomi@test.com");\n\n// Calling repository.save(u) triggers Hibernate to write:\n// INSERT INTO users (name, email) \n// VALUES ('Bhoomi', 'bhoomi@test.com');`}
  },
  t80: {
    tag:'Phase 2 · Backend (Spring)', num:80,
    title:'Entity Mapping',
    desc:'Using JPA annotations to define exactly how a Java Class translates into a Database Table.',
    theory:`<div class="card"><h3>🗺️ The Blueprint</h3><p>To tell Hibernate how to map a Java class to a Database table, you use <strong>JPA Annotations</strong> on your class (called an <strong>Entity</strong>).</p><h4>Core Annotations</h4><ul><li><code>@Entity</code>: Marks the class as a database entity.</li><li><code>@Table(name="users")</code>: (Optional) Specifies the exact table name.</li><li><code>@Id</code>: Marks the primary key field.</li><li><code>@GeneratedValue</code>: Tells the database to auto-increment the ID.</li><li><code>@Column</code>: Maps a specific field to a column name or enforces rules (e.g., <code>nullable=false</code>).</li></ul><div class="box b-am"><h5>Relationships</h5><p>You can also map Foreign Keys using <code>@OneToOne</code>, <code>@OneToMany</code>, and <code>@ManyToMany</code> annotations.</p></div></div>`,
    mcqs:[
      {q:"Which annotation is strictly REQUIRED to mark a Java class as something that should be mapped to a database table?",opts:["A. @Table","B. @Entity","C. @Database","D. @Record"],ans:1,exp:"@Entity tells the JPA scanner that this class represents a data model."},
      {q:"What does the @Id annotation do?",opts:["A. Generates a random number","B. Marks the field as the Primary Key for the database table","C. Creates an index","D. Validates identity"],ans:1,exp:"Every Entity MUST have exactly one @Id field to uniquely identify the row."},
      {q:"If you want the database to automatically generate and increment the ID for new rows, what do you use?",opts:["A. @AutoID","B. @GeneratedValue(strategy = GenerationType.IDENTITY)","C. @Increment","D. @Sequence"],ans:1,exp:"This delegates the ID generation to the underlying database (like MySQL's AUTO_INCREMENT)."},
      {q:"If you have a User class, but you want it to map to a table named 'tbl_users' instead of 'user', how do you do it?",opts:["A. Rename the Java class","B. Add @Table(name = 'tbl_users') above the class","C. Use @Column","D. You cannot change it"],ans:1,exp:"@Table gives you granular control over the table properties without having to rename your Java objects."},
      {q:"What annotation would you use if a 'User' can write multiple 'Posts'?",opts:["A. @OneToOne","B. @ManyToOne","C. @OneToMany","D. @ManyToMany"],ans:2,exp:"From the perspective of the User class, One user has Many posts."}
    ],
    flows:[
      {title:"Entity Mapping Flow",items:["start:@Entity class User","proc:@Id private Long id; -> PRIMARY KEY","proc:@Column(unique=true) String email; -> UNIQUE","dec:Hibernate reads annotations on boot","end:Hibernate runs 'CREATE TABLE' SQL!"]}
    ],
    game:{icon:"🗺️",title:"The Cartographer",desc:"Master JPA metadata",badges:["🗺️ Mapper","🔑 Primary Key","🔗 Relator"],challenges:[{icon:"📝",title:"Relationships",desc:"Name the 4 relationship annotations",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Create an Entity",badge:"Database Designer",desc:"Write a complete JPA Entity class.",tags:["Spring","JPA"],steps:[{title:"Class",desc:"Add @Entity"},{"title:"ID",desc:"Add @Id and @GeneratedValue to a Long id"},{"title:"Fields",desc:"Add a String username"}],code:`import jakarta.persistence.*;\n\n@Entity\n@Table(name = "players") // Optional override\npublic class Player {\n\n  @Id\n  @GeneratedValue(strategy = GenerationType.IDENTITY)\n  private Long id;\n\n  @Column(nullable = false, unique = true)\n  private String username;\n  \n  // Getters and Setters omitted for brevity\n}`}
  },
  t81: {
    tag:'Phase 2 · Backend (Spring)', num:81,
    title:'Spring Data JPA',
    desc:'A Spring module that magically generates database repositories and SQL queries for you.',
    theory:`<div class="card"><h3>✨ The Magic Repositories</h3><p>Historically, even with Hibernate, you had to write a lot of boilerplate Java code to open database sessions, begin transactions, and save objects. <strong>Spring Data JPA</strong> eliminates 99% of this code.</p><h4>The JpaRepository Interface</h4><p>You simply create an interface that extends <code>JpaRepository&lt;EntityClass, IdType&gt;</code>. You don't write <em>any</em> implementation code. Spring automatically generates a class at runtime that provides standard CRUD methods (<code>save()</code>, <code>findAll()</code>, <code>findById()</code>, <code>delete()</code>).</p><h4>Query Derivation</h4><p>If you need a custom query, you just name the method using a specific syntax, like <code>findByEmail(String email)</code>. Spring will literally parse the name of your method and generate the SQL automatically!</p></div>`,
    mcqs:[
      {q:"What is the primary benefit of Spring Data JPA?",opts:["A. It replaces the database","B. It provides a massive reduction in boilerplate code by automatically generating Repository implementations (CRUD operations) at runtime","C. It makes the UI faster","D. It writes CSS"],ans:1,exp:"You just declare an interface, and Spring provides all the database access logic instantly."},
      {q:"If your Entity is 'User' and its Primary Key is a 'Long', how do you declare the repository?",opts:["A. class UserRepository extends Database","B. interface UserRepository extends JpaRepository<User, Long>","C. class UserRepo implements SQL","D. interface UserRepository extends Crud<Long>"],ans:1,exp:"The generics <Entity, ID> tell Spring exactly what tables and data types it is dealing with."},
      {q:"What is 'Query Method Derivation' in Spring Data JPA?",opts:["A. Writing SQL in an XML file","B. Spring automatically generating SQL queries simply by parsing the English name of your method (e.g., findByLastName(String name))","C. Using a calculator","D. Hashing passwords"],ans:1,exp:"It is literal magic. You type a method signature, and Spring builds the SQL WHERE clause for you."},
      {q:"If you declare 'List<User> findByAgeGreaterThan(int age);' in your repository, what SQL does Spring generate?",opts:["A. SELECT * FROM users","B. SELECT * FROM users WHERE age > ?","C. DELETE FROM users WHERE age > ?","D. It throws an error"],ans:1,exp:"Spring parses 'GreaterThan' and turns it into the SQL '>' operator."},
      {q:"Do you need to add @Repository to an interface extending JpaRepository?",opts:["A. Yes, absolutely required","B. No, Spring Data JPA automatically detects interfaces extending JpaRepository and handles them","C. Only on Fridays","D. Yes, or it won't compile"],ans:1,exp:"While you can add it for clarity, it is completely optional. Spring handles it via proxy generation."}
    ],
    flows:[
      {title:"Query Derivation Flow",items:["start:Call repo.findByEmail('test@a.com')","proc:Spring parses method name","proc:Extracts 'findBy' and 'Email'","dec:Generates SQL: SELECT * FROM user WHERE email = ?","end:Executes and returns User object"]}
    ],
    game:{icon:"✨",title:"The Magician",desc:"Master Spring Data magic",badges:["✨ Boilerplate Slayer","📝 Method Namer","🚀 Repo Master"],challenges:[{icon:"📝",title:"Derive Query",desc:"Method name for: Select users by status?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Magic Repository",badge:"Sorcerer",desc:"Create a Spring Data repository with derived queries.",tags:["Spring","Database"],steps:[{title:"Interface",desc:"interface UserRepo extends JpaRepository<User, Long>"},{"title:"Derived Query 1",desc:"List<User> findByRole(String role);"},{"title:"Derived Query 2",desc:"boolean existsByEmail(String email);"}],code:`import org.springframework.data.jpa.repository.JpaRepository;\n\n// That's it. No implementation class needed!\npublic interface UserRepository extends JpaRepository<User, Long> {\n  \n  // Spring generates: SELECT * FROM users WHERE status = ?\n  List<User> findByStatus(String status);\n  \n  // Spring generates: SELECT COUNT(...) > 0 FROM users WHERE email = ?\n  boolean existsByEmail(String email);\n}`}
  },
  t82: {
    tag:'Phase 2 · Backend (Spring)', num:82,
    title:'JPQL vs Native SQL',
    desc:'Writing custom queries when method derivation isn\'t enough.',
    theory:`<div class="card"><h3>🗣️ Speaking to the Database</h3><p>Sometimes, Spring Data JPA's method naming (<code>findByEmailAndAgeGreaterThanAndStatusOrderByCreatedAtDesc</code>) gets ridiculous, or you need complex Joins. In this case, you use the <code>@Query</code> annotation.</p><h4>JPQL (Java Persistence Query Language)</h4><p>JPQL looks like SQL, but <strong>it queries your Java Classes (Entities), NOT your database tables</strong>. It is database-agnostic. <br><code>@Query("SELECT u FROM User u WHERE u.email = ?1")</code></p><h4>Native SQL</h4><p>If you need to use a database-specific feature (like a Postgres JSONB function), you can write raw SQL by setting <code>nativeQuery = true</code>. This bypasses Hibernate's translation, but ties your code to that specific database. <br><code>@Query(value = "SELECT * FROM users WHERE...", nativeQuery = true)</code></p></div>`,
    mcqs:[
      {q:"What is the primary difference between JPQL and Native SQL?",opts:["A. JPQL is faster","B. JPQL queries Java Entity Classes and Fields (Database Agnostic). Native SQL queries actual Database Tables and Columns (Database Specific).","C. Native SQL is for NoSQL databases","D. They are identical"],ans:1,exp:"In JPQL, you write 'SELECT u FROM User u'. 'User' is your Java class, not the table name."},
      {q:"Why might you prefer JPQL over Native SQL?",opts:["A. Because it looks cooler","B. If you switch from MySQL to PostgreSQL, your JPQL queries will automatically be translated correctly by Hibernate. Native SQL might break.","C. JPQL runs instantly without compiling","D. Native SQL is deprecated"],ans:1,exp:"Database agnosticism is a huge architectural advantage."},
      {q:"When MUST you use Native SQL instead of JPQL?",opts:["A. When querying by ID","B. When you need to use a highly specific, proprietary database feature (like Postgres PostGIS spatial queries or JSONB manipulation) that Hibernate doesn't understand","C. When joining tables","D. When doing math"],ans:1,exp:"JPQL only supports standard SQL concepts. Proprietary features require native queries."},
      {q:"How do you pass a method parameter into a @Query string?",opts:["A. Using string concatenation (+)","B. Using named parameters (e.g. :status) combined with the @Param annotation on the method argument","C. You can't pass variables","D. Using global variables"],ans:1,exp:"Never use string concatenation for queries to avoid SQL Injection attacks."},
      {q:"What annotation do you use to define a custom query in a Spring Data interface?",opts:["A. @SQL","B. @Database","C. @Query","D. @Select"],ans:2,exp:"Place @Query above your method signature in the interface."}
    ],
    flows:[
      {title:"Query Resolution",items:["start:Repository Method Called","dec:Has @Query annotation?","proc:(No) Use Method Name Derivation","dec:(Yes) Is nativeQuery=true?","proc:(No) Translate JPQL to SQL","end:(Yes) Pass raw SQL directly to DB"]}
    ],
    game:{icon:"🗣️",title:"The Linguist",desc:"Master query languages",badges:["🗣️ JPQL Speaker","🗄️ Native Hacker","🛡️ Injection Preventer"],challenges:[{icon:"📝",title:"Identify Param",desc:"How to bind a parameter in JPQL?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Custom Queries",badge:"Query Crafter",desc:"Write a JPQL and a Native query.",tags:["Spring","SQL"],steps:[{title:"JPQL",desc:"@Query('SELECT u FROM User u WHERE u.status = :stat')"},{"title:"Bind",desc:"Pass @Param('stat') String stat"},{"title:"Native",desc:"@Query(value='SELECT * FROM users LIMIT 1', nativeQuery=true)"}],code:`public interface UserRepo extends JpaRepository<User, Long> {\n\n  // JPQL: Querying the Object ('User' is the class name)\n  @Query("SELECT u FROM User u WHERE u.status = :stat")\n  List<User> findCustomByStatus(@Param("stat") String stat);\n\n  // Native SQL: Querying the Database ('tbl_users' is the table)\n  @Query(value = "SELECT * FROM tbl_users LIMIT 5", nativeQuery = true)\n  List<User> getFiveRandomUsers();\n}`}
  },
  t83: {
    tag:'Phase 2 · Backend (Spring)', num:83,
    title:'Transaction Management',
    desc:'Ensuring data integrity by grouping multiple database operations into a single atomic unit of work.',
    theory:`<div class="card"><h3>🏦 The All-or-Nothing Rule</h3><p>Imagine a Bank Transfer: You must deduct $100 from Account A, and add $100 to Account B. If the server crashes <em>after</em> the deduction but <em>before</em> the addition, the money vanishes!</p><h4>ACID Transactions</h4><p>A <strong>Transaction</strong> groups these operations together. It guarantees <strong>Atomicity</strong> (All-or-Nothing). If any operation fails, the database performs a <strong>Rollback</strong>, undoing everything. If all succeed, it performs a <strong>Commit</strong>, saving everything.</p><div class="cb"><span class="cm">// In Spring, it's insanely easy:</span>
<span class="ck">@Transactional</span>
<span class="ck">public void</span> transferMoney() {
    <span class="cm">// Deduct from A (SQL UPDATE)</span>
    <span class="cm">// Add to B (SQL UPDATE)</span>
    <span class="cm">// If ANY Exception occurs here, Spring automatically rolls back both!</span>
}</div></div>`,
    mcqs:[
      {q:"What is the primary purpose of a Database Transaction?",opts:["A. To make queries run faster","B. To group multiple SQL operations into a single atomic unit that must completely succeed (Commit) or completely fail (Rollback), preventing partial data corruption","C. To encrypt data","D. To log user activity"],ans:1,exp:"Transactions protect your database from hardware crashes or software bugs mid-execution."},
      {q:"What Spring annotation enables automatic transaction management for a method?",opts:["A. @Transaction","B. @DatabaseSafe","C. @Transactional","D. @Commit"],ans:2,exp:"By adding @Transactional, Spring intercepts the method, starts a transaction before it runs, and commits/rolls back after it finishes."},
      {q:"Under what specific condition will Spring @Transactional automatically trigger a Rollback?",opts:["A. Whenever the method returns null","B. Automatically, if any Unchecked Exception (RuntimeException) is thrown during the method execution","C. If the method takes longer than 5 seconds","D. If the user clicks cancel"],ans:1,exp:"By default, Spring rolls back on RuntimeExceptions. It does NOT roll back on Checked Exceptions (like IOException) unless you specifically configure it to."},
      {q:"What does the 'A' in ACID stand for?",opts:["A. Asynchronous","B. Atomicity (All-or-Nothing)","C. Arrays","D. Application"],ans:1,exp:"ACID = Atomicity, Consistency, Isolation, Durability. The core tenets of reliable databases."},
      {q:"Where is the best architectural place to put the @Transactional annotation?",opts:["A. On the Entity class","B. On the Controller layer","C. On the Service layer (Business Logic)","D. On the HTML View"],ans:2,exp:"The Service layer is where you orchestrate multiple repository calls (like deducting from one account and adding to another)."}
    ],
    flows:[
      {title:"@Transactional Flow",items:["start:Call transferMoney()","proc:Spring intercepts, starts DB Transaction","proc:Deduct from A succeeds","dec:Add to B throws Exception!","proc:Spring catches Exception","end:Spring issues ROLLBACK to DB!"]}
    ],
    game:{icon:"🏦",title:"The Banker",desc:"Master ACID compliance",badges:["🏦 ACID Compliant","⏪ Rollbacker","🛡️ Data Protector"],challenges:[{icon:"📝",title:"Rollback Rule",desc:"When does Spring auto-rollback?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Safe Transfer",badge:"Bank Teller",desc:"Write a transactional service method.",tags:["Spring","Database"],steps:[{title:"Service",desc:"Create BankService"},{"title:"Annotation",desc:"Add @Transactional to method"},{"title:"Logic",desc:"Update two repos, throw error to test rollback"}],code:`@Service\npublic class BankService {\n\n  // If this method crashes at ANY point, NO data is saved.\n  @Transactional\n  public void transfer(Long fromId, Long toId, int amount) {\n    accountRepo.deduct(fromId, amount);\n    \n    // Imagine server crashes here!\n    if(true) throw new RuntimeException("Server crash!");\n    \n    // This never runs. The deduction is safely rolled back.\n    accountRepo.add(toId, amount); \n  }\n}`}
  },
"""

start_marker = "};\n\nlet userXP"
inject_idx = content.find(start_marker)

if inject_idx != -1:
    new_content = content[:inject_idx] + ",\n" + rich_content + content[inject_idx:]
    with open(html_path, "w") as f:
        f.write(new_content)
    print("Successfully generated T78-T83 rich content!")
else:
    print("Could not find injection point.")
