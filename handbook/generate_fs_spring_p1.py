import re

html_path = "/Users/bhoomim/devops CI:CD/handbook/fullstack_ai_handbook.html"
with open(html_path, "r") as f:
    content = f.read()

rich_content = r"""
  t73: {
    tag:'Phase 2 · Backend (Spring)', num:73,
    title:'Spring Boot Annotations',
    desc:'Metadata tags that provide instructions to the Spring compiler and runtime.',
    theory:`<div class="card"><h3>🏷️ The Magic Tags</h3><p>Spring Boot heavily relies on <strong>Annotations</strong> (<code>@</code> symbols). They are essentially metadata that you attach to classes, methods, or variables to tell the Spring Framework how to treat them.</p><h4>Core Annotations</h4><ul><li><code>@SpringBootApplication</code>: The entry point. It auto-configures the app, enables component scanning, and tells Spring this is a configuration class.</li><li><code>@RestController</code>: Tells Spring that this class handles incoming HTTP web requests and should return JSON data.</li><li><code>@RequestMapping</code> / <code>@GetMapping</code> / <code>@PostMapping</code>: Maps a specific URL path (like <code>/users</code>) to a specific Java method.</li></ul><div class="cb"><span class="cm">// Example</span>
<span class="ck">@RestController</span>
<span class="ck">public class</span> <span class="cv">UserController</span> {
    <span class="ck">@GetMapping</span>(<span class="cs">"/hello"</span>)
    <span class="ck">public</span> String sayHi() { <span class="ck">return</span> <span class="cs">"Hi!"</span>; }
}</div></div>`,
    mcqs:[
      {q:"What is an Annotation in Java/Spring?",opts:["A. A comment that the compiler ignores","B. Metadata that provides data about a program but is not part of the program itself. Spring uses it to generate boilerplate code and wire the app together.","C. A type of loop","D. A database table"],ans:1,exp:"Annotations replace thousands of lines of XML configuration that old Java applications required."},
      {q:"Which annotation is used to mark the main entry point of a Spring Boot application?",opts:["A. @Main","B. @Start","C. @SpringBootApplication","D. @App"],ans:2,exp:"This single annotation combines @Configuration, @EnableAutoConfiguration, and @ComponentScan."},
      {q:"What does @RestController do?",opts:["A. It restarts the server","B. It marks a class as a web controller that handles HTTP requests, and automatically serializes the returned objects into JSON responses","C. It connects to a database","D. It runs a background thread"],ans:1,exp:"It is a convenience annotation combining @Controller and @ResponseBody."},
      {q:"If you want a method to trigger ONLY when a user makes an HTTP POST request to '/api/users', which annotation do you use?",opts:["A. @GetMapping('/api/users')","B. @PostMapping('/api/users')","C. @Put('/api/users')","D. @Web('/api/users')"],ans:1,exp:"POST is used for creating new resources."},
      {q:"What does @PathVariable do in a method signature?",opts:["A. It extracts a value from the URL path (e.g., /users/{id}) and binds it to a method parameter","B. It sets an environment variable","C. It finds a file path on the hard drive","D. It maps to a database column"],ans:0,exp:"If the URL is /users/5, @PathVariable int id will capture the number 5."}
    ],
    flows:[
      {title:"Annotation Routing",items:["start:User requests GET /hello","proc:Spring scans controllers","dec:Finds @GetMapping('/hello')?","proc:(Yes) Executes sayHi() method","end:Returns 'Hi!' to user"]}
    ],
    game:{icon:"🏷️",title:"The Tagger",desc:"Master Spring metadata",badges:["🏷️ Annotator","🌐 REST Router","🚀 Bootstrapper"],challenges:[{icon:"📝",title:"Identify Path",desc:"Difference between POST and GET?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Basic API Endpoint",badge:"Web Dev",desc:"Create a simple REST Controller returning JSON.",tags:["Spring","Web"],steps:[{title:"Class",desc:"Add @RestController to class"},{"title:"Method",desc:"Create public String getStatus()"},{"title:"Route",desc:"Add @GetMapping('/status') above method"}],code:`import org.springframework.web.bind.annotation.*;\n\n@RestController\npublic class HealthController {\n\n  @GetMapping("/status")\n  public String checkStatus() {\n    return "{\"status\": \"OK\", \"code\": 200}";\n  }\n}`}
  },
  t74: {
    tag:'Phase 2 · Backend (Spring)', num:74,
    title:'Dependency Injection',
    desc:'A design pattern where an object receives other objects that it depends on.',
    theory:`<div class="card"><h3>💉 The Code Surgeon</h3><p>If a <code>Car</code> needs an <code>Engine</code>, the naive approach is to write <code>Engine e = new Engine()</code> directly inside the Car class. This tightly couples the Car to a specific Engine. If you want to swap to an ElectricEngine, you have to rewrite the Car class.</p><h4>Dependency Injection (DI)</h4><p>Instead of the Car creating its own Engine, you <strong>inject</strong> the Engine into the Car from the outside (usually through the Constructor). The Car doesn't know or care how the Engine is built; it just knows it has one.</p><div class="box b-vi"><h5>@Autowired</h5><p>In Spring Boot, you don't even have to write the injection code yourself. You just slap <code>@Autowired</code> on a variable or constructor, and Spring automatically finds the right Dependency and injects it for you!</p></div></div>`,
    mcqs:[
      {q:"What problem does Dependency Injection solve?",opts:["A. It makes the code compile faster","B. It solves tight coupling. Objects no longer instantiate their own dependencies using 'new', making the system modular, easier to test, and flexible.","C. It injects CSS into HTML","D. It encrypts database passwords"],ans:1,exp:"Loose coupling means you can swap out a MySQL database class for a MongoDB class without changing the high-level business logic."},
      {q:"What happens if Class A uses the 'new' keyword to create an instance of Class B inside its constructor?",opts:["A. Class A and Class B are now tightly coupled","B. Class A and Class B are loosely coupled","C. Class A is now abstract","D. Class B is deleted"],ans:0,exp:"Using 'new' means Class A is completely dependent on that exact implementation of Class B."},
      {q:"What is the preferred way to inject a dependency in modern Spring Boot?",opts:["A. Field Injection (putting @Autowired directly on the variable)","B. Constructor Injection (passing the dependency through the class constructor)","C. Setter Injection","D. Writing an XML file"],ans:1,exp:"Constructor injection ensures that the object cannot be created without its required dependencies, making it immutable and easy to unit test."},
      {q:"What Spring annotation tells the framework to automatically inject a dependency?",opts:["A. @InjectThis","B. @GiveMe","C. @Autowired","D. @Dependency"],ans:2,exp:"Spring will scan the Application Context for a matching Bean and wire it in automatically."},
      {q:"If you use Constructor Injection with a single constructor in modern Spring Boot, do you still need to type @Autowired?",opts:["A. Yes, always","B. No, Spring automatically infers it and injects the parameters","C. Only if the parameter is a String","D. Yes, or it won't compile"],ans:1,exp:"This reduces boilerplate code and keeps your classes looking like clean, standard Java."}
    ],
    flows:[
      {title:"Constructor Injection",items:["start:App Needs a UserService","proc:UserService needs UserRepository","dec:Spring creates UserRepository first","proc:Spring calls new UserService(userRepository)","end:UserService is fully assembled!"]}
    ],
    game:{icon:"💉",title:"The Injector",desc:"Master loose coupling",badges:["💉 Autowirer","🔗 Decoupler","🏗️ Constructor Constructor"],challenges:[{icon:"📝",title:"Tight Coupling",desc:"Why is the 'new' keyword bad for architecture?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Refactor to DI",badge:"Architect",desc:"Change tightly coupled code to Dependency Injection.",tags:["Architecture","Spring"],steps:[{title:"Bad Code",desc:"Car has: this.engine = new V8Engine();"},{"title:"Constructor",desc:"Change to: public Car(Engine engine)"},{"title:"Assignment",desc:"this.engine = engine;"}],code:`// Tightly Coupled (BAD)\nclass Car {\n  Engine engine = new GasEngine();\n}\n\n// Dependency Injected (GOOD)\nclass Car {\n  private final Engine engine;\n  \n  // Spring injects the engine automatically!\n  public Car(Engine engine) {\n    this.engine = engine;\n  }\n}`}
  },
  t75: {
    tag:'Phase 2 · Backend (Spring)', num:75,
    title:'Inversion of Control',
    desc:'A principle in which the control of object creation and flow is transferred to a framework.',
    theory:`<div class="card"><h3>🔄 Giving Up the Reins</h3><p>Dependency Injection is actually just one specific implementation of a broader concept called <strong>Inversion of Control (IoC)</strong>.</p><h4>Traditional vs IoC</h4><p>In traditional programming, <strong>YOU</strong> are in control. Your <code>main()</code> method creates objects, calls their methods, and destroys them. You dictate the flow.</p><p>In a framework like Spring, the <strong>FRAMEWORK</strong> is in control. You write the components, but Spring decides when to instantiate them, how to wire them together, and when to call their methods (like calling your <code>@GetMapping</code> method when a web request arrives). The control has been inverted!</p></div>`,
    mcqs:[
      {q:"What does Inversion of Control (IoC) mean in the context of Spring?",opts:["A. Reversing a string","B. The flow of control is inverted: instead of your code calling a library, the framework calls your code and manages the lifecycle of your objects","C. Reversing a Linked List","D. Undoing a database transaction"],ans:1,exp:"You hand over the responsibility of object creation and flow management to the Spring IoC Container."},
      {q:"What is the relationship between IoC and Dependency Injection (DI)?",opts:["A. They are opposites","B. DI is a specific design pattern used to achieve IoC","C. They are completely unrelated","D. IoC is for front-end, DI is for back-end"],ans:1,exp:"IoC is the overarching philosophy (framework holds control). DI is the mechanism (framework hands you the objects you need)."},
      {q:"What is a 'Bean' in Spring?",opts:["A. A vegetable","B. An object that is instantiated, assembled, and otherwise managed by a Spring IoC container","C. A database row","D. A private variable"],ans:1,exp:"If you add @Component to a class, it becomes a Spring Bean."},
      {q:"Which of the following is an example of IoC?",opts:["A. Writing a 'for' loop to process data","B. Using the 'new' keyword to create a scanner","C. Adding an event listener to a button (the OS decides when to call your function, not you)","D. Adding 1 + 1"],ans:2,exp:"Event-driven programming, routing, and dependency injection are all forms of IoC."},
      {q:"What is the 'Hollywood Principle' often used to describe IoC?",opts:["A. 'Show me the money'","B. 'Don't call us, we'll call you'","C. 'I'll be back'","D. 'May the force be with you'"],ans:1,exp:"You don't call the framework to get things done; the framework calls your classes when it needs them."}
    ],
    flows:[
      {title:"Traditional vs IoC",items:["start:Traditional: Main -> new A() -> new B()","proc:IoC: Spring boots up","proc:Spring creates Bean B","proc:Spring creates Bean A","end:Spring injects B into A. Control is inverted!"]}
    ],
    game:{icon:"🔄",title:"The Director",desc:"Master the Hollywood principle",badges:["🔄 Inverter","🫘 Bean Counter","🎬 Hollywood Star"],challenges:[{icon:"📝",title:"Hollywood",desc:"Explain the Hollywood Principle",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Component Scanning",badge:"Scanner",desc:"Tell Spring to manage a class as a Bean.",tags:["Spring","IoC"],steps:[{title:"The Class",desc:"Create class NotificationService"},{"title:"The Tag",desc:"Add @Service or @Component to the class"},{"title:"The Magic",desc:"Spring IoC Container now manages this object!"}],code:`import org.springframework.stereotype.Service;\n\n// By adding this annotation, we give control to Spring.\n// Spring will create exactly ONE instance (a Singleton) of this class\n// and inject it wherever we use @Autowired.\n@Service\npublic class EmailService {\n  public void sendEmail() {\n    System.out.println("Email sent!");\n  }\n}`}
  },
  t76: {
    tag:'Phase 2 · Backend (Spring)', num:76,
    title:'Application Context',
    desc:'The advanced IoC container in Spring that holds all the Beans.',
    theory:`<div class="card"><h3>📦 The Bean Warehouse</h3><p>The <strong>ApplicationContext</strong> is the heart of a Spring application. It is the actual, literal implementation of the IoC container. When your app boots up, the Application Context scans your code, builds all your Beans, wires their dependencies together, and stores them in memory.</p><h4>Singleton by Default</h4><p>When the Application Context creates a Bean (like <code>UserService</code>), it creates exactly <strong>ONE instance</strong> of it. Every time you <code>@Autowire</code> a <code>UserService</code>, Spring hands you the exact same object from its warehouse. This is the <em>Singleton Design Pattern</em>, and it saves massive amounts of memory.</p></div>`,
    mcqs:[
      {q:"What is the 'ApplicationContext' in Spring?",opts:["A. The database connection pool","B. The central interface providing configuration for an application; it is the IoC container that holds and manages all the Beans","C. The web server","D. The user's browser"],ans:1,exp:"It is the giant warehouse containing every object your application needs to run."},
      {q:"How many instances of a specific @Service or @Component does the Application Context create by default?",opts:["A. A new one every time it is requested","B. Exactly one (Singleton scope)","C. Two","D. Ten"],ans:1,exp:"Singletons are highly efficient. Because a Service usually just contains logic (no state/data), there is no need to have more than one in memory."},
      {q:"What happens during 'Component Scanning'?",opts:["A. Spring scans the database for users","B. The Application Context scans your Java packages looking for classes annotated with @Component, @Service, @Controller, etc., and registers them as Beans","C. The OS scans for viruses","D. It reads XML files"],ans:1,exp:"Component scanning is how Spring discovers what it is supposed to manage."},
      {q:"If you absolutely NEED a brand new instance of a Bean every time it is injected, what must you change?",opts:["A. Delete the Application Context","B. Change the Bean's Scope from 'Singleton' to 'Prototype' using @Scope('prototype')","C. Use the 'new' keyword instead","D. Use an Interface"],ans:1,exp:"Prototype scope tells Spring to act like a factory, pumping out a new instance on every request."},
      {q:"Which of the following annotations is used for the Data Access (Database) layer to tell the Application Context it's a Bean?",opts:["A. @Controller","B. @Service","C. @Repository","D. @Component"],ans:2,exp:"@Repository is just a specialized @Component that also provides automatic database exception translation."}
    ],
    flows:[
      {title:"Application Context Boot",items:["start:App Starts","proc:Scans packages for Annotations","proc:Finds @Repository, @Service, @Controller","dec:Constructs them as Singletons","proc:Wires dependencies (@Autowired)","end:Ready to accept web requests!"]}
    ],
    game:{icon:"📦",title:"The Warehouse",desc:"Master the Spring Container",badges:["📦 Context Manager","🥇 Singleton Purist","🔍 Component Scanner"],challenges:[{icon:"📝",title:"Bean Scopes",desc:"Difference between Singleton and Prototype?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Scope Experiment",badge:"Scientist",desc:"Understand why Singletons share state (and why that can be dangerous).",tags:["Architecture","Spring"],steps:[{title:"Service",desc:"Create a Singleton Bean with an integer 'counter'"},{"title:"Controller",desc:"Inject Bean, increment counter on request"},{"title:"Test",desc:"Hit endpoint twice. Counter goes to 2! State is shared!"}],code:`@Service\npublic class CounterService {\n  // DANGER: Singletons share memory!\n  // If 1000 users hit the web server at once, they all \n  // access this exact same variable. \n  private int requests = 0;\n  \n  public int increment() {\n    return ++requests; // Not thread-safe without synchronization!\n  }\n}`}
  },
  t77: {
    tag:'Phase 2 · Backend (Spring)', num:77,
    title:'Spring MVC Architecture',
    desc:'Model-View-Controller: The architectural pattern used to separate concerns in web applications.',
    theory:`<div class="card"><h3>🏛️ The Three Pillars</h3><p>Spring Web is built on the <strong>Model-View-Controller (MVC)</strong> pattern. It separates an application into three interconnected parts to separate internal representations of information from the ways information is presented.</p><ul><li><strong>Model (Data):</strong> The structure of your data (e.g., a User class). It represents the business logic and database state.</li><li><strong>View (UI):</strong> The visual representation (e.g., an HTML page or a JSON response payload).</li><li><strong>Controller (Brain):</strong> The middleman. It receives the HTTP request from the user, asks the Model for data, and passes that data to the View to be rendered.</li></ul><div class="box b-ro"><h5>The DispatcherServlet</h5><p>In Spring, all incoming web requests hit a Front Controller called the <em>DispatcherServlet</em> first. It acts like a traffic cop, looking at the URL (e.g. /users) and routing the request to the correct specific Controller.</p></div></div>`,
    mcqs:[
      {q:"What does MVC stand for?",opts:["A. Model-View-Controller","B. Main-Virtual-Class","C. Micro-Variable-Code","D. Map-View-Code"],ans:0,exp:"It is the most famous architectural pattern for user interfaces and web frameworks."},
      {q:"In the MVC pattern, which component is responsible for handling the incoming HTTP request and deciding what to do next?",opts:["A. The Model","B. The View","C. The Controller","D. The Database"],ans:2,exp:"The Controller acts as the orchestrator. It doesn't do the heavy lifting, it just delegates."},
      {q:"What is the 'DispatcherServlet' in Spring MVC?",opts:["A. A database driver","B. The Front Controller that receives all incoming HTTP requests and routes them to the appropriate specific Controller based on the URL mappings (@GetMapping)","C. A security firewall","D. An HTML template"],ans:1,exp:"You never write the DispatcherServlet yourself; Spring Boot configures it automatically."},
      {q:"If a user submits a registration form, what does the Model represent in that scenario?",opts:["A. The HTML form itself","B. The Java Object (e.g., User user) that holds the submitted data (username, email) and the business logic to save it","C. The 'Submit' button","D. The HTTP POST request"],ans:1,exp:"The Model is the pure data and business rules, ignorant of how it is displayed."},
      {q:"In modern REST APIs (like you build with @RestController), what replaces the traditional 'View' (HTML page)?",opts:["A. There is no view","B. The JSON or XML data payload returned to the client (who then renders it on their own frontend, like React)","C. A database table","D. The Server"],ans:1,exp:"In a purely RESTful app, the View is just serialized data."}
    ],
    flows:[
      {title:"Spring MVC Request Flow",items:["start:User requests GET /api/users","proc:DispatcherServlet receives request","dec:Looks up routing map","proc:Routes to UserController.getUsers()","proc:Controller gets data from Model","end:Controller returns JSON (View)"]}
    ],
    game:{icon:"🏛️",title:"The Architect",desc:"Master the MVC pattern",badges:["🏛️ Pattern Purist","🚦 Traffic Cop","🔄 Flow Master"],challenges:[{icon:"📝",title:"Separation",desc:"Why separate Model and View?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"The Three Pillars",badge:"Builder",desc:"Identify the parts of an MVC flow in code.",tags:["Architecture","MVC"],steps:[{title:"Model",desc:"class Product { String name; int price; }"},{"title:"Controller",desc:"@RestController class ProductController"},{"title:"View",desc:"Returning JSON: { \"name\": \"Laptop\" }"}],code:`// MODEL (Data)\nclass User { public String name = "Bhoomi"; }\n\n// CONTROLLER (Traffic Cop)\n@RestController\nclass UserController {\n  \n  @GetMapping("/user")\n  public User getUser() {\n    // Gets the model, Spring handles the view translation\n    return new User(); \n    // VIEW (Output): {"name": "Bhoomi"}\n  }\n}`}
  },
"""

start_marker = "};\n\nlet userXP"
inject_idx = content.find(start_marker)

if inject_idx != -1:
    new_content = content[:inject_idx] + ",\n" + rich_content + content[inject_idx:]
    with open(html_path, "w") as f:
        f.write(new_content)
    print("Successfully generated T73-T77 rich content!")
else:
    print("Could not find injection point.")
