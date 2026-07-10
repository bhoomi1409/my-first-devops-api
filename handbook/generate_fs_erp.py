import re

html_path = "/Users/bhoomim/devops CI:CD/handbook/fullstack_ai_handbook.html"
with open(html_path, "r") as f:
    content = f.read()

rich_content = r"""
  t171: {
    tag:'Phase 8 · ERP Systems', num:171,
    title:'Introduction to ERP',
    desc:'Enterprise Resource Planning: The central nervous system of modern businesses.',
    theory:`<div class="card"><h3>🏢 The Single Source of Truth</h3><p>Before <strong>ERP (Enterprise Resource Planning)</strong> systems, a company's HR department used one software, Finance used another, and Manufacturing used spreadsheets. When Manufacturing built a car, they had to email Finance to tell them to bill the customer.</p><h4>The ERP Revolution</h4><p>An ERP system replaces all these disconnected tools with one massive, unified software suite sharing a single, centralized database. When Manufacturing marks a car as "Shipped", the ERP instantly subtracts the parts from Inventory and automatically generates an invoice in Finance.</p></div>`,
    mcqs:[
      {q:"What does ERP stand for?",opts:["A. Electronic Revenue Processor","B. Enterprise Resource Planning. A unified software system that manages and integrates a company's financials, supply chain, operations, commerce, reporting, manufacturing, and HR activities.","C. Emergency Response Protocol","D. External Routing Platform"],ans:1,exp:"ERPs are the backbone of almost every Fortune 500 company."},
      {q:"What is the primary technical advantage of an ERP system?",opts:["A. It writes code for you","B. It provides a 'Single Source of Truth' by utilizing a centralized database. Data entered by one department (e.g., Sales) is instantly visible and usable by all other departments (e.g., Warehouse).","C. It prevents hacking","D. It is free"],ans:1,exp:"Without an ERP, data gets siloed and out of sync."},
      {q:"Why are ERP implementations notoriously difficult and expensive?",opts:["A. Because computers are slow","B. Because they require a company to completely overhaul and standardize its internal business processes to match the software's logic, which faces massive human resistance.","C. Because the code is written in Latin","D. Because they require new hardware"],ans:1,exp:"An ERP implementation is a business transformation project, not just an IT project."},
      {q:"Which of these is NOT typically considered a core module of an ERP?",opts:["A. Human Resources (HR)","B. Supply Chain Management (SCM)","C. First-Person Shooter Engine","D. Customer Relationship Management (CRM)"],ans:2,exp:"ERPs cover almost every aspect of a business."},
      {q:"Who are the traditional 'Big Two' vendors in the enterprise ERP market?",opts:["A. Apple and Google","B. SAP and Oracle","C. Meta and Netflix","D. Adobe and Salesforce"],ans:1,exp:"SAP is the undisputed king of manufacturing and supply chain ERPs."}
    ],
    flows:[
      {title:"The ERP Workflow",items:["start:Sales Rep closes a Deal in CRM module","proc:ERP instantly checks Inventory module","dec:Item is in stock!","proc:ERP automatically alerts Warehouse to ship","end:ERP automatically generates Invoice in Finance!"]}
    ],
    game:{icon:"🏢",title:"The Executive",desc:"Master ERP basics",badges:["🏢 Centralizer","🔗 Data Linker","🧠 Truth Seeker"],challenges:[{icon:"📝",title:"Data Silos",desc:"What happens without an ERP?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Mental Model",badge:"Strategist",desc:"Understand the DB structure.",tags:["ERP","Database"],steps:[{title:"The Old Way",desc:"HR Database + Finance Database + Sales Database"},{"title:"The ERP Way",desc:"One massive, normalized SQL database."},{"title:"The Result",desc:"Zero data duplication. Perfect reporting."}],code:`// The Philosophy of ERP:\n// Information should only be entered into a computer system ONCE.\n// After that, it should flow seamlessly to anyone who needs it.`}
  },
  t172: {
    tag:'Phase 8 · ERP Systems', num:172,
    title:'Core ERP Modules',
    desc:'The building blocks that make up a massive enterprise system.',
    theory:`<div class="card"><h3>🧩 The Puzzle Pieces</h3><p>An ERP is not just one app; it is a suite of <strong>Modules</strong> that all plug into the same database. A company might buy the Finance module but skip the Manufacturing module if they just sell software.</p><h4>The Big Three Modules</h4><ol><li><strong>FICO (Finance & Controlling):</strong> The most important module. General ledger, accounts payable/receivable, and financial reporting.</li><li><strong>SCM (Supply Chain Management):</strong> Tracking raw materials from the supplier, to the factory, to the warehouse, to the customer.</li><li><strong>HCM (Human Capital Management):</strong> Payroll, hiring, benefits, and employee performance.</li></ol></div>`,
    mcqs:[
      {q:"Which ERP module is the absolute core that almost every company implements first?",opts:["A. Manufacturing","B. Finance & Accounting (General Ledger, AP/AR). Every business must track money.","C. Social Media Management","D. Fleet Tracking"],ans:1,exp:"Finance is the heart of the ERP system."},
      {q:"What does the SCM (Supply Chain Management) module handle?",opts:["A. Writing emails","B. Procurement of raw materials, manufacturing routing, warehouse inventory management, and logistics/shipping.","C. Hiring employees","D. Building websites"],ans:1,exp:"If a company manufactures physical goods, SCM is critical."},
      {q:"What is a CRM (Customer Relationship Management) module?",opts:["A. A tool to manage servers","B. A module used by Sales and Marketing to track leads, customer interactions, support tickets, and sales pipelines (e.g., Salesforce).","C. A database indexing tool","D. A payroll calculator"],ans:1,exp:"Many companies use a dedicated CRM like Salesforce, but integrate it deeply with their main ERP."},
      {q:"Why do companies often buy ERP modules 'a la carte' (one by one)?",opts:["A. They are too heavy to download","B. To save money and reduce complexity. A hospital needs HCM and Finance, but they do not need a factory Manufacturing module.","C. Because modules conflict with each other","D. To avoid paying taxes"],ans:1,exp:"ERPs are highly modular and customizable."},
      {q:"What is the MRP (Material Requirements Planning) function within the Supply Chain module?",opts:["A. A tool to plan meetings","B. A complex calculator that looks at customer orders, checks current inventory, and automatically calculates exactly how much raw material needs to be purchased to build the products on time.","C. A marketing tool","D. A firewall"],ans:1,exp:"MRP was actually the historical predecessor to modern ERP systems in the 1970s!"}
    ],
    flows:[
      {title:"Module Interaction Flow",items:["start:HCM Module: Hires new factory worker","proc:SCM Module: Assigns worker to a machine","dec:Worker builds 10 widgets","proc:SCM adds 10 widgets to Inventory","end:Finance Module: Pays worker's hourly wage"]}
    ],
    game:{icon:"🧩",title:"The Modular Thinker",desc:"Master ERP components",badges:["🧩 FICO Expert","🚚 SCM Router","🤝 HCM Manager"],challenges:[{icon:"📝",title:"The Core",desc:"Which module is most important?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Module Mapping",badge:"Mapper",desc:"Map a business to modules.",tags:["ERP","Architecture"],steps:[{title:"Business",desc:"A Car Factory."},{"title:"Required Modules",desc:"FICO (Money), HCM (Workers), SCM (Parts), MRP (Planning), CRM (Deals)."},{"title:"Result",desc:"A fully integrated manufacturing powerhouse."}],code:`// ERP Data Flow Example\n// The 'Order to Cash' (O2C) Process:\n// 1. CRM: Lead becomes a Customer.\n// 2. Sales: Quote becomes a Sales Order.\n// 3. SCM: Warehouse picks, packs, and ships the item.\n// 4. Finance: Generates Invoice and receives Payment.\n// All tracked in ONE system!`}
  },
  t173: {
    tag:'Phase 8 · ERP Systems', num:173,
    title:'Monolithic vs Composable ERP',
    desc:'The architectural shift in how enterprises build their software stack.',
    theory:`<div class="card"><h3>🏛️ The Giant vs The Swarm</h3><p>Historically, companies bought a <strong>Monolithic ERP</strong> (like SAP ECC or Oracle EBS). You bought every module from one vendor. It was highly integrated but incredibly rigid, slow to upgrade, and had a terrible UI.</p><h4>Composable ERP (Postmodern ERP)</h4><p>Today, companies prefer a <strong>Composable ERP</strong> strategy. They buy a lightweight Core Finance ERP (like NetSuite), but use Workday for HR, Salesforce for CRM, and Shopify for E-commerce. They connect all these "Best-of-Breed" cloud apps together using APIs. It provides ultimate flexibility, but introduces massive integration challenges.</p></div>`,
    mcqs:[
      {q:"What is a major characteristic of a traditional Monolithic ERP?",opts:["A. It is extremely lightweight","B. It is a massive, highly-coupled, single-vendor suite where UI, logic, and data are tightly bound together. It provides incredible data consistency but is notoriously difficult to upgrade.","C. It requires no database","D. It runs on mobile phones"],ans:1,exp:"Upgrading a monolithic ERP can take years and cost millions."},
      {q:"What is the 'Composable ERP' (or Postmodern ERP) strategy?",opts:["A. Building an ERP in C++","B. Shifting away from a single vendor, and instead assembling a custom software stack by connecting various specialized 'Best-of-Breed' cloud applications together via APIs.","C. Using only open-source software","D. Deleting the ERP entirely"],ans:1,exp:"This allows a company to use the absolute best tool for each specific department."},
      {q:"What is a 'Best-of-Breed' application?",opts:["A. A dog breeding app","B. A software product that is universally recognized as the absolute best in its specific niche (e.g., Salesforce for CRM, Workday for HR), rather than a mediocre module bundled in a monolith.","C. The cheapest software","D. The oldest software"],ans:1,exp:"Vendors like SAP try to build everything, but they can't be the best at everything."},
      {q:"What is the biggest technical challenge of a Composable ERP strategy?",opts:["A. The screens are too bright","B. Integration. You now have 5 different apps with 5 different databases. You must build robust API integrations and data pipelines to ensure they all stay perfectly in sync.","C. It uses too much RAM","D. It only works on Mac"],ans:1,exp:"If Salesforce (CRM) and NetSuite (Finance) get out of sync, the company's reporting is ruined."},
      {q:"Why do modern enterprises prefer Cloud (SaaS) ERPs over On-Premise ERPs?",opts:["A. They look cooler","B. Cloud ERPs handle all server maintenance, backups, and security. Most importantly, they push automatic, seamless software updates, eliminating the nightmare of 'Version Lock'.","C. They don't require internet","D. They are free"],ans:1,exp:"On-premise ERPs are slowly dying."}
    ],
    flows:[
      {title:"Composable Architecture",items:["start:Best-of-Breed Stack","proc:HR: Workday (SaaS)","dec:CRM: Salesforce (SaaS)","proc:Finance (Core): NetSuite (SaaS)","end:iPaaS (MuleSoft) connects them all via APIs!"]}
    ],
    game:{icon:"🏛️",title:"The Strategist",desc:"Master ERP architecture",badges:["🏛️ Postmodernist","🏆 Best-of-Breed","🔗 Integration Master"],challenges:[{icon:"📝",title:"The Tradeoff",desc:"What do you trade for flexibility?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Tech Stack Design",badge:"Architect",desc:"Design a modern tech stack.",tags:["Architecture","Cloud"],steps:[{title:"Core",desc:"NetSuite (Finance/Inventory)"},{"title:"Edge Apps",desc:"Salesforce (CRM), Workday (HR), Shopify (Web)"},{"title:"Integration",desc:"Use an iPaaS to sync customers between Salesforce and NetSuite."}],code:`// Monolithic ERP:\n// One throat to choke. If it breaks, you call SAP.\n\n// Composable ERP:\n// Ultimate agility. If the CRM module is bad, you rip it out \n// and plug in a new one without touching the Finance module.`}
  },
  t174: {
    tag:'Phase 8 · ERP Systems', num:174,
    title:'Configuration vs Customization',
    desc:'The golden rule of ERP implementation that dictates success or failure.',
    theory:`<div class="card"><h3>⚙️ The Golden Rule</h3><p>When a company buys an ERP, it never perfectly matches their unique business processes. How do you fix this?</p><h4>Configuration (The Good Way)</h4><p>Using the ERP's built-in settings and toggles to adapt the software to your needs (e.g., changing a dropdown menu, setting tax rates, creating a custom workflow using the GUI). This is safe and survives software updates.</p><h4>Customization (The Dangerous Way)</h4><p>Writing custom, proprietary code (Java, C#, ABAP) directly into the core of the ERP to force it to do something it wasn't designed to do. <strong>When the ERP vendor releases a software update next year, your custom code will break!</strong></p></div>`,
    mcqs:[
      {q:"What is 'Configuration' in an ERP implementation?",opts:["A. Writing new source code","B. Using the software's built-in tools, toggles, and settings to tailor the system's behavior to the company's needs without writing any custom code.","C. Buying new hardware","D. Changing the company name"],ans:1,exp:"Configuration is safe, supported by the vendor, and upgrade-proof."},
      {q:"What is 'Customization' in an ERP implementation?",opts:["A. Changing a user's password","B. Writing proprietary, custom code (scripts, backend logic) to alter the core functionality of the ERP because the built-in settings weren't enough.","C. Installing a printer","D. Adding a logo"],ans:1,exp:"Customization is incredibly expensive to build and even more expensive to maintain."},
      {q:"Why is heavy Customization considered a massive risk ('Technical Debt') in ERP systems?",opts:["A. It makes the UI ugly","B. Because when the ERP vendor releases a new version (e.g., moving to the Cloud), all your custom code will likely break. You become trapped on an old version of the software ('Version Lock').","C. It slows down the internet","D. It is illegal"],ans:1,exp:"Many companies are stuck on 15-year-old software because they customized it too much to ever upgrade."},
      {q:"What is the modern best practice when an ERP's standard functionality doesn't match a company's business process?",opts:["A. Write a massive custom script inside the ERP","B. Change the company's business process to match the software's standard best practices, rather than forcing the software to match a flawed legacy process. (Or build a custom microservice OUTSIDE the ERP).","C. Sue the ERP vendor","D. Go back to using Excel"],ans:1,exp:"'Vanilla ERP' (zero customizations) is the holy grail of IT strategy."},
      {q:"If you absolutely MUST build custom logic, what is the modern 'Side-by-Side Extensibility' approach?",opts:["A. Writing the code on a piece of paper","B. Building the custom logic as a separate microservice hosted on AWS, and having it communicate with the 'Vanilla' ERP via standard REST APIs, keeping the ERP core completely clean.","C. Running two ERPs at the same time","D. Using two monitors"],ans:1,exp:"This keeps the core ERP perfectly clean and easy to upgrade!"}
    ],
    flows:[
      {title:"The Customization Trap",items:["start:Company wants a weird billing feature","proc:Dev writes custom C# code inside the ERP","dec:2 Years Later: ERP Vendor releases 'V2.0 Update'","proc:Company tries to update. Custom C# code crashes!","end:Company is permanently stuck on V1.0. Technical Debt!"]}
    ],
    game:{icon:"⚙️",title:"The Configurator",desc:"Master ERP implementation strategy",badges:["⚙️ Configurator","🚫 Anti-Customizer","🍦 Vanilla Advocate"],challenges:[{icon:"📝",title:"Version Lock",desc:"How does custom code trap you?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Side-by-Side Extensibility",badge:"Modernizer",desc:"Keep the core clean.",tags:["Architecture","Extensibility"],steps:[{title:"The Goal",desc:"Calculate a complex local tax."},{"title:"The Bad Way",desc:"Write a script inside the ERP DB."},{"title:"The Good Way",desc:"AWS Lambda function calculates tax. ERP calls it via API."}],code:`// ERP Implementation Golden Rule:\n// "Keep the Core Clean."\n\n// If you customize the core ERP code, you own that code forever.\n// When it breaks, the vendor will not help you.\n// Build extensions OUTSIDE the ERP and use APIs.`}
  },
  t175: {
    tag:'Phase 8 · ERP Systems', num:175,
    title:'Master Data Management (MDM)',
    desc:'The critical discipline of keeping enterprise data accurate and consistent.',
    theory:`<div class="card"><h3>🗃️ The Dictionary</h3><p>If Salesforce lists a customer as "Apple Inc.", but the Finance ERP lists them as "Apple Computer", and the Support portal lists them as "Apple", your reporting is completely broken. How do you know how much money Apple spent?</p><h4>Master Data</h4><p>Master Data is the core data essential to operations (Customers, Products, Employees). <strong>MDM (Master Data Management)</strong> is the technology and process of creating one single, authoritative, accurate record (The Golden Record) for each entity, and ensuring all systems sync to it.</p></div>`,
    mcqs:[
      {q:"What is 'Master Data' in an enterprise?",opts:["A. Old backup data","B. The core, relatively static data entities that describe the business (e.g., Customers, Products, Employees, Locations).","C. Transactional data like a single sales receipt","D. Temporary log files"],ans:1,exp:"Master Data rarely changes. Transactional data (orders, invoices) changes every second and references Master Data."},
      {q:"What is the primary goal of Master Data Management (MDM)?",opts:["A. To compress data files","B. To eliminate data silos, duplicates, and inconsistencies by creating a single, authoritative 'Golden Record' for every critical piece of data across the entire organization.","C. To encrypt passwords","D. To generate UI dashboards"],ans:1,exp:"If a customer updates their address on the website, MDM ensures the Finance system gets the new address instantly."},
      {q:"If the CRM system and the Finance system disagree on a customer's phone number, what concept dictates which system is correct?",opts:["A. The loudest developer","B. The 'System of Record' (or Source of Truth). A robust MDM strategy explicitly defines which system owns and controls a specific piece of data.","C. Alphabetical order","D. The newest system"],ans:1,exp:"For example, Workday (HR) is usually the System of Record for employee names. The ERP must listen to Workday."},
      {q:"What is 'Data Cleansing' in an MDM project?",opts:["A. Deleting all the data","B. The grueling process of identifying, merging, and fixing duplicate, inaccurate, or improperly formatted data before loading it into the new ERP.","C. Formatting hard drives","D. Writing unit tests"],ans:1,exp:"'Garbage In, Garbage Out'. A new ERP with bad data is just a shiny new garbage can."},
      {q:"How does an MDM system usually enforce the 'Golden Record' across multiple apps?",opts:["A. By printing paper reports","B. By acting as a central hub. When a record changes, the MDM publishes an Event/Message to a Message Broker (like Kafka), which broadcasts the update to all connected systems instantly.","C. By emailing users","D. By using CSS"],ans:1,exp:"Event-driven architecture is critical for keeping massive enterprises in sync."}
    ],
    flows:[
      {title:"MDM Golden Record Flow",items:["start:Salesforce: 'Jon Doe' (ID: 1)","proc:NetSuite: 'Jonathan Doe' (ID: 9)","dec:MDM System merges them!","proc:Creates Golden Record: 'Jonathan Doe' (Global ID: X)","end:MDM pushes Global ID 'X' back to both systems!"]}
    ],
    game:{icon:"🗃️",title:"The Librarian",desc:"Master enterprise data",badges:["🗃️ MDM Master","🥇 Golden Record Maker","🧹 Data Cleanser"],challenges:[{icon:"📝",title:"Garbage In",desc:"Why is cleansing critical before launch?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"System of Record",badge:"Data Owner",desc:"Assign data ownership.",tags:["MDM","Data"],steps:[{title:"Employee Data",desc:"Source of Truth: Workday (HR)"},{"title:"Customer Data",desc:"Source of Truth: Salesforce (CRM)"},{"title:"Invoice Data",desc:"Source of Truth: NetSuite (Finance)"}],code:`// The Data Sync Nightmare
// If you don't define a 'System of Record', 
// a user might update their address in the Support Portal,
// and the Finance ERP might overwrite it the next day with old data.
// MDM ensures everyone agrees on the truth.`}
  },
  t176: {
    tag:'Phase 8 · ERP Systems', num:176,
    title:'ERP Integrations (ETL/APIs)',
    desc:'Connecting the ERP to the outside world.',
    theory:`<div class="card"><h3>🔌 The Integration Layer</h3><p>An ERP cannot exist in isolation. It must pull daily exchange rates from a bank, push shipping orders to FedEx, and sync customer data with Salesforce.</p><h4>Integration Patterns</h4><ul><li><strong>ETL (Extract, Transform, Load):</strong> Batch processing. Once a night, a script extracts 10,000 rows from a legacy database, transforms them into JSON, and loads them into the ERP.</li><li><strong>Webhooks / APIs:</strong> Real-time. When a user buys a shirt on Shopify, Shopify instantly sends an HTTP POST (Webhook) to the ERP to deduct inventory.</li><li><strong>iPaaS:</strong> Platforms like MuleSoft or Boomi act as graphical drag-and-drop integration hubs to manage these complex API connections safely.</li></ul></div>`,
    mcqs:[
      {q:"What does ETL stand for in data integration?",opts:["A. Electronic Transfer Logic","B. Extract, Transform, Load. The process of pulling data from a source, cleaning/formatting it, and inserting it into a destination (like an ERP or Data Warehouse).","C. External Text Language","D. Encrypted Token Layer"],ans:1,exp:"ETL is typically used for massive, scheduled batch jobs (e.g., syncing millions of rows at 2 AM)."},
      {q:"What is a Webhook, and why is it better than API Polling for real-time ERP integration?",opts:["A. It is a fishing tool","B. A Webhook is an HTTP POST request triggered by an event. Instead of the ERP asking Shopify 'Any new orders?' every 5 seconds (Polling), Shopify instantly 'pushes' the order data to the ERP the millisecond a sale happens.","C. It is a database format","D. It is an XML parser"],ans:1,exp:"Webhooks are the foundation of modern, real-time, event-driven architectures."},
      {q:"What is an iPaaS (Integration Platform as a Service) like MuleSoft, Boomi, or Workato?",opts:["A. A cloud-based hardware server","B. A cloud platform that provides pre-built connectors and a visual interface to easily integrate hundreds of different SaaS applications (like linking Salesforce to SAP) without writing custom code.","C. An Apple product","D. A SQL database"],ans:1,exp:"iPaaS tools drastically reduce the time it takes to build complex integrations."},
      {q:"Why is Data Transformation (the 'T' in ETL) necessary when integrating two systems?",opts:["A. Because it looks pretty","B. Because System A might store dates as 'MM-DD-YYYY' and gender as 'M/F', while the ERP requires dates as 'YYYY-MM-DD' and gender as 'Male/Female'. The data must be translated to match the target schema.","C. To encrypt it","D. To compress it"],ans:1,exp:"Data mapping and transformation are the most tedious parts of ERP integration."},
      {q:"What is an EDI (Electronic Data Interchange)?",opts:["A. A modern JSON API","B. An ancient, standardized text format used heavily in manufacturing and logistics to securely exchange purchase orders and invoices between the ERPs of different companies (B2B).","C. A database engine","D. A type of UI"],ans:1,exp:"EDI is old and clunky, but it powers the global supply chain."}
    ],
    flows:[
      {title:"Shopify to ERP Webhook Flow",items:["start:Customer buys Shoes on Shopify","proc:Shopify fires Webhook (HTTP POST)","dec:iPaaS (MuleSoft) receives JSON","proc:iPaaS transforms JSON to match ERP Schema","end:iPaaS calls ERP API -> Order created in ERP instantly!"]}
    ],
    game:{icon:"🔌",title:"The Connector",desc:"Master ERP Integrations",badges:["🔌 API Linker","🎣 Webhook Catcher","🔄 ETL Batcher"],challenges:[{icon:"📝",title:"Polling vs Webhooks",desc:"Why are webhooks vastly superior?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Data Transformation",badge:"Transformer",desc:"Map JSON between systems.",tags:["ETL","Integration"],steps:[{title:"Source (Salesforce)",desc:"{ 'first_name': 'Jon', 'last_name': 'Doe' }"},{"title:"The Transformation",desc:"Code merges strings: source.first_name + ' ' + source.last_name"},{"title:"Target (ERP)",desc:"{ 'fullName': 'Jon Doe' }"}],code:`// Example of a simple Webhook Endpoint in Node.js
app.post('/webhook/shopify-order', async (req, res) => {
  const shopifyOrder = req.body;
  
  // Transform the data to match our internal ERP Schema
  const erpOrder = {
    customer_name: \`\${shopifyOrder.customer.first_name} \${shopifyOrder.customer.last_name}\`,
    total_revenue: shopifyOrder.total_price,
    item_sku: shopifyOrder.line_items[0].sku
  };

  // Push to our internal ERP API
  await myErpApi.createSalesOrder(erpOrder);
  
  // Instantly return 200 OK so Shopify knows we got it!
  res.sendStatus(200);
});`}
  },
  t177: {
    tag:'Phase 8 · ERP Systems', num:177,
    title:'Popular ERP Giants',
    desc:'The major players dominating the enterprise software market.',
    theory:`<div class="card"><h3>👑 The Kings of Enterprise</h3><p>Choosing an ERP is a million-dollar decision. The market is dominated by a few massive vendors.</p><ul><li><strong>SAP (S/4HANA):</strong> The German giant. The undisputed king of massive global enterprises and complex manufacturing/supply chains. Very rigid, very powerful.</li><li><strong>Oracle (NetSuite & Cloud ERP):</strong> The database king. NetSuite was the first true cloud ERP, highly favored by mid-market tech companies and startups going public.</li><li><strong>Microsoft (Dynamics 365):</strong> Integrates flawlessly with Office 365, Teams, and Azure. Very popular for companies already in the Microsoft ecosystem.</li></ul></div>`,
    mcqs:[
      {q:"Which company is generally considered the global market leader in Tier 1 Enterprise ERP systems, especially for massive manufacturing and supply chain operations?",opts:["A. Apple","B. SAP","C. Intuit","D. Google"],ans:1,exp:"SAP's flagship product is currently S/4HANA, which runs on their blazing fast, in-memory HANA database."},
      {q:"Which ERP system was famously built 'in the cloud from day one' and is incredibly popular among fast-growing mid-market companies and tech startups?",opts:["A. SAP ECC","B. Oracle NetSuite","C. QuickBooks","D. Microsoft Excel"],ans:1,exp:"Oracle acquired NetSuite in 2016 for $9.3 billion."},
      {q:"What is a major advantage of Microsoft Dynamics 365?",opts:["A. It is entirely open source","B. Deep, native integration with the rest of the Microsoft ecosystem (Azure, Office 365, Teams, Power BI), providing a seamless experience for users.","C. It runs without an operating system","D. It is designed for gamers"],ans:1,exp:"If a company uses Windows and Office, Dynamics 365 is a very compelling choice."},
      {q:"What is 'Tier 1' vs 'Tier 2' in the ERP market?",opts:["A. Server sizes","B. Tier 1 ERPs (SAP, Oracle) are for massive global enterprises ($1B+ revenue) with immense complexity. Tier 2 ERPs (NetSuite, Sage) are for mid-market companies.","C. Pricing plans","D. UI colors"],ans:1,exp:"Implementing a Tier 1 ERP can literally take 3 to 5 years."},
      {q:"Why do massive companies spend tens of millions of dollars implementing SAP or Oracle instead of building their own software?",opts:["A. Because it looks cool","B. Because these ERPs have 40+ years of 'Best Practices' for almost every industry baked directly into the software, ensuring legal, financial, and operational compliance globally.","C. Because they don't have developers","D. Because it is faster"],ans:1,exp:"You aren't just buying code; you are buying a proven business operating model."}
    ],
    flows:[
      {title:"Choosing an ERP",items:["start:Is the company a massive global manufacturer?","dec:(Yes) SAP S/4HANA or Oracle Cloud ERP","proc:(No) Are they a fast-growing SaaS startup?","dec:(Yes) Oracle NetSuite","end:(No) Deep in MS Ecosystem? Microsoft Dynamics 365"]}
    ],
    game:{icon:"👑",title:"The Consultant",desc:"Know the ERP market",badges:["👑 Tier 1 Expert","☁️ NetSuite Fan","🟦 Microsoft Aligned"],challenges:[{icon:"📝",title:"Best Practices",desc:"Why buy instead of build?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Market Mapping",badge:"Analyst",desc:"Map vendors to company sizes.",tags:["Business","Market"],steps:[{title:"Tier 1",desc:"Walmart, Coca-Cola -> SAP / Oracle ERP Cloud"},{"title:"Tier 2",desc:"Zoom, Spotify -> Oracle NetSuite"},{"title:"Tier 3",desc:"Local Bakery -> QuickBooks Online / Xero"}],code:`// Software as a Business Model
// The code is just a tool. 
// A great ERP enforces operational discipline, ensures SOX compliance, 
// and makes a company highly attractive to auditors and investors.`}
  },
  t178: {
    tag:'Phase 8 · ERP Systems', num:178,
    title:'Open Source ERPs (Odoo/ERPNext)',
    desc:'Accessible, customizable alternatives to the expensive enterprise giants.',
    theory:`<div class="card"><h3>🐧 Power to the People</h3><p>SAP and Oracle cost millions in licensing and implementation fees. For small-to-medium businesses (SMBs) or highly technical startups, <strong>Open Source ERPs</strong> are a game-changer.</p><h4>Odoo & ERPNext</h4><p>These platforms provide full ERP functionality (Accounting, Inventory, CRM, eCommerce) for free (or very cheap). Because the source code (usually Python) is open, you can host it on your own AWS server, inspect the code, and customize it infinitely without asking a vendor for permission.</p></div>`,
    mcqs:[
      {q:"What is the primary advantage of Open Source ERPs like Odoo and ERPNext?",opts:["A. They are built by Apple","B. They provide massive enterprise-grade functionality at a fraction of the cost, and grant developers total access to the source code for ultimate customization.","C. They require no database","D. They are written in HTML"],ans:1,exp:"They democratize business software for startups and SMBs."},
      {q:"Which popular open-source ERP is known for its highly modular 'App Store' approach, where you can install CRM, Website Builder, and Accounting as separate apps?",opts:["A. SAP","B. Odoo","C. Workday","D. Salesforce"],ans:1,exp:"Odoo's UI is incredibly modern and user-friendly, rivaling top SaaS tools."},
      {q:"What programming language are both Odoo and ERPNext primarily built with?",opts:["A. Java","B. Python (often paired with a Javascript frontend and a Postgres or MariaDB database)","C. C++","D. Ruby"],ans:1,exp:"Python's readability makes it easy for developers to jump in and customize the ERP logic."},
      {q:"What is a major risk or 'hidden cost' of using a free Open Source ERP?",opts:["A. It might have viruses","B. The cost of implementation, hosting, security, and maintenance. If the server crashes or the code breaks, you are entirely responsible for fixing it. There is no vendor support hotline.","C. It is illegal to use","D. It runs too slowly"],ans:1,exp:"'Free as in speech, not free as in beer.' You pay with developer hours instead of licensing fees."},
      {q:"How do Open Source ERP companies (like Odoo S.A.) actually make money if the software is free?",opts:["A. They sell ads","B. Through a 'Freemium' model (Enterprise features cost money), managed cloud hosting, and premium technical support/consulting services.","C. They mine crypto","D. They don't make money"],ans:1,exp:"The 'Community' version is free. The 'Enterprise' version requires a paid license."}
    ],
    flows:[
      {title:"Open Source Deployment Flow",items:["start:Startup needs an ERP but has zero budget","proc:Dev provisions an AWS EC2 Ubuntu Server","dec:Dev clones ERPNext repo from GitHub","proc:Runs setup script (Installs Python, MariaDB, Redis)","end:ERP is live! Total cost: $20/month for the server."]}
    ],
    game:{icon:"🐧",title:"The Open Sourcer",desc:"Master Open Source ERPs",badges:["🐧 Penguin Rider","🐍 Python Hacker","💰 Cost Saver"],challenges:[{icon:"📝",title:"Hidden Costs",desc:"What is the catch with 'free' ERPs?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Odoo Architecture",badge:"Pythonista",desc:"Understand Odoo's MVC pattern.",tags:["Odoo","Python"],steps:[{title:"Model",desc:"Python classes define database tables (ORM)."},{"title:"View",desc:"XML files define the UI forms and lists."},{"title:"Controller",desc:"Python routes handle HTTP web requests."}],code:`# Example of creating a custom Module in Odoo (Python)
from odoo import models, fields

class HospitalPatient(models.Model):
    _name = 'hospital.patient' # Creates a DB table!
    _description = 'Patient Record'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('m', 'Male'),
        ('f', 'Female')
    ], string='Gender')
    # Odoo automatically generates the UI and Database schema from this class!`}
  },
  t179: {
    tag:'Phase 8 · ERP Systems', num:179,
    title:'Building a Custom ERP',
    desc:'Why you should (and usually should not) build your own enterprise software from scratch.',
    theory:`<div class="card"><h3>🏗️ Re-inventing the Wheel</h3><p>Every ambitious engineering team eventually asks: "Why don't we just build our own ERP from scratch using React and Node.js? It will be exactly what we need, and we save millions on licenses!"</p><h4>The Build vs Buy Dilemma</h4><p>Building a custom ERP is almost always a catastrophic mistake. ERPs deal with multi-currency accounting, complex tax laws, depreciation logic, and supply chain routing. Your developers will spend 5 years writing accounting logic instead of building the actual product your company sells. <strong>Buy commodity features (Finance/HR), and Build competitive advantages (Your core product).</strong></p></div>`,
    mcqs:[
      {q:"What is the 'Build vs Buy' dilemma in enterprise software?",opts:["A. Deciding whether to build a server or buy a cloud server","B. The strategic decision of whether to develop custom software in-house ('Build') or purchase a commercial off-the-shelf solution ('Buy').","C. Deciding whether to build a house or buy one","D. A marketing strategy"],ans:1,exp:"This is a critical decision for CTOs and CIOs."},
      {q:"What is the golden rule for deciding whether to Build or Buy software?",opts:["A. Always build, it's cheaper","B. 'Buy commodity, Build core.' Buy software for standard business processes (Accounting, HR, Payroll). Build custom software only for processes that give you a unique competitive advantage in the market.","C. Always buy, it's safer","D. Flip a coin"],ans:1,exp:"Nobody buys your product because you have a really cool custom HR system. Just buy Workday."},
      {q:"Why do Custom ERP projects often fail spectacularly?",opts:["A. Developers get bored","B. Underestimation of complexity. Building basic forms is easy. Building a compliant, double-entry accounting ledger that handles global tax codes and reverse logistics takes years and highly specialized domain knowledge.","C. Javascript is too slow","D. The cloud is too expensive"],ans:1,exp:"You end up building a buggy, unmaintainable version of SAP."},
      {q:"In what rare scenario DOES it make sense for a company to build a custom ERP?",opts:["A. When they want to save money on licenses","B. When their business model is so profoundly unique (e.g., Amazon, SpaceX, Uber) that no existing commercial ERP can possibly handle their workflows or scale.","C. When they hire a new developer","D. When they are a small bakery"],ans:1,exp:"Tesla famously built their own custom ERP 'Warp' in a few months, but Tesla is an extreme exception."},
      {q:"If you choose to 'Buy' an ERP, what happens to your internal engineering team?",opts:["A. They get fired","B. They transition from building UI forms to focusing on High-Level Integrations (APIs), Data Analytics, and building custom microservices that augment the ERP to drive business value.","C. They write documentation all day","D. They do IT support"],ans:1,exp:"The role shifts from 'Coder' to 'Systems Architect'."}
    ],
    flows:[
      {title:"Build vs Buy Decision Flow",items:["start:Does this process give us a competitive edge?","dec:(Yes, e.g. Trading Algorithm) -> BUILD IT!","proc:(No, e.g. Employee Payroll) -> BUY IT!","dec:Does standard software fit 80% of our needs?","end:(Yes) -> BUY IT and adapt our processes to it!"]}
    ],
    game:{icon:"🏗️",title:"The CTO",desc:"Master Build vs Buy",badges:["🏗️ Decision Maker","💰 Commodity Buyer","⚔️ Core Builder"],challenges:[{icon:"📝",title:"The Golden Rule",desc:"Buy commodity, build...",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"CTO Strategy",badge:"Executive",desc:"Evaluate software investments.",tags:["Strategy","Business"],steps:[{title:"Feature: Double-Entry Accounting",desc:"Result: BUY (NetSuite/QuickBooks). Complex and standardized."},{"title:"Feature: Secret Recipe Recommendation AI",desc:"Result: BUILD. This is why customers pay us!"},{"title:"Feature: Team Chat",desc:"Result: BUY (Slack/Teams)."}],code:`// A CTO's inner monologue:
// "Our engineering talent is our most expensive and constrained resource."
// "Every hour they spend writing a generic 'Submit Expense' form..."
// "...is an hour they ARE NOT spending building our flagship product."
// "Buy the ERP."`}
  },
  t180: {
    tag:'Phase 8 · ERP Systems', num:180,
    title:'The Future of ERP (AI & IoT)',
    desc:'How intelligent technologies are transforming passive databases into proactive assistants.',
    theory:`<div class="card"><h3>🔮 The Intelligent Enterprise</h3><p>Traditional ERPs are passive; humans must manually type in data and run reports to find problems. The next generation of ERPs are <strong>Proactive</strong>.</p><ul><li><strong>IoT (Internet of Things):</strong> Sensors on factory machines send real-time data directly to the ERP. If a machine vibrates too much, the ERP automatically schedules maintenance <em>before</em> it breaks.</li><li><strong>AI & LLMs:</strong> Instead of clicking through 50 menus to find a report, the CEO simply types: <em>"Hey ERP, why did Q3 revenue drop in Germany?"</em> The AI instantly queries the database, generates a chart, and provides a textual summary.</li></ul></div>`,
    mcqs:[
      {q:"How is IoT (Internet of Things) transforming Supply Chain ERPs?",opts:["A. By making the screens brighter","B. By connecting physical objects (trucks, factory machines, shipping containers) to the internet, allowing them to automatically stream real-time telemetry and location data directly into the ERP without human data entry.","C. By playing music in the warehouse","D. By replacing human workers entirely"],ans:1,exp:"This enables 'Digital Twins'—a real-time virtual replica of your physical factory."},
      {q:"What is 'Predictive Maintenance'?",opts:["A. Guessing when to fix something","B. Using IoT sensors and AI to monitor machine health in real-time. The ERP detects anomalies and automatically triggers a repair work order BEFORE the machine actually breaks down, preventing factory downtime.","C. Fixing things after they break","D. Cleaning the servers"],ans:1,exp:"Downtime in a factory can cost millions of dollars an hour."},
      {q:"How are Large Language Models (LLMs) like GPT-4 being integrated into modern ERPs?",opts:["A. To write poetry","B. As conversational interfaces (Copilots). Users can ask natural language questions ('Show me inventory for Product X'), and the AI translates that into complex SQL queries, returning instant insights without needing a data analyst.","C. To generate random numbers","D. To design new company logos"],ans:1,exp:"SAP Joule and Microsoft Copilot are transforming how users interact with dense enterprise software."},
      {q:"What is 'Hyperautomation' in the context of an ERP?",opts:["A. Running the servers faster","B. The use of advanced tech (AI, Machine Learning, and Robotic Process Automation - RPA) to completely automate complex, multi-step business processes that previously required human decision-making.","C. Automated coffee machines","D. Deleting old data quickly"],ans:1,exp:"For example, AI automatically reading a scanned PDF invoice, matching it to a purchase order, and paying the vendor with zero human touches."},
      {q:"As ERP systems become highly intelligent and automated, what becomes the most critical asset for a company?",opts:["A. The color of their logo","B. High-Quality, Clean Data. AI and automation algorithms are useless (or actively dangerous) if the underlying Master Data they rely on is inaccurate or duplicated.","C. The size of their office","D. The number of employees"],ans:1,exp:"'Garbage In, Garbage Out' remains the most important rule in all of computer science."}
    ],
    flows:[
      {title:"The AI-Powered ERP Flow",items:["start:CEO types: 'Why are shipments delayed?'","proc:ERP Copilot (LLM) translates to SQL","dec:Queries SCM module -> Finds Truck #42 is broken","proc:Copilot generates summary & chart","end:Outputs: 'Truck 42 broke down. ETA delayed by 2 days.'"]}
    ],
    game:{icon:"🔮",title:"The Futurist",desc:"Master next-gen ERP tech",badges:["🔮 Future Seer","🤖 Copilot Commander","📡 IoT Whisperer"],challenges:[{icon:"📝",title:"Predictive",desc:"What is Predictive Maintenance?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"AI Database Query",badge:"Data Scientist",desc:"Use natural language for SQL.",tags:["AI","ERP"],steps:[{title:"The Schema",desc:"Provide the ERP DB schema to the LLM."},{"title:"The Prompt",desc:"'Write a Postgres query for Q3 revenue by region'."},{"title:"The Execution",desc:"Run the generated SQL and return the chart."}],code:`// The Future of ERP Interfaces
// We are moving away from GUI clicks and towards Conversational UI.

const userPrompt = "Find all open invoices over $10,000 for Apple Inc.";

// 1. LLM translates English to SQL based on your ERP Schema
const sqlQuery = await ai.generateSQL(userPrompt, erpSchema);

// 2. Execute against the database safely (Read-Only!)
const results = await db.execute(sqlQuery);

// 3. Return beautiful data to the user!`}
  }
"""

start_marker = "};\n\nlet userXP"
inject_idx = content.find(start_marker)

if inject_idx != -1:
    new_content = content[:inject_idx] + ",\n" + rich_content + content[inject_idx:]
    with open(html_path, "w") as f:
        f.write(new_content)
    print("Successfully generated T171-T180 rich content!")
else:
    print("Could not find injection point.")
