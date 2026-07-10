import re

html_path = "/Users/bhoomim/devops CI:CD/handbook/fullstack_ai_handbook.html"
with open(html_path, "r") as f:
    content = f.read()

rich_content = """
  t14: {
    tag:'Phase 1 · OOP', num:14,
    title:'Classes',
    desc:'The blueprint for creating objects in Object-Oriented Programming.',
    theory:`<div class="card"><h3>🏛️ The Blueprint of Data</h3><p>A <strong>Class</strong> is a template or blueprint that defines the properties (data/state) and methods (behavior) that objects created from it will have.</p><h4>Why use Classes?</h4><ul><li><strong>Organization:</strong> Groups related data and functions together.</li><li><strong>Reusability:</strong> Write the blueprint once, create thousands of instances from it.</li></ul><div class="cb"><span class="cm">// JavaScript Class Example</span>
<span class="ck">class</span> <span class="cv">Car</span> {
    <span class="cm">// Properties and methods go here</span>
    startEngine() {
        console.log(<span class="cs">"Vroom!"</span>);
    }
}</div></div>`,
    mcqs:[
      {q:"What is the best real-world analogy for a Class?",opts:["A. A physical car you can drive","B. The factory blueprint used to build the car","C. The gas inside the car","D. The road"],ans:1,exp:"A Class is the abstract blueprint. An Object is the actual instance built from it."},
      {q:"In OOP, what do we call the 'functions' that belong to a class?",opts:["A. Properties","B. Methods","C. Variables","D. Pointers"],ans:1,exp:"Functions attached to a class are called Methods. Variables are called Properties or Attributes."},
      {q:"What does a Class group together?",opts:["A. HTML and CSS","B. State (Properties) and Behavior (Methods)","C. Databases and APIs","D. Numbers and Strings"],ans:1,exp:"Classes encapsulate data and the operations that modify that data into a single entity."},
      {q:"Is a Class stored in the Heap or the Stack?",opts:["A. Heap","B. Stack","C. Neither (It's a definition, not an instance)","D. Both"],ans:2,exp:"The class definition itself is part of the code/metaspace. Instances (objects) created from the class are stored in the Heap."},
      {q:"What keyword is used to declare a class in most modern languages?",opts:["A. object","B. struct","C. class","D. create"],ans:2,exp:"'class' is the universal keyword in Java, C++, JS, Python, etc."}
    ],
    flows:[
      {title:"From Blueprint to Instance",items:["start:Define Class (Blueprint)","proc:Call new Class()","proc:Allocate Memory in Heap","end:Return Object Instance"]}
    ],
    game:{icon:"🏛️",title:"Architect",desc:"Master class creation",badges:["🏛️ Blueprint Drawer","🧩 Organizer","🛠️ Method Maker"],challenges:[{icon:"📝",title:"Draft a Class",desc:"Write an empty User class",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"RPG Character Blueprint",badge:"Game Dev",desc:"Create a base class for an RPG game.",tags:["OOP","Classes"],steps:[{title:"Define Class",desc:"Create a class called Player"},{title:"Add Method",desc:"Add a method called attack()"},{title:"Test",desc:"Instantiate and call attack()"}],code:`class Player {\n  attack() {\n    console.log("Player swung their sword!");\n  }\n}\n\nlet p1 = new Player();\np1.attack();`}
  },
  t15: {
    tag:'Phase 1 · OOP', num:15,
    title:'Objects',
    desc:'Instances created from a Class blueprint, containing actual data and state.',
    theory:`<div class="card"><h3>🏎️ The Physical Instance</h3><p>An <strong>Object</strong> is a concrete instance of a Class. While a Class is just an idea, an Object exists in the computer's memory (the Heap) and holds actual values.</p><h4>Instantiation</h4><p>You create an object using the <code>new</code> keyword.</p><div class="cb"><span class="cm">// Using the Car class from before</span>
<span class="ck">let</span> <span class="cv">myHonda</span> = <span class="ck">new</span> Car(); 
myHonda.startEngine(); <span class="cm">// Output: Vroom!</span></div><div class="box b-vi"><h5>💡 Multiple Instances</h5><p>You can create 100 <code>Car</code> objects. They all share the same methods (startEngine), but they can have different states (color, mileage).</p></div></div>`,
    mcqs:[
      {q:"What is an Object in the context of OOP?",opts:["A. A primitive data type","B. A concrete instance created from a Class blueprint","C. A database table","D. The blueprint itself"],ans:1,exp:"The class is the blueprint, the object is the actual house built from it."},
      {q:"What keyword is traditionally used to create a new Object from a Class?",opts:["A. create","B. init","C. new","D. object"],ans:2,exp:"The 'new' keyword tells the system to allocate heap memory and run the constructor."},
      {q:"If you create two objects from the same class, do they share the exact same memory address?",opts:["A. Yes","B. No, each object gets its own unique space in the Heap","C. Only in Java","D. Yes, if they have the same properties"],ans:1,exp:"Each instantiation allocates a brand new, distinct block of memory."},
      {q:"What is 'State' in an object?",opts:["A. The functions it can run","B. The current values of its properties (e.g., color='red', speed=50)","C. The OS it runs on","D. Whether it is deleted or not"],ans:1,exp:"State refers to the data held by the object at any given moment."},
      {q:"How do you access a method inside an object named 'myCar'?",opts:["A. myCar->method()","B. myCar.method() (Dot notation)","C. method(myCar)","D. myCar[method]"],ans:1,exp:"Dot notation is the standard way to access properties and methods of an object."}
    ],
    flows:[
      {title:"Object Memory Allocation",items:["start:let a = new Car()","proc:Heap reserves space for Car properties","proc:Stack variable 'a' points to Heap","end:Done"]}
    ],
    game:{icon:"🏎️",title:"Instance Initiator",desc:"Master object instantiation",badges:["🏎️ Instance Creator","📦 State Holder","🎯 Dot Notator"],challenges:[{icon:"📝",title:"Instantiate",desc:"Create two instances of a class",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Object Factory",badge:"Factory Worker",desc:"Create multiple unique objects from a single class.",tags:["OOP","Objects"],steps:[{title:"Define Class",desc:"Create Dog class with a bark method"},{title:"Create Instances",desc:"Make dog1 and dog2 using 'new Dog()'"},{title:"Call Methods",desc:"Call bark() on both"}],code:`class Dog {\n  bark() {\n    console.log("Woof!");\n  }\n}\n\nlet dog1 = new Dog();\nlet dog2 = new Dog();\n\ndog1.bark();\ndog2.bark();`}
  },
  t16: {
    tag:'Phase 1 · OOP', num:16,
    title:'Constructors',
    desc:'Special methods invoked automatically when an object is created to initialize its state.',
    theory:`<div class="card"><h3>🏗️ Setting Up the Object</h3><p>A <strong>Constructor</strong> is a special method inside a class. Its sole purpose is to initialize the object's properties at the exact moment it is created.</p><h4>The <code>this</code> keyword</h4><p>Inside the constructor, the keyword <code>this</code> refers to the <em>specific object</em> being created right now.</p><div class="cb"><span class="ck">class</span> <span class="cv">Car</span> {
    constructor(make, model) {
        <span class="cs">this</span>.make = make;   <span class="cm">// Initialize state</span>
        <span class="cs">this</span>.model = model;
    }
}
<span class="cm">// The arguments are passed directly into the constructor</span>
<span class="ck">let</span> <span class="cv">myCar</span> = <span class="ck">new</span> Car(<span class="cs">"Honda"</span>, <span class="cs">"Civic"</span>);</div></div>`,
    mcqs:[
      {q:"When is a constructor function executed?",opts:["A. Every time a method is called","B. When the program ends","C. Automatically, the exact moment an object is instantiated with the 'new' keyword","D. Only when manually called"],ans:2,exp:"Constructors run immediately upon creation to set up the object."},
      {q:"What is the primary purpose of a constructor?",opts:["A. To delete the object","B. To initialize the object's properties (state) with provided arguments","C. To connect to a database","D. To return a string"],ans:1,exp:"Constructors take the arguments passed into the 'new' call and assign them to the object's internal state."},
      {q:"Inside a class, what does the keyword 'this' (or 'self' in Python) refer to?",opts:["A. The Class blueprint itself","B. The specific object instance that is currently executing the code","C. The global window object","D. The parent class"],ans:1,exp:"'this' allows you to attach data specifically to the object being built, not the generic blueprint."},
      {q:"Can a class have multiple constructors? (In languages like Java)",opts:["A. Yes, through Constructor Overloading","B. No, only one is allowed","C. Yes, but they must have the same arguments","D. No, it causes a crash"],ans:0,exp:"Languages like Java allow multiple constructors as long as their parameter lists (signatures) are different (Overloading)."},
      {q:"If you do not write a constructor in your class, what happens?",opts:["A. The program crashes when you use 'new'","B. The compiler provides a default empty constructor automatically","C. You can't create objects","D. It throws a Syntax Error"],ans:1,exp:"Most OOP languages inject a hidden, empty default constructor if you don't define one."}
    ],
    flows:[
      {title:"Constructor Execution Flow",items:["start:new Car('Honda')","proc:Allocate Heap Memory","proc:Call constructor('Honda')","proc:Set this.make = 'Honda'","end:Return Object"]}
    ],
    game:{icon:"🏗️",title:"State Setter",desc:"Master object initialization",badges:["🏗️ Builder","🧩 Initializer","👈 'This' Master"],challenges:[{icon:"📝",title:"Write a Constructor",desc:"Initialize 3 properties",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Custom Character Builder",badge:"RPG Smith",desc:"Use constructors to dynamically generate unique characters.",tags:["OOP","Constructors"],steps:[{title:"Class Setup",desc:"Create Character class with constructor(name, hp)"},{title:"Initialization",desc:"Assign this.name = name, this.hp = hp"},{title:"Instantiate",desc:"Create a Warrior (100 HP) and Mage (50 HP)"}],code:`class Character {\n  constructor(name, hp) {\n    this.name = name;\n    this.hp = hp;\n  }\n}\n\nlet warrior = new Character("Thor", 150);\nlet mage = new Character("Merlin", 60);\n\nconsole.log(warrior.name + " has " + warrior.hp + " HP.");`}
  },
  t17: {
    tag:'Phase 1 · OOP', num:17,
    title:'Encapsulation',
    desc:'Bundling data and methods together, and restricting direct access to the data.',
    theory:`<div class="card"><h3>🛡️ Protecting the State</h3><p>Encapsulation is one of the 4 pillars of OOP. It means hiding the internal state of an object and requiring all interaction to be performed through an object's methods.</p><h4>Access Modifiers</h4><ul><li><strong>Public:</strong> Accessible from anywhere.</li><li><strong>Private:</strong> Accessible <em>only</em> from within the class itself. Prevents outside code from messing up internal logic.</li></ul><div class="cb"><span class="ck">class</span> <span class="cv">BankAccount</span> {
    <span class="cm">// Private field (JS syntax)</span>
    #balance = <span class="cs">0</span>;

    <span class="cm">// Public method to safely interact with private data</span>
    deposit(amount) {
        <span class="ck">if</span> (amount > <span class="cs">0</span>) <span class="cs">this</span>.#balance += amount;
    }
    
    getBalance() {
        <span class="ck">return</span> <span class="cs">this</span>.#balance;
    }
}</div><p>Without encapsulation, anyone could do <code>account.balance = 1000000;</code> directly! Encapsulation forces them to use the <code>deposit()</code> method, which can contain validation logic.</p></div>`,
    mcqs:[
      {q:"What is the primary goal of Encapsulation?",opts:["A. To make code run faster","B. To hide internal data state and restrict access to it, protecting it from invalid external changes","C. To inherit properties from another class","D. To connect to a database"],ans:1,exp:"Encapsulation acts as a protective shield around your object's data."},
      {q:"What access modifier makes a property accessible ONLY from inside its own class?",opts:["A. public","B. protected","C. private","D. static"],ans:2,exp:"Private properties cannot be read or modified by external code."},
      {q:"If a variable is private, how does external code interact with it?",opts:["A. It can't at all","B. Through public getter and setter methods","C. By hacking the compiler","D. By making the class public"],ans:1,exp:"Getters and setters (methods) act as the controlled gateway to private data."},
      {q:"Why not just make all properties public?",opts:["A. It's too slow","B. It uses too much memory","C. It violates data integrity; external code could set an 'age' property to -500","D. It causes infinite loops"],ans:2,exp:"Encapsulation allows you to add validation logic (e.g., 'if age < 0 throw error') inside the setter method."},
      {q:"Which OOP pillar does 'Information Hiding' refer to?",opts:["A. Polymorphism","B. Inheritance","C. Abstraction","D. Encapsulation"],ans:3,exp:"Information Hiding is the core concept of Encapsulation."}
    ],
    flows:[
      {title:"Encapsulated Access",items:["start:External Code","proc:Call object.setAge(-5)","proc:Setter checks (val > 0)","proc:(Fails) Reject change","end:Internal State Protected"]}
    ],
    game:{icon:"🛡️",title:"Data Defender",desc:"Master data protection",badges:["🛡️ Shield Wall","🔒 Privatizer","🚪 Gateway Master"],challenges:[{icon:"📝",title:"Make it Private",desc:"Define a private variable",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Secure Bank Vault",badge:"Security Guard",desc:"Use encapsulation to protect a bank balance from direct modification.",tags:["OOP","Encapsulation"],steps:[{title:"Private Balance",desc:"Create a class with a private #balance"},{title:"Getter",desc:"Add getBalance()"},{title:"Setter with Logic",desc:"Add deposit(amount) that rejects negative numbers"}],code:`class Vault {\n  #balance = 0;\n\n  deposit(amount) {\n    if (amount <= 0) {\n      console.log("Invalid amount");\n      return;\n    }\n    this.#balance += amount;\n  }\n\n  getBalance() {\n    return this.#balance;\n  }\n}\n\nlet v = new Vault();\nv.deposit(50);\nconsole.log(v.getBalance());`}
  },
"""

start_marker = "};\n\nlet userXP"
inject_idx = content.find(start_marker)

if inject_idx != -1:
    new_content = content[:inject_idx] + ",\n" + rich_content + content[inject_idx:]
    with open(html_path, "w") as f:
        f.write(new_content)
    print("Successfully generated T14-T17 rich content!")
else:
    print("Could not find injection point.")
