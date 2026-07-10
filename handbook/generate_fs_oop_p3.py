import re

html_path = "/Users/bhoomim/devops CI:CD/handbook/fullstack_ai_handbook.html"
with open(html_path, "r") as f:
    content = f.read()

rich_content = """
  t22: {
    tag:'Phase 1 · OOP', num:22,
    title:'Abstract Classes',
    desc:'A partially implemented class that serves as a foundation for subclasses.',
    theory:`<div class="card"><h3>🏛️ The Half-Built House</h3><p>An <strong>Abstract Class</strong> is a class that cannot be instantiated on its own (you cannot use <code>new AbstractClass()</code>). It is meant to be subclassed.</p><h4>Abstract vs Interfaces</h4><p>While an interface has NO implementation code, an Abstract Class can provide <em>shared default behavior</em> (regular methods) while forcing child classes to implement <em>specific behavior</em> (abstract methods).</p><div class="cb"><span class="cm">// TypeScript/Java Syntax</span>
<span class="ck">abstract class</span> <span class="cv">Shape</span> {
    <span class="cm">// Concrete method (shared)</span>
    printShape() { console.log(<span class="cs">"I am a shape."</span>); }
    
    <span class="cm">// Abstract method (forces child to implement)</span>
    <span class="ck">abstract</span> getArea(): number;
}

<span class="ck">class</span> <span class="cv">Square</span> <span class="ck">extends</span> Shape {
    constructor(private width: number) { <span class="ck">super</span>(); }
    <span class="cm">// MUST implement getArea</span>
    getArea() { <span class="ck">return</span> <span class="cs">this</span>.width * <span class="cs">this</span>.width; }
}</div></div>`,
    mcqs:[
      {q:"Can you create a direct instance of an Abstract Class?",opts:["A. Yes, always","B. No, they can only be used as parent classes (inherited from)","C. Only in JavaScript","D. Yes, if you provide arguments"],ans:1,exp:"The compiler will prevent you from instantiating an abstract class directly."},
      {q:"What is an 'abstract method'?",opts:["A. A method that is very fast","B. A method signature defined in an abstract class that MUST be implemented by any child class","C. A method that deletes itself","D. A private method"],ans:1,exp:"Abstract methods act like a strict contract for the child class."},
      {q:"If a class has common code that 10 subclasses need to share, but also requires each subclass to write a specific 'calculate()' function, what should you use?",opts:["A. An Interface","B. An Abstract Class","C. A global function","D. A struct"],ans:1,exp:"An abstract class is perfect here because it allows sharing concrete code while enforcing a contract for the 'calculate' method."},
      {q:"How does JavaScript (ES6) handle Abstract Classes?",opts:["A. Natively with the 'abstract' keyword","B. It doesn't have them natively, developers simulate them by throwing an error in the parent constructor if instantiated directly","C. It uses Interfaces instead","D. It removes them"],ans:1,exp:"In JS, you check 'new.target === ParentClass' and throw an error to mimic an abstract class."},
      {q:"Which keyword is used by a child class to call the parent's constructor?",opts:["A. call()","B. super()","C. parent()","D. init()"],ans:1,exp:"The 'super()' keyword invokes the constructor of the class being extended."}
    ],
    flows:[
      {title:"Abstract Implementation",items:["start:Define Abstract Shape","dec:Create new Shape()?","proc:(Error) Cannot instantiate","dec:Square extends Shape","proc:Square implements getArea()","end:new Square() works"]}
    ],
    game:{icon:"🏛️",title:"Half-Builder",desc:"Master abstract foundations",badges:["🏛️ Abstract Thinker","🛑 Constructor Blocker","✅ Implementer"],challenges:[{icon:"📝",title:"Simulate",desc:"Simulate an abstract class in JS",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Abstract Worker",badge:"Manager",desc:"Create a base worker class that forces specific jobs.",tags:["OOP","Abstraction"],steps:[{title:"Base Class",desc:"Create Worker with a concrete clockIn() method"},{"title:"Error Throw",desc:"Create doWork() that throws 'Must implement'"},{"title:"Subclass",desc:"Create Developer that overrides doWork()"}],code:`class Worker {\n  constructor() {\n    if (new.target === Worker) throw new Error("Abstract class");\n  }\n  clockIn() { console.log("Clocked in"); }\n  doWork() { throw new Error("Method not implemented"); }\n}\n\nclass Developer extends Worker {\n  doWork() { console.log("Writing code"); }\n}\n\nlet dev = new Developer();\ndev.clockIn();\ndev.doWork();`}
  },
  t23: {
    tag:'Phase 1 · OOP', num:23,
    title:'Method Overloading',
    desc:'Defining multiple methods with the same name but different parameters within the same class.',
    theory:`<div class="card"><h3>🏋️ Static Polymorphism</h3><p><strong>Method Overloading</strong> allows a single class to have multiple methods with the exact same name, as long as their parameter lists (signatures) are different. <em>Note: Java, C#, and C++ support this natively. JavaScript/Python do not.</em></p><h4>Why use it?</h4><p>It provides a cleaner API. Instead of having <code>addTwoInts(a, b)</code> and <code>addThreeInts(a, b, c)</code>, you just have <code>add()</code>, and the compiler figures out which one to use based on what you pass in.</p><div class="cb"><span class="cm">// Java Syntax</span>
<span class="ck">class</span> <span class="cv">MathUtil</span> {
    <span class="cm">// Overload 1</span>
    <span class="ck">int</span> add(<span class="ck">int</span> a, <span class="ck">int</span> b) { <span class="ck">return</span> a + b; }
    
    <span class="cm">// Overload 2 (Different parameters)</span>
    <span class="ck">int</span> add(<span class="ck">int</span> a, <span class="ck">int</span> b, <span class="ck">int</span> c) { <span class="ck">return</span> a + b + c; }
    
    <span class="cm">// Overload 3 (Different types)</span>
    <span class="ck">double</span> add(<span class="ck">double</span> a, <span class="ck">double</span> b) { <span class="ck">return</span> a + b; }
}</div></div>`,
    mcqs:[
      {q:"What is Method Overloading?",opts:["A. A child class replacing a parent's method","B. Having multiple methods in the SAME class with the SAME name, but DIFFERENT parameter lists","C. Calling a method too fast","D. Hiding private variables"],ans:1,exp:"Overloading relies on changing the method signature (number or type of arguments)."},
      {q:"How does the compiler know which overloaded method to call?",opts:["A. It runs them all and picks the best one","B. It looks at the number, type, and order of the arguments passed during the call","C. It guesses randomly","D. It asks the OS"],ans:1,exp:"This is called 'Compile-time polymorphism' or 'Static Dispatch'."},
      {q:"Does vanilla JavaScript support native Method Overloading?",opts:["A. Yes","B. No, JS dynamically types parameters. If you write two methods with the same name, the last one overwrites the first.","C. Only in Node.js","D. Only if you use 'const'"],ans:1,exp:"In JS, you simulate overloading by checking the `arguments` length or types inside a single method."},
      {q:"What is a Method Signature?",opts:["A. The name of the method and the types/order of its parameters","B. The return type of the method","C. The comments above the method","D. The code inside the method block"],ans:0,exp:"Signatures are how the compiler distinguishes overloaded methods."},
      {q:"Can you overload a method just by changing its return type (in Java)?",opts:["A. Yes","B. No, the parameter list MUST be different. Changing only the return type causes an error.","C. Only for Strings","D. Only if it is private"],ans:1,exp:"The compiler cannot determine which method to call based solely on what the method intends to return."}
    ],
    flows:[
      {title:"Compile-Time Resolution",items:["start:Call add(1, 2, 3)","dec:Find matching signature?","proc:Matches add(int, int, int)","proc:Binds to Overload 2","end:Executes"]}
    ],
    game:{icon:"🏋️",title:"Heavy Lifter",desc:"Master static polymorphism",badges:["🏋️ Overloader","✍️ Signature Pro","🦆 JS Simulator"],challenges:[{icon:"📝",title:"Simulate in JS",desc:"Write a JS function that checks arguments.length",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"JS Overload Sim",badge:"Faker",desc:"Simulate overloading in JavaScript.",tags:["JavaScript","Polymorphism"],steps:[{title:"Single Method",desc:"Create print()"},{"title:"Argument Check",desc:"Check if arguments.length === 1 or 2"},{"title:"Branch Logic",desc:"Execute different code based on count"}],code:`class Printer {\n  print() {\n    if (arguments.length === 1) {\n      console.log("Printing 1: " + arguments[0]);\n    } else if (arguments.length === 2) {\n      console.log("Printing 2: " + arguments[0] + ", " + arguments[1]);\n    }\n  }\n}\n\nlet p = new Printer();\np.print("A");\np.print("A", "B");`}
  },
  t24: {
    tag:'Phase 1 · OOP', num:24,
    title:'Method Overriding',
    desc:'Providing a specific implementation in a subclass for a method that is already defined in its superclass.',
    theory:`<div class="card"><h3>🎭 Dynamic Polymorphism</h3><p><strong>Method Overriding</strong> happens when a Child class decides it doesn't want the exact behavior of its Parent's method, so it writes its own version with the <strong>exact same name and signature</strong>.</p><h4>Why use it?</h4><p>It allows for highly specific behavior while maintaining a generic interface. (e.g., Every <code>Enemy</code> has an <code>attack()</code> method, but a <code>Dragon</code> overriding it breathes fire, while a <code>Goblin</code> stabs).</p><div class="cb"><span class="cm">// JavaScript Syntax</span>
<span class="ck">class</span> <span class="cv">Enemy</span> {
    attack() { console.log(<span class="cs">"Generic punch"</span>); }
}

<span class="ck">class</span> <span class="cv">Dragon</span> <span class="ck">extends</span> Enemy {
    <span class="cm">// Overriding the parent's method</span>
    attack() { 
        <span class="ck">super</span>.attack(); <span class="cm">// Can optionally call parent first</span>
        console.log(<span class="cs">"Breathes fire!"</span>); 
    }
}</div></div>`,
    mcqs:[
      {q:"What is the main difference between Overloading and Overriding?",opts:["A. They are the same","B. Overloading happens in the SAME class (different params). Overriding happens in a CHILD class (same params).","C. Overloading is for Java, Overriding is for JS","D. Overriding is faster"],ans:1,exp:"Overloading = Static polymorphism. Overriding = Dynamic polymorphism."},
      {q:"If a child overrides a parent method, how can the child still call the original parent method?",opts:["A. It's impossible, it's gone forever","B. By using the 'super' keyword (e.g., super.methodName())","C. By using 'parent'","D. By creating a new object"],ans:1,exp:"'super' allows you to invoke the superclass's implementation before or after your specific logic."},
      {q:"What happens at runtime when you call an overridden method on an object?",opts:["A. The OS crashes","B. Dynamic Dispatch ensures the most specific version (the child's version) is executed","C. Both the parent and child run automatically","D. The compiler throws a warning"],ans:1,exp:"The runtime checks the actual object type and calls its specific overridden method."},
      {q:"Can you override a 'final' method (in Java)?",opts:["A. Yes","B. No, the 'final' keyword explicitly prevents subclasses from overriding the method","C. Only if you use 'super'","D. Only in abstract classes"],ans:1,exp:"'final' is a security/design measure to lock down a method's behavior."},
      {q:"In JS, if you don't override a parent's method, what happens when you call it on the child?",opts:["A. An error occurs","B. The engine walks up the Prototype Chain and executes the parent's method","C. It does nothing","D. It returns undefined"],ans:1,exp:"The prototype chain resolves method calls by looking up the inheritance tree."}
    ],
    flows:[
      {title:"Prototype Lookup (JS)",items:["start:Call dragon.attack()","dec:Does Dragon have attack()?","proc:(Yes) Execute Dragon's version","dec:(No) Walk up to Enemy","proc:Execute Enemy's version","end:Done"]}
    ],
    game:{icon:"🎭",title:"The Overrider",desc:"Master dynamic polymorphism",badges:["🎭 Overrider","👆 Super Caller","🔗 Chain Walker"],challenges:[{icon:"📝",title:"Call Parent",desc:"Use super to call a parent method",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Employee Hierarchy",badge:"HR Rep",desc:"Override a calculatePay method for different employee types.",tags:["OOP","Overriding"],steps:[{title:"Base Employee",desc:"calculatePay() returns base salary"},{"title:"Manager",desc:"Overrides to return salary + bonus"},{"title:"Super Call",desc:"Manager uses super.calculatePay() + 5000"}],code:`class Employee {\n  constructor(salary) { this.salary = salary; }\n  calculatePay() { return this.salary; }\n}\n\nclass Manager extends Employee {\n  calculatePay() {\n    // Use parent logic, add specific logic\n    return super.calculatePay() + 5000;\n  }\n}\n\nlet m = new Manager(50000);\nconsole.log(m.calculatePay()); // 55000`}
  },
  t25: {
    tag:'Phase 1 · OOP', num:25,
    title:'Composition vs Inheritance',
    desc:'The architectural debate between "Is-A" (Inheritance) and "Has-A" (Composition) relationships.',
    theory:`<div class="card"><h3>🧩 The Fragile Base Class Problem</h3><p>Inheritance creates an "Is-A" relationship (A Dog <em>is an</em> Animal). However, deep inheritance trees become rigid and fragile. If you change the base class, it breaks all subclasses.</p><h4>Composition to the Rescue</h4><p>Composition creates a "Has-A" relationship. Instead of inheriting behavior, an object is composed of smaller, independent objects that provide that behavior.</p><div class="cb"><span class="cm">// Inheritance (Rigid)</span>
<span class="ck">class</span> <span class="cv">FlyingCar</span> <span class="ck">extends</span> Car { ... } <span class="cm">// Wait, does it extend Plane or Car?</span>

<span class="cm">// Composition (Flexible)</span>
<span class="ck">class</span> <span class="cv">Vehicle</span> {
    constructor(engine, wings) {
        <span class="cs">this</span>.engine = engine; <span class="cm">// Has an engine</span>
        <span class="cs">this</span>.wings = wings;   <span class="cm">// Has wings</span>
    }
}</div><p>Rule of thumb: <strong>Favor Composition over Inheritance.</strong></p></div>`,
    mcqs:[
      {q:"What type of relationship does Inheritance represent?",opts:["A. Has-A","B. Is-A","C. Uses-A","D. Wants-A"],ans:1,exp:"A Cat 'is an' Animal. A Truck 'is a' Vehicle."},
      {q:"What type of relationship does Composition represent?",opts:["A. Is-A","B. Has-A","C. Belongs-To","D. Works-With"],ans:1,exp:"A Car 'has an' Engine. A Player 'has an' Inventory."},
      {q:"What is the 'Gorilla Banana' problem with Inheritance?",opts:["A. You want a banana, but you get a gorilla holding the banana and the entire jungle","B. Gorillas eat bananas","C. Code is too slow","D. It causes memory leaks"],ans:0,exp:"When you inherit a class, you inherit its entire massive dependency tree, even if you only wanted one small function."},
      {q:"Why is Composition generally favored over Inheritance?",opts:["A. It's faster to compile","B. It's more flexible, easier to test, and avoids deep rigid class hierarchies","C. It uses less RAM","D. It's an older technique"],ans:1,exp:"Composition allows you to plug-and-play different behaviors without being locked into a strict family tree."},
      {q:"If a robot can 'Walk', 'Talk', and 'Shoot', how would you design this using Composition?",opts:["A. Create a Robot class that extends Walker, Talker, and Shooter","B. Create separate Leg, Speaker, and Gun classes, and pass them into the Robot constructor","C. Write a 10,000 line Robot class","D. Use an Interface"],ans:1,exp:"The Robot 'has' legs, 'has' a speaker, and 'has' a gun. You compose the robot from these modular parts."}
    ],
    flows:[
      {title:"Inheritance vs Composition",items:["start:Goal: Flying Car","dec:Inheritance (Fails)","proc:Cannot extend both Car and Plane","dec:Composition (Succeeds)","proc:Has an Engine (Car)","proc:Has Wings (Plane)","end:Done"]}
    ],
    game:{icon:"🧩",title:"Architect",desc:"Master class relationships",badges:["🦍 Gorilla Tamer","🧩 Composer","🧱 Modularizer"],challenges:[{icon:"📝",title:"Compose",desc:"Build a class using two other classes",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Robot Assembler",badge:"Engineer",desc:"Use composition to build a robot with interchangeable parts.",tags:["Architecture","Composition"],steps:[{title:"Modules",desc:"Create Motor and Laser classes"},{"title:"Assembly",desc:"Create Robot class that takes motor and laser in constructor"},{"title:"Execute",desc:"Call robot.motor.drive() and robot.laser.fire()"}],code:`class Motor { drive() { console.log("Vroom"); } }\nclass Laser { fire() { console.log("Pew pew"); } }\n\nclass Robot {\n  constructor(motor, laser) {\n    this.motor = motor;\n    this.laser = laser;\n  }\n  action() {\n    this.motor.drive();\n    this.laser.fire();\n  }\n}\n\nlet bot = new Robot(new Motor(), new Laser());\nbot.action();`}
  },
  t26: {
    tag:'Phase 1 · OOP', num:26,
    title:'SOLID Principles',
    desc:'Five foundational design principles to make software designs more understandable, flexible, and maintainable.',
    theory:`<div class="card"><h3>🏛️ The Rules of Clean Architecture</h3><p>Coined by "Uncle Bob" Martin, SOLID is the gold standard for OOP design.</p><ul><li><strong>S - Single Responsibility:</strong> A class should have one, and only one, reason to change (do one thing well).</li><li><strong>O - Open/Closed:</strong> Classes should be open for extension (inheritance/composition) but closed for modification (don't edit the core file).</li><li><strong>L - Liskov Substitution:</strong> If you replace a Parent class with a Child class, the program should not break.</li><li><strong>I - Interface Segregation:</strong> Don't force a class to implement an interface with methods it doesn't need. (Split big interfaces into small ones).</li><li><strong>D - Dependency Inversion:</strong> High-level modules should not depend on low-level modules; both should depend on abstractions (Interfaces).</li></ul></div>`,
    mcqs:[
      {q:"What does the 'S' in SOLID stand for?",opts:["A. Static Typing","B. Single Responsibility Principle","C. Superclass","D. System Design"],ans:1,exp:"A class should do one thing. Don't put DB logic and UI logic in the same class."},
      {q:"What does the Open/Closed Principle mean?",opts:["A. Files should be open to the public","B. Software entities should be open for extension, but closed for modification","C. Databases should be closed","D. APIs should be open"],ans:1,exp:"You should be able to add new functionality (like a new payment method) by writing new code, not altering existing core code."},
      {q:"Liskov Substitution Principle states that:",opts:["A. Objects of a superclass should be replaceable with objects of its subclasses without breaking the application","B. You should substitute variables often","C. You must use Liskov language","D. Inheritance is bad"],ans:0,exp:"If a function expects a 'Bird', passing a 'Penguin' (which extends Bird) should not cause the function to crash if it calls .fly()."},
      {q:"If an Interface has 20 methods, and a class only needs 2 of them, which principle is violated?",opts:["A. Dependency Inversion","B. Single Responsibility","C. Interface Segregation Principle","D. Open/Closed"],ans:2,exp:"Interface Segregation dictates that large, fat interfaces should be split into smaller, specific ones so clients aren't forced to implement useless methods."},
      {q:"Dependency Inversion means you should depend on:",opts:["A. Concrete classes (like MySQLDatabase)","B. Abstractions/Interfaces (like IDatabase)","C. Global variables","D. NPM packages"],ans:1,exp:"If your high-level logic depends on an Interface, you can easily swap out MySQL for MongoDB without changing the high-level code."}
    ],
    flows:[
      {title:"Dependency Inversion Flow",items:["start:App Logic","dec:Depends On ->","proc:IDatabase (Interface)","dec:Implemented By ->","proc:MySQL Class","proc:Mongo Class","end:App logic never touches DB code directly"]}
    ],
    game:{icon:"🏛️",title:"Uncle Bob",desc:"Master the SOLID principles",badges:["📐 Architect","✂️ Segregator","🔌 Inverter"],challenges:[{icon:"📝",title:"Identify S",desc:"Spot a Single Responsibility violation",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Refactoring to 'S'",badge:"Refactorer",desc:"Split a monolithic class into two responsible classes.",tags:["Architecture","SOLID"],steps:[{title:"Monolith",desc:"Identify a class doing DB saves and Email sending"},{"title:"Split DB",desc:"Create UserRepository class"},{"title:"Split Email",desc:"Create EmailService class"}],code:`// BAD: Violates SRP\nclass User {\n  saveToDb() { /* sql */ }\n  sendWelcomeEmail() { /* smtp */ }\n}\n\n// GOOD: SRP Applied\nclass UserRepository {\n  save(user) { /* sql */ }\n}\nclass EmailService {\n  sendWelcome(user) { /* smtp */ }\n}`}
  },
"""

start_marker = "};\n\nlet userXP"
inject_idx = content.find(start_marker)

if inject_idx != -1:
    new_content = content[:inject_idx] + ",\n" + rich_content + content[inject_idx:]
    with open(html_path, "w") as f:
        f.write(new_content)
    print("Successfully generated T22-T26 rich content!")
else:
    print("Could not find injection point.")
