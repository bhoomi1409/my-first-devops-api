import re

html_path = "/Users/bhoomim/devops CI:CD/handbook/fullstack_ai_handbook.html"
with open(html_path, "r") as f:
    content = f.read()

rich_content = """
  t18: {
    tag:'Phase 1 · OOP', num:18,
    title:'Inheritance',
    desc:'Creating a new class based on an existing class to promote code reuse.',
    theory:`<div class="card"><h3>🧬 Passing Down the Genes</h3><p>Inheritance allows a new class (<strong>Child / Subclass</strong>) to inherit properties and methods from an existing class (<strong>Parent / Superclass</strong>).</p><h4>Why use it?</h4><p>Instead of copy-pasting the same code for a <code>Dog</code> class and a <code>Cat</code> class, you put the shared code in an <code>Animal</code> class, and make Dog and Cat inherit from it. (DRY - Don't Repeat Yourself).</p><div class="cb"><span class="cm">// Parent Class</span>
<span class="ck">class</span> <span class="cv">Animal</span> {
    eat() { console.log(<span class="cs">"Munch munch"</span>); }
}

<span class="cm">// Child Class inherits using 'extends'</span>
<span class="ck">class</span> <span class="cv">Dog</span> <span class="ck">extends</span> Animal {
    bark() { console.log(<span class="cs">"Woof!"</span>); }
}

<span class="ck">let</span> <span class="cv">d</span> = <span class="ck">new</span> Dog();
d.eat();  <span class="cm">// Inherited!</span>
d.bark(); <span class="cm">// Specific to Dog</span></div></div>`,
    mcqs:[
      {q:"What is the primary benefit of Inheritance?",opts:["A. It makes the code run faster","B. Code reuse (DRY principle) by sharing common logic in a parent class","C. It hides data","D. It connects to the database"],ans:1,exp:"Inheritance prevents code duplication by centralizing shared behavior in a superclass."},
      {q:"What keyword is commonly used to establish inheritance in languages like Java and JS?",opts:["A. implements","B. inherits","C. extends","D. super"],ans:2,exp:"'extends' is the standard keyword to create a subclass (e.g., class Dog extends Animal)."},
      {q:"Can a Child class access private properties of the Parent class?",opts:["A. Yes, always","B. No, private properties belong strictly to the class they are defined in","C. Only in Python","D. Yes, if you use the 'super' keyword"],ans:1,exp:"Private properties are truly private. (Though 'protected' properties can be accessed by subclasses in languages like Java)."},
      {q:"What is a 'Superclass'?",opts:["A. A class with more than 1000 lines of code","B. The parent class being inherited from","C. A class that has no parent","D. The final object"],ans:1,exp:"Superclass = Parent. Subclass = Child."},
      {q:"If 'Car' inherits from 'Vehicle', and 'Vehicle' has a drive() method, can an instance of 'Car' call drive()?",opts:["A. Yes, it inherits the method automatically","B. No, you must rewrite it in Car","C. Only if Car is public","D. No, it throws an error"],ans:0,exp:"The subclass inherits all public and protected methods of the superclass."}
    ],
    flows:[
      {title:"Inheritance Hierarchy",items:["start:Animal (eat, sleep)","dec:Inherits To ->","proc:Dog (bark)","proc:Cat (meow)","end:Dog has (eat, sleep, bark)"]}
    ],
    game:{icon:"🧬",title:"Gene Splicer",desc:"Master class inheritance",badges:["🧬 Inheritor","👨‍👦 Parent/Child","🔁 DRY Master"],challenges:[{icon:"📝",title:"Extend it",desc:"Make a Penguin class extend Bird",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Vehicle Fleet",badge:"Mechanic",desc:"Create a hierarchy of vehicles sharing common startEngine logic.",tags:["OOP","Inheritance"],steps:[{title:"Parent Class",desc:"Create Vehicle with start()"},{"title:"Child Classes",desc:"Create Car and Truck extending Vehicle"},{"title:"Specific Methods",desc:"Give Truck a loadCargo() method"}],code:`class Vehicle {\n  start() { console.log("Engine started"); }\n}\n\nclass Truck extends Vehicle {\n  loadCargo() { console.log("Loading boxes"); }\n}\n\nlet t = new Truck();\nt.start(); // Inherited\nt.loadCargo();`}
  },
  t19: {
    tag:'Phase 1 · OOP', num:19,
    title:'Polymorphism',
    desc:'The ability of different objects to respond to the same method call in their own unique way.',
    theory:`<div class="card"><h3>🎭 Many Forms</h3><p>Polymorphism (from Greek: "many forms") allows you to treat objects of different classes as if they were objects of a common parent class. It allows a single function name to behave differently depending on the object it is called on.</p><h4>Method Overriding</h4><p>A child class can provide its own specific implementation of a method that is already provided by its parent.</p><div class="cb"><span class="ck">class</span> <span class="cv">Animal</span> {
    makeSound() { console.log(<span class="cs">"Generic sound"</span>); }
}
<span class="ck">class</span> <span class="cv">Dog</span> <span class="ck">extends</span> Animal {
    <span class="cm">// Overriding the parent's method</span>
    makeSound() { console.log(<span class="cs">"Woof!"</span>); } 
}
<span class="ck">class</span> <span class="cv">Cat</span> <span class="ck">extends</span> Animal {
    <span class="cm">// Overriding the parent's method</span>
    makeSound() { console.log(<span class="cs">"Meow!"</span>); }
}

<span class="cm">// Polymorphism in action:</span>
<span class="ck">let</span> <span class="cv">pets</span> = [<span class="ck">new</span> Dog(), <span class="ck">new</span> Cat()];
pets.forEach(p => p.makeSound()); <span class="cm">// Woof! Meow!</span></div></div>`,
    mcqs:[
      {q:"What does Polymorphism literally mean?",opts:["A. Hiding data","B. Many forms","C. Code reuse","D. Single structure"],ans:1,exp:"Poly = many, morph = forms. It means one method name can take many forms depending on the object calling it."},
      {q:"What is Method Overriding?",opts:["A. Writing two methods with the exact same name in the same class","B. A subclass providing a specific implementation of a method that is already defined in its parent class","C. Deleting a method","D. Calling a method too many times"],ans:1,exp:"Overriding allows a child to change the behavior inherited from the parent."},
      {q:"Why is Polymorphism useful?",opts:["A. It makes the code execute faster","B. It allows you to write generic code that can process a list of different objects uniformly (e.g. calling .render() on all UI components)","C. It secures the database","D. It saves memory"],ans:1,exp:"You don't need to write 'if (type == dog) bark else if (type == cat) meow'. You just call makeSound()."},
      {q:"What is Method Overloading (common in Java/C++)?",opts:["A. A child class rewriting a parent method","B. Having multiple methods in the SAME class with the SAME name, but DIFFERENT parameters (e.g., add(int, int) vs add(int, int, int))","C. Crashing the stack","D. Using the 'overload' keyword"],ans:1,exp:"Overloading is compile-time polymorphism based on parameter signatures."},
      {q:"In the pets array example, what determines which makeSound() is executed?",opts:["A. The array length","B. The compiler","C. The actual object type at runtime (Dynamic Dispatch)","D. The OS"],ans:2,exp:"The runtime engine looks at the specific object (Dog or Cat) and calls its specific overridden method."}
    ],
    flows:[
      {title:"Dynamic Dispatch Flow",items:["start:Call p.makeSound()","dec:Is p a Dog?","proc:(Yes) Run Dog.makeSound()","dec:Is p a Cat?","proc:(Yes) Run Cat.makeSound()","end:Done"]}
    ],
    game:{icon:"🎭",title:"Shape Shifter",desc:"Master polymorphic behavior",badges:["🎭 Shape Shifter","📝 Overrider","🎯 Dispatcher"],challenges:[{icon:"📝",title:"Override",desc:"Override a parent method",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"UI Renderer",badge:"Frontend Fake",desc:"Use polymorphism to render different UI elements.",tags:["OOP","Polymorphism"],steps:[{title:"Base Class",desc:"Create UIComponent with render()"},{"title:"Subclasses",desc:"Create Button and Input extending UIComponent and overriding render()"},{"title:"Loop",desc:"Put them in an array and loop over them calling render()"}],code:`class UIComponent {\n  render() { console.log("Rendering component"); }\n}\nclass Button extends UIComponent {\n  render() { console.log("<button>Click</button>"); }\n}\nclass Input extends UIComponent {\n  render() { console.log("<input type='text'/>"); }\n}\n\nlet dom = [new Button(), new Input()];\ndom.forEach(el => el.render());`}
  },
  t20: {
    tag:'Phase 1 · OOP', num:20,
    title:'Abstraction',
    desc:'Hiding complex implementation details and showing only the essential features of the object.',
    theory:`<div class="card"><h3>🌫️ Hiding the Complexity</h3><p>Abstraction is about reducing complexity by hiding irrelevant details. When you drive a car, you use the steering wheel and pedals. You don't need to know the physics of internal combustion inside the engine.</p><h4>How is it achieved?</h4><ul><li><strong>Simple Interfaces:</strong> Providing simple public methods (like <code>startCar()</code>) while hiding complex private methods (like <code>injectFuel()</code>, <code>igniteSpark()</code>).</li><li><strong>Abstract Classes:</strong> Classes that cannot be instantiated directly, but serve as a strict template for subclasses.</li></ul><div class="box b-ro"><h5>Encapsulation vs Abstraction</h5><p><strong>Encapsulation</strong> is about <em>security</em> and hiding data state (using private variables). <strong>Abstraction</strong> is about <em>simplicity</em> and hiding complex logic to provide a clean API.</p></div></div>`,
    mcqs:[
      {q:"What is the primary goal of Abstraction?",opts:["A. To hide complex implementation details and provide a simple, clean interface to the user/developer","B. To secure variables from being changed","C. To inherit properties","D. To compile faster"],ans:0,exp:"Abstraction reduces cognitive load. You just call .connect() instead of dealing with TCP handshakes."},
      {q:"What is a good real-world example of Abstraction?",opts:["A. A blueprint of a house","B. A coffee machine: you press a button, it handles the grinding, heating, and pouring internally","C. A transparent glass","D. A lock box"],ans:1,exp:"The coffee machine abstracts away the complex mechanics behind a simple interface (the button)."},
      {q:"How does Abstraction differ from Encapsulation?",opts:["A. They are exactly the same","B. Encapsulation hides data (security); Abstraction hides complex logic/implementation (simplicity)","C. Encapsulation is for Java, Abstraction is for C++","D. Abstraction uses 'private', Encapsulation uses 'abstract'"],ans:1,exp:"Encapsulation restricts access to state. Abstraction provides a simplified high-level API."},
      {q:"What is an Abstract Class?",opts:["A. A class that is very hard to understand","B. A class that cannot be instantiated directly (using 'new') and is only meant to be subclassed","C. A class with no methods","D. A class that deletes itself"],ans:1,exp:"Abstract classes force you to create specific child classes (e.g. you can't create a generic 'Animal', you must create a 'Dog')."},
      {q:"If a public method calls 5 complex private helper methods internally, what is this an example of?",opts:["A. Inheritance","B. Polymorphism","C. Abstraction","D. Recursion"],ans:2,exp:"The complexity of the 5 helper methods is abstracted away behind a single, simple public method call."}
    ],
    flows:[
      {title:"The Abstraction Barrier",items:["start:User calls startEngine()","proc:(Barrier)","proc:Private: injectFuel()","proc:Private: igniteSpark()","end:Engine Starts"]}
    ],
    game:{icon:"🌫️",title:"Illusionist",desc:"Master complexity hiding",badges:["🌫️ Abstractor","🕹️ Interface Designer","🧩 Simplifier"],challenges:[{icon:"📝",title:"Hide It",desc:"Write a public method that hides 3 private ones",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Coffee Machine API",badge:"Barista",desc:"Abstract away the complex steps of making coffee.",tags:["OOP","Abstraction"],steps:[{title:"Complex Methods",desc:"Create private methods #grindBeans(), #boilWater(), #brew()"},{"title:"Simple API",desc:"Create a public makeCoffee() method that calls all three"}],code:`class CoffeeMachine {\n  #grindBeans() { console.log("Grinding..."); }\n  #boilWater() { console.log("Boiling..."); }\n  #brew() { console.log("Brewing..."); }\n\n  // The Abstracted, simple interface\n  makeCoffee() {\n    this.#grindBeans();\n    this.#boilWater();\n    this.#brew();\n    console.log("Coffee is ready!");\n  }\n}\n\nlet cm = new CoffeeMachine();\ncm.makeCoffee(); // Simple!`}
  },
  t21: {
    tag:'Phase 1 · OOP', num:21,
    title:'Interfaces',
    desc:'A contract that defines what methods a class must implement.',
    theory:`<div class="card"><h3>📜 The Contract</h3><p>An <strong>Interface</strong> is a strict contract. If a class claims to "implement" an interface, it <strong>must</strong> provide the code for all the methods defined in that interface.</p><h4>Why use Interfaces?</h4><p>They guarantee that certain classes will have specific behaviors, regardless of what parent class they inherit from. (Note: JavaScript does not have native Interfaces, but TypeScript and Java do).</p><div class="cb"><span class="cm">// TypeScript/Java Syntax</span>
<span class="ck">interface</span> <span class="cv">Flyable</span> {
    fly(): <span class="ck">void</span>;
}

<span class="cm">// The class MUST write the fly method, or it won't compile</span>
<span class="ck">class</span> <span class="cv">Bird</span> <span class="ck">implements</span> Flyable {
    fly() {
        console.log(<span class="cs">"Flapping wings!"</span>);
    }
}</div></div>`,
    mcqs:[
      {q:"What is an Interface?",opts:["A. A GUI (Graphical User Interface)","B. A strict contract specifying methods that a class MUST implement","C. A type of variable","D. A database connection string"],ans:1,exp:"An interface forces a class to write specific methods, guaranteeing that behavior exists."},
      {q:"Can you instantiate an Interface (e.g., new Flyable())?",opts:["A. Yes","B. No, interfaces have no implementation code, they are just definitions","C. Only in JavaScript","D. Yes, if you pass arguments"],ans:1,exp:"Interfaces are completely abstract. You can only instantiate classes that implement them."},
      {q:"What happens if a class implements an interface but forgets to write one of the required methods?",opts:["A. The program runs normally","B. The compiler throws an error and refuses to compile","C. It creates a warning but runs","D. The method is auto-generated"],ans:1,exp:"The contract is broken, so statically typed languages (Java, TS, C#) will throw a compilation error."},
      {q:"How does an Interface differ from an Abstract Class? (In Java)",opts:["A. They are identical","B. Abstract classes can contain actual code (implementation) for some methods, while Interfaces traditionally only contain method signatures (no code)","C. Interfaces are faster","D. Interfaces can hold state variables"],ans:1,exp:"Abstract classes can share common code. Interfaces only define the 'what', not the 'how'."},
      {q:"Does vanilla JavaScript have native Interfaces?",opts:["A. Yes","B. No, JavaScript relies on Duck Typing. TypeScript adds Interfaces.","C. Only in ES5","D. Yes, using the 'interface' keyword"],ans:1,exp:"JavaScript does not have strict interfaces at runtime. TypeScript provides them at compile time."}
    ],
    flows:[
      {title:"Interface Contract Flow",items:["start:Interface Flyable (requires fly)","dec:Class Bird implements Flyable","dec:Does Bird have fly() method?","proc:(Yes) Compiles Successfully","proc:(No) Compiler Error!","end:Done"]}
    ],
    game:{icon:"📜",title:"Contractor",desc:"Master class contracts",badges:["📜 Signatory","🦆 Duck Typer","✅ Implementer"],challenges:[{icon:"📝",title:"Implement",desc:"Write a class implementing a logger interface",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Payment Gateway Contract",badge:"Banker",desc:"Define an interface for payment processors (Conceptual TS).",tags:["TypeScript","Interfaces"],steps:[{title:"Interface",desc:"Define IPayable with pay(amount)"},{"title:"Implementation 1",desc:"Create Stripe class that implements it"},{"title:"Implementation 2",desc:"Create PayPal class that implements it"}],code:`// TypeScript Example\ninterface IPayable {\n  pay(amount: number): void;\n}\n\nclass Stripe implements IPayable {\n  pay(amount: number) {\n    console.log("Paid $" + amount + " via Stripe");\n  }\n}\n\nclass PayPal implements IPayable {\n  pay(amount: number) {\n    console.log("Paid $" + amount + " via PayPal");\n  }\n}`}
  },
"""

start_marker = "};\n\nlet userXP"
inject_idx = content.find(start_marker)

if inject_idx != -1:
    new_content = content[:inject_idx] + ",\n" + rich_content + content[inject_idx:]
    with open(html_path, "w") as f:
        f.write(new_content)
    print("Successfully generated T18-T21 rich content!")
else:
    print("Could not find injection point.")
