import re

html_path = "/Users/bhoomim/devops CI:CD/handbook/fullstack_ai_handbook.html"
with open(html_path, "r") as f:
    content = f.read()

rich_content = r"""
  t96: {
    tag:'Phase 2 · Databases', num:96,
    title:'Joins',
    desc:'Combining rows from two or more tables based on a related column between them.',
    theory:`<div class="card"><h3>🤝 Bringing Data Together</h3><p>Because Normalization splits data into multiple tables (e.g., Users in one table, Orders in another), we need a way to stitch them back together for the UI. That is what a <strong>JOIN</strong> does.</p><h4>Types of Joins</h4><ul><li><strong>INNER JOIN:</strong> Returns rows that have matching values in <em>both</em> tables. (e.g., Only users who have placed an order).</li><li><strong>LEFT JOIN:</strong> Returns <em>all</em> rows from the left table, and the matched rows from the right table. If there is no match, the right side returns NULL. (e.g., All users, and their orders if they have any).</li><li><strong>RIGHT JOIN:</strong> Opposite of Left Join.</li><li><strong>FULL OUTER JOIN:</strong> Returns all rows from both tables, matching where possible, NULLing where not.</li></ul></div>`,
    mcqs:[
      {q:"What is the purpose of an SQL JOIN?",opts:["A. To delete data","B. To combine columns from one or more tables into a single result set based on a common column (usually a Foreign Key)","C. To sort the data","D. To encrypt the tables"],ans:1,exp:"Joins are the fundamental querying mechanism of Relational Databases."},
      {q:"If you want a list of ALL Users, regardless of whether they have ever placed an Order, which JOIN should you use?",opts:["A. INNER JOIN","B. LEFT JOIN (assuming Users is the left table)","C. RIGHT JOIN","D. OUTER JOIN"],ans:1,exp:"LEFT JOIN guarantees that no row from the left table is dropped, even if the right table has no matching data (it just returns NULLs for the right columns)."},
      {q:"What does an INNER JOIN do?",opts:["A. Returns everything","B. Returns ONLY the rows where there is a match in BOTH tables","C. Returns the left table only","D. Returns an error"],ans:1,exp:"If a user has never placed an order, they will NOT show up in an INNER JOIN result between Users and Orders."},
      {q:"Which clause is used to specify the exact columns that link the two tables together in a JOIN?",opts:["A. WHERE","B. ON (e.g., ON users.id = orders.user_id)","C. LINK","D. MATCH"],ans:1,exp:"The ON clause tells the database exactly how to stitch the rows together."},
      {q:"Why are JOINs considered computationally expensive?",opts:["A. Because they cost money","B. Because the database has to mathematically match rows from two different data structures, which can be very slow if the tables are massive and not properly indexed","C. Because they use RAM","D. They are actually very cheap"],ans:1,exp:"This is why NoSQL databases avoid JOINs entirely by embedding data in a single document."}
    ],
    flows:[
      {title:"Inner Join Flow",items:["start:Table A (IDs: 1, 2, 3)","proc:Table B (IDs: 2, 3, 4)","dec:INNER JOIN ON A.id = B.id","end:Result contains only IDs 2 and 3!"]}
    ],
    game:{icon:"🤝",title:"The Matchmaker",desc:"Master relational stitching",badges:["🤝 Joiner","⬅️ Left Leaner","🎯 Inner Core"],challenges:[{icon:"📝",title:"Left vs Inner",desc:"Explain the difference",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Write a Join",badge:"Stitcher",desc:"Write an SQL query with an INNER JOIN.",tags:["SQL","Database"],steps:[{title:"Select",desc:"SELECT users.name, orders.amount"},{"title:"From",desc:"FROM users"},{"title:"Join",desc:"INNER JOIN orders ON users.id = orders.user_id"}],code:`-- Get a list of names and the amounts they spent\nSELECT users.name, orders.amount\nFROM users\nINNER JOIN orders ON users.id = orders.user_id;\n\n-- If 'Bob' has 0 orders, he will NOT be in this list.`}
  },
  t97: {
    tag:'Phase 2 · Databases', num:97,
    title:'NoSQL Types',
    desc:'Exploring the 4 main families of Non-Relational databases.',
    theory:`<div class="card"><h3>📦 The Flexible Stores</h3><p>While all SQL databases are relatively similar (Tables/Rows), "NoSQL" is just a blanket term for anything that ISN'T relational. There are 4 distinct types of NoSQL databases, each designed for a completely different use case.</p><h4>The 4 Families</h4><ol><li><strong>Document Stores (MongoDB):</strong> Stores JSON-like objects. Great for flexible, hierarchical data.</li><li><strong>Key-Value Stores (Redis, DynamoDB):</strong> A massive HashMap. Lookups are purely by Key. Blisteringly fast. Great for caching or session storage.</li><li><strong>Wide-Column Stores (Cassandra):</strong> Highly optimized for massive write speeds and analytical queries on huge datasets.</li><li><strong>Graph Databases (Neo4j):</strong> Nodes and Edges. Highly optimized for complex relationships (e.g., Social Networks, Recommendation Engines).</li></ol></div>`,
    mcqs:[
      {q:"What is the primary characteristic of a Key-Value NoSQL database like Redis?",opts:["A. It stores XML","B. It acts like a massive HashMap, storing data as a single Value tied to a single Key, providing incredibly fast O(1) lookups","C. It uses Tables","D. It stores Graphs"],ans:1,exp:"Key-Value stores are the simplest and fastest type of NoSQL database."},
      {q:"Which type of NoSQL database is MongoDB?",opts:["A. Key-Value","B. Wide-Column","C. Document Store","D. Graph"],ans:2,exp:"MongoDB stores data in BSON (Binary JSON) documents, allowing for deeply nested, flexible data structures."},
      {q:"If you are building a 'People You May Know' feature for a social network, which NoSQL database type is specifically engineered for traversing complex relationships quickly?",opts:["A. Document Store","B. Graph Database (e.g., Neo4j)","C. Wide-Column","D. Key-Value"],ans:1,exp:"Graph databases treat the connections (Edges) between data points (Nodes) as first-class citizens."},
      {q:"Why might a company choose Cassandra (a Wide-Column store) over a standard SQL database?",opts:["A. It's easier to use","B. They need to handle massive amounts of incoming write data (like IoT sensor data or logging) spread across multiple global data centers without downtime","C. It supports JSON","D. It's free"],ans:1,exp:"Cassandra was originally developed at Facebook to handle Inbox Search, prioritizing massive write availability."},
      {q:"Does NoSQL mean 'No SQL'? ",opts:["A. Yes","B. It actually stands for 'Not Only SQL'. Most NoSQL databases now offer SQL-like query languages (e.g., Cassandra's CQL).","C. Yes, it's illegal to use SQL","D. No, it means 'New SQL'"],ans:1,exp:"The line between SQL and NoSQL is blurring as both adopt features from each other."}
    ],
    flows:[
      {title:"Choosing a Database",items:["start:Complex Relationships? -> Graph (Neo4j)","dec:Caching / Sessions? -> Key-Value (Redis)","dec:Massive Writes/Logs? -> Wide-Column (Cassandra)","end:Flexible Schema / Rapid Dev? -> Document (MongoDB)"]}
    ],
    game:{icon:"📦",title:"The Selector",desc:"Master NoSQL use cases",badges:["📦 Documenter","🔑 Key Master","🕸️ Graph Walker"],challenges:[{icon:"📝",title:"Identify DB",desc:"Which DB for a Social Network?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Mental Map",badge:"Architect",desc:"Match the database to the scenario.",tags:["Architecture","NoSQL"],steps:[{title:"Scenario 1",desc:"A shopping cart that expires in 1 hour -> Redis (Key-Value)"},{"title:"Scenario 2",desc:"A blog post with an array of comments -> MongoDB (Document)"},{"title:"Scenario 3",desc:"Financial accounting -> Postgres (SQL)"}],code:`// Database Architecture is about using the right tool.\n// Many modern apps use 'Polyglot Persistence':\n// 1. Postgres for User Accounts & Billing (ACID)\n// 2. Redis for caching active sessions (Speed)\n// 3. MongoDB for flexible product catalogs (Schema-less)\n// 4. ElasticSearch for text searching`}
  },
  t98: {
    tag:'Phase 2 · Databases', num:98,
    title:'CAP Theorem',
    desc:'A theorem stating that a distributed data store cannot simultaneously guarantee Consistency, Availability, and Partition Tolerance.',
    theory:`<div class="card"><h3>⚖️ Pick Two</h3><p>The <strong>CAP Theorem</strong> is the fundamental law of distributed databases (databases running on multiple servers). It states you can only guarantee <strong>TWO</strong> of the following three properties during a network failure:</p><ul><li><strong>Consistency (C):</strong> Every read receives the most recent write (or an error). All nodes see the exact same data.</li><li><strong>Availability (A):</strong> Every request receives a non-error response, but without the guarantee that it contains the most recent write.</li><li><strong>Partition Tolerance (P):</strong> The system continues to operate despite an arbitrary number of messages being dropped/delayed by the network between nodes.</li></ul><div class="box b-ro"><h5>The Reality</h5><p>Because networks fail (Partition Tolerance is mandatory), you really only get to choose between Consistency (<strong>CP</strong>) or Availability (<strong>AP</strong>).</p></div></div>`,
    mcqs:[
      {q:"What does the CAP Theorem state?",opts:["A. You can have all three if you pay enough money","B. A distributed database can only guarantee two out of three: Consistency, Availability, and Partition Tolerance","C. Databases must be Consistent","D. Code And Programming"],ans:1,exp:"You must make an architectural trade-off."},
      {q:"Since network failures (Partitions) are inevitable in the real world, the CAP theorem usually boils down to a choice between what?",opts:["A. Consistency vs Partition Tolerance","B. Consistency vs Availability (CP vs AP)","C. Availability vs Partition Tolerance","D. SQL vs NoSQL"],ans:1,exp:"When the network splits, do you return old data (Available) or return an error/block reads until the network heals (Consistent)?"},
      {q:"If an ATM database network splits, and it refuses to let you withdraw money (returns an error) until it can reconnect to the master server, what is it prioritizing?",opts:["A. Availability (AP)","B. Consistency (CP)","C. Speed","D. Partition Tolerance"],ans:1,exp:"Banks prefer to be offline (Unavailable) rather than risk giving you money you don't actually have (Inconsistent)."},
      {q:"If Twitter's network splits, and your feed loads but misses a tweet your friend just posted 1 second ago, what is Twitter prioritizing?",opts:["A. Consistency (CP)","B. Availability (AP)","C. Security","D. Relational Data"],ans:1,exp:"Twitter prefers to give you slightly stale data (Available) rather than crashing the app (Consistent)."},
      {q:"Standard Relational Databases (like single-node MySQL) technically prioritize what?",opts:["A. AP","B. CA (Consistency and Availability)","C. CP","D. None"],ans:1,exp:"Because they run on a single node, they don't have to deal with Partitions. But they lack distributed scalability."}
    ],
    flows:[
      {title:"The CAP Choice (Network Splits)",items:["start:Node A and Node B lose connection","dec:User requests data from Node B","proc:Option 1 (CP): Node B throws Error (Safe but Offline)","end:Option 2 (AP): Node B returns stale data (Online but Inaccurate)"]}
    ],
    game:{icon:"⚖️",title:"The Compromiser",desc:"Master distributed trade-offs",badges:["⚖️ CAP Master","🛑 Consistency Guard","✅ Availability Hero"],challenges:[{icon:"📝",title:"ATM Choice",desc:"Why do ATMs choose CP?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"CP vs AP (Mental)",badge:"Architect",desc:"Decide the trade-off for a system.",tags:["Architecture","Theory"],steps:[{title:"System",desc:"You are building a live chat app (like Discord)"},{"title:"Decision",desc:"Users want speed and uptime. Perfect consistency isn't critical."},{"title:"Result",desc:"Choose an AP database (like Cassandra) over a CP database."}],code:`// The CAP Theorem is an architectural decision.\n// CP Systems (HBase, MongoDB): Good for financial data, inventory.\n// AP Systems (Cassandra, DynamoDB): Good for social media, messaging, logs.`}
  },
  t99: {
    tag:'Phase 2 · Databases', num:99,
    title:'MongoDB Basics',
    desc:'The most popular Document-based NoSQL database.',
    theory:`<div class="card"><h3>📄 The Document Store</h3><p><strong>MongoDB</strong> stores data in <strong>BSON</strong> (Binary JSON). Instead of Tables and Rows, it uses <strong>Collections</strong> and <strong>Documents</strong>.</p><h4>Why developers love it</h4><ul><li><strong>Schema-less:</strong> You don't have to run <code>ALTER TABLE</code> SQL commands to add a new field. You just start sending JSON with the new field, and Mongo saves it.</li><li><strong>Embedding:</strong> Instead of doing complex JOINs, you can embed arrays and objects directly inside the document. A single database query returns the entire hierarchical object!</li></ul></div>`,
    mcqs:[
      {q:"What format does MongoDB use to store data under the hood?",opts:["A. XML","B. BSON (Binary JSON)","C. CSV","D. Plain Text"],ans:1,exp:"BSON extends standard JSON with extra data types (like Dates and ObjectIds) and is optimized for fast parsing."},
      {q:"In MongoDB, what are the equivalents to SQL's 'Table' and 'Row'?",opts:["A. Folder and File","B. Collection (Table) and Document (Row)","C. Map and Key","D. Array and Object"],ans:1,exp:"A Collection holds many Documents."},
      {q:"What is the defining feature of a MongoDB Collection?",opts:["A. It must have exactly 5 columns","B. It is 'Schema-less' (or flexible schema). Documents in the same collection do not need to have the exact same fields.","C. It is encrypted","D. It cannot be deleted"],ans:1,exp:"This flexibility allows for rapid iteration during development."},
      {q:"Instead of using Foreign Keys and JOINs, what is the preferred way to handle related data (like a User's multiple Addresses) in MongoDB?",opts:["A. Use two collections","B. Embed the addresses directly into the User document as an Array of objects","C. Use SQL","D. It's impossible"],ans:1,exp:"Embedding data means retrieving the User document automatically retrieves their addresses in a single, blazing-fast disk read."},
      {q:"What is the default primary key field automatically generated for every document in MongoDB?",opts:["A. id","B. primary_key","C. _id (an ObjectId)","D. uuid"],ans:2,exp:"MongoDB automatically generates a highly unique 12-byte ObjectId for the `_id` field if you don't provide one."}
    ],
    flows:[
      {title:"SQL vs Mongo (Data Retrieval)",items:["start:Goal: Get User and their Posts","proc:SQL: SELECT * FROM users JOIN posts ON... (Expensive)","dec:Mongo: db.users.find({_id: 1})","end:Mongo returns JSON with 'posts' array already embedded inside!"]}
    ],
    game:{icon:"📄",title:"The Documenter",desc:"Master MongoDB basics",badges:["📄 BSON Writer","📦 Embedder","🗂️ Schemaless Dev"],challenges:[{icon:"📝",title:"Table vs Collection",desc:"What is a Row called in Mongo?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Mongo Query",badge:"NoSQL Ninja",desc:"Write a basic MongoDB query.",tags:["Database","MongoDB"],steps:[{title:"Insert",desc:"db.users.insertOne({name: 'Alice', age: 25})"},{"title:"Find",desc:"db.users.find({age: {$gt: 20}})"},{"title:"Result",desc:"Returns a cursor to the JSON documents"}],code:`// MongoDB Shell Commands\n\n// 1. Insert a document (No CREATE TABLE needed!)\ndb.users.insertOne({\n  name: "Bhoomi",\n  skills: ["Java", "React"]\n});\n\n// 2. Query (Find all users where age is Greater Than 20)\ndb.users.find({ age: { $gt: 20 } });`}
  },
  t100: {
    tag:'Phase 2 · Databases', num:100,
    title:'Redis In-Memory Cache',
    desc:'The blazing fast, in-memory key-value store used to supercharge application performance.',
    theory:`<div class="card"><h3>⚡ The Lightning Cache</h3><p>Databases like Postgres or MongoDB store data on a Hard Drive (SSD). While SSDs are fast, <strong>RAM (Memory)</strong> is hundreds of times faster. <strong>Redis</strong> is a NoSQL Key-Value store that keeps all its data entirely in RAM!</p><h4>The Caching Pattern</h4><p>You don't replace Postgres with Redis. You use them together. When a user requests data, you check Redis first. If it's there (Cache Hit), you return it instantly (0.1ms). If it's not (Cache Miss), you query the slow Postgres database (50ms), save the result in Redis for next time, and return it.</p></div>`,
    mcqs:[
      {q:"Why is Redis significantly faster than traditional databases like PostgreSQL or MongoDB?",opts:["A. It uses better math","B. It stores all of its data entirely in RAM (In-Memory), completely bypassing the slow hard drive","C. It only stores strings","D. It runs on the client browser"],ans:1,exp:"RAM is volatile (data is lost if power dies), but incredibly fast. Redis does offer persistence options, but its primary use is as an in-memory cache."},
      {q:"What data model does Redis use?",opts:["A. Relational Tables","B. Key-Value pairs (essentially a massive, remote HashMap)","C. XML","D. Graphs"],ans:1,exp:"You look up a Value by its unique Key. O(1) time complexity."},
      {q:"What is a 'Cache Miss'?",opts:["A. When the cache crashes","B. When the application asks Redis for data, but the data isn't there, forcing the app to query the primary database","C. When data is corrupted","D. A cache collision"],ans:1,exp:"A good caching strategy aims to maximize Cache Hits and minimize Cache Misses."},
      {q:"What is a TTL (Time To Live) in Redis?",opts:["A. A security protocol","B. An expiration timer you can set on a Key. Once the TTL reaches 0, Redis automatically deletes the data to free up RAM.","C. The time it takes to reboot","D. A ping test"],ans:1,exp:"Because RAM is expensive and limited, you don't cache data forever. You cache it for a few minutes/hours."},
      {q:"Which of the following is a very common use case for Redis?",opts:["A. Storing a user's permanent billing history","B. Storing ephemeral User Session Tokens so API gateways can validate logins in <1ms","C. Storing large video files","D. Running complex analytical SQL queries"],ans:1,exp:"Never use Redis as the ONLY source of truth for critical data. Use it for transient data (Sessions) or cached data."}
    ],
    flows:[
      {title:"The Cache-Aside Pattern",items:["start:User requests Profile ID 5","dec:Check Redis for Key 'user:5'","proc:(Hit) Return data instantly!","proc:(Miss) Query Postgres for User 5","proc:Save User 5 to Redis with TTL=1 hr","end:Return data to User"]}
    ],
    game:{icon:"⚡",title:"The Speeder",desc:"Master in-memory caching",badges:["⚡ Cache Hitter","⏱️ TTL Master","🔑 Key-Value Pro"],challenges:[{icon:"📝",title:"Cache Miss",desc:"What happens on a cache miss?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Cache Logic",badge:"Optimizer",desc:"Implement the Cache-Aside pattern.",tags:["Architecture","Redis"],steps:[{title:"Check Cache",desc:"String data = redis.get(key)"},{"title:"Cache Hit",desc:"if (data != null) return data;"},{"title:"Cache Miss",desc:"data = db.query(); redis.set(key, data); return data;"}],code:`function getUserProfile(userId) {\n  let cacheKey = "user:" + userId;\n  \n  // 1. Check Cache (0.1ms)\n  let cachedData = redis.get(cacheKey);\n  if (cachedData != null) return cachedData; // Cache Hit!\n  \n  // 2. Cache Miss! Query slow Database (50ms)\n  let dbData = postgres.query("SELECT * FROM users WHERE id=" + userId);\n  \n  // 3. Save to Cache for next time (Expires in 3600 seconds)\n  redis.set(cacheKey, dbData, "EX", 3600);\n  \n  return dbData;\n}`}
  }
"""

start_marker = "};\n\nlet userXP"
inject_idx = content.find(start_marker)

if inject_idx != -1:
    new_content = content[:inject_idx] + ",\n" + rich_content + content[inject_idx:]
    with open(html_path, "w") as f:
        f.write(new_content)
    print("Successfully generated T96-T100 rich content!")
else:
    print("Could not find injection point.")
