import re

html_path = "/Users/bhoomim/devops CI:CD/handbook/fullstack_ai_handbook.html"
with open(html_path, "r") as f:
    content = f.read()

rich_content = r"""
  t69: {
    tag:'Phase 2 · Backend (Java)', num:69,
    title:'Lambdas & Functional Interfaces',
    desc:'Bringing Functional Programming features to Java to make code more concise.',
    theory:`<div class="card"><h3>🏹 The Arrow Function</h3><p>Before Java 8, if you wanted to pass behavior (a function) into another method (like a click listener or a sorting comparator), you had to create a bulky <strong>Anonymous Inner Class</strong>. <strong>Lambda Expressions</strong> (<code>-></code>) provide a clear and concise way to represent a method interface using an expression.</p><h4>Functional Interfaces</h4><p>A Lambda expression can only be used where the expected type is a <strong>Functional Interface</strong>. A Functional Interface is simply an interface that contains <strong>exactly one abstract method</strong>. (e.g., <code>Runnable</code>, <code>Callable</code>, <code>Comparator</code>).</p><div class="cb"><span class="cm">// Old Java 7 Way (Anonymous Inner Class):</span>
button.addActionListener(<span class="ck">new</span> ActionListener() {
    <span class="ck">public void</span> actionPerformed(ActionEvent e) {
        System.out.println(<span class="cs">"Clicked!"</span>);
    }
});

<span class="cm">// Java 8 Lambda Way:</span>
button.addActionListener(e -> System.out.println(<span class="cs">"Clicked!"</span>));</div></div>`,
    mcqs:[
      {q:"What is a Lambda Expression in Java?",opts:["A. A new type of database","B. A short, anonymous block of code (function) that can be passed around as if it were an object","C. A multi-threading library","D. A garbage collector algorithm"],ans:1,exp:"Lambdas bring functional programming concepts to Java, dramatically reducing boilerplate code."},
      {q:"What is the defining rule of a 'Functional Interface'?",opts:["A. It must contain 'Functional' in the name","B. It must have exactly one abstract method","C. It cannot have any methods","D. It must be a class, not an interface"],ans:1,exp:"Because there is only one method to implement, the compiler can infer that your Lambda expression is meant to implement that exact method."},
      {q:"Which of the following is a classic example of a built-in Functional Interface?",opts:["A. java.util.List","B. java.lang.Runnable (only has run())","C. java.lang.String","D. java.util.HashMap"],ans:1,exp:"Runnable only has public void run(). Therefore, you can use a Lambda `() -> { code }` to create a Runnable."},
      {q:"What does the @FunctionalInterface annotation do?",opts:["A. Makes the interface run faster","B. It is an optional compiler check that throws an error if you accidentally add a second abstract method to the interface","C. Allows it to run on the GPU","D. Turns it into a class"],ans:1,exp:"It acts exactly like @Override, protecting you from breaking the interface contract in the future."},
      {q:"In the lambda expression '(a, b) -> a + b', what are 'a' and 'b'?",opts:["A. Method names","B. The parameters being passed into the single abstract method of the functional interface","C. Classes","D. Strings"],ans:1,exp:"The compiler uses Type Inference to figure out if 'a' and 'b' are integers, strings, etc., based on the interface."}
    ],
    flows:[
      {title:"Lambda Inference",items:["start:Comparator<Integer> c = (a, b) -> a - b","dec:Compiler sees Comparator","proc:Compiler knows it requires int compare(T o1, T o2)","proc:Infers 'a' and 'b' are Integers","end:Generates the anonymous class under the hood"]}
    ],
    game:{icon:"🏹",title:"The Archer",desc:"Master concise code",badges:["🏹 Lambda Shooter","⚡ Type Inferencer","🎯 Single Method"],challenges:[{icon:"📝",title:"Identify FI",desc:"What defines a Functional Interface?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Custom Functional Interface",badge:"Code Golfer",desc:"Create and use a custom Lambda.",tags:["Java","Functional"],steps:[{title:"Interface",desc:"Create interface MathOperation with one method: operate(a, b)"},{"title:"Lambda",desc:"MathOperation add = (a, b) -> a + b;"},{"title:"Execute",desc:"System.out.println(add.operate(5, 5));"}],code:`@FunctionalInterface\ninterface MathOperation {\n  int operate(int a, int b);\n}\n\npublic class Main {\n  public static void main(String[] args) {\n    // The Lambda replaces an entire anonymous class block!\n    MathOperation addition = (a, b) -> a + b;\n    MathOperation multiply = (a, b) -> a * b;\n    \n    System.out.println(addition.operate(10, 5)); // 15\n    System.out.println(multiply.operate(10, 5)); // 50\n  }\n}`}
  },
  t70: {
    tag:'Phase 2 · Backend (Java)', num:70,
    title:'Java Collections Framework',
    desc:'The unified architecture for representing and manipulating collections (Lists, Sets, Maps).',
    theory:`<div class="card"><h3>📦 The Data Toolbox</h3><p>Arrays in Java are fixed-size and rigid. The <strong>Collections Framework</strong> provides highly optimized, dynamic data structures for everyday use.</p><h4>The Core Hierarchy</h4><ul><li><strong>Iterable -> Collection -> List:</strong> Ordered collections (allow duplicates). <em>(ArrayList, LinkedList)</em></li><li><strong>Iterable -> Collection -> Set:</strong> Unordered collections (no duplicates). <em>(HashSet, TreeSet)</em></li><li><strong>Iterable -> Collection -> Queue:</strong> FIFO collections. <em>(PriorityQueue, LinkedList)</em></li><li><strong>Map:</strong> Key-Value pairs. Maps do <strong>NOT</strong> inherit from the Collection interface! <em>(HashMap, TreeMap)</em></li></ul><div class="box b-cy"><h5>ArrayList vs LinkedList</h5><p>ArrayList uses a dynamic array under the hood (Fast random access O(1), Slow insertions O(N)). LinkedList uses pointers (Slow random access O(N), Fast insertions at ends O(1)).</p></div></div>`,
    mcqs:[
      {q:"Which Interface sits at the very top of the Java Collections hierarchy (excluding Map)?",opts:["A. List","B. Iterable","C. Collection","D. Object"],ans:1,exp:"Iterable allows the collection to be used in an enhanced 'for-each' loop."},
      {q:"What is the fundamental rule of a 'Set' collection in Java?",opts:["A. It keeps everything perfectly sorted","B. It does not allow duplicate elements","C. It acts as a Key-Value store","D. It has a fixed size"],ans:1,exp:"HashSet is backed by a HashMap and ensures uniqueness."},
      {q:"Does the 'Map' interface (like HashMap) inherit from the 'Collection' interface?",opts:["A. Yes","B. No, Map is a completely separate branch of the framework because it stores Key-Value pairs rather than single elements","C. Yes, it inherits from List","D. Yes, it inherits from Set"],ans:1,exp:"You cannot directly iterate over a Map. You must iterate over its entrySet(), keySet(), or values()."},
      {q:"If you need to store 1,000,000 items, and you will frequently look up random items by their index (e.g. get(500000)), which is better?",opts:["A. ArrayList","B. LinkedList","C. HashSet","D. Queue"],ans:0,exp:"ArrayList provides O(1) random access because it uses a contiguous array under the hood."},
      {q:"If you need a Map that keeps its keys perfectly sorted alphabetically, which should you use?",opts:["A. HashMap","B. LinkedHashMap","C. TreeMap","D. ConcurrentHashMap"],ans:2,exp:"TreeMap uses a Red-Black tree under the hood to maintain sorted order in O(log N) time."}
    ],
    flows:[
      {title:"Choosing a Collection",items:["start:Key-Value? -> Map","dec:No? Needs Uniqueness? -> Set","dec:No? Needs FIFO? -> Queue","end:No? Use List (ArrayList)"]}
    ],
    game:{icon:"📦",title:"The Collector",desc:"Master data structures",badges:["📦 List Maker","🎯 Set Sniper","🗺️ Map Navigator"],challenges:[{icon:"📝",title:"List vs Set",desc:"Explain the primary difference",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Deduplication",badge:"Filterer",desc:"Convert a List to a Set to remove duplicates.",tags:["Java","Collections"],steps:[{title:"List",desc:"List<String> list = Arrays.asList('A', 'A', 'B')"},{"title:"Set",desc:"Set<String> set = new HashSet<>(list);"},{"title:"Result",desc:"Set now only contains 'A', 'B'"}],code:`List<String> rawData = Arrays.asList("apple", "banana", "apple", "orange");\n\n// Easiest way to deduplicate data in Java:\nSet<String> uniqueData = new HashSet<>(rawData);\n\nSystem.out.println(uniqueData); // [banana, orange, apple]`}
  },
  t71: {
    tag:'Phase 2 · Backend (Java)', num:71,
    title:'Generics',
    desc:'Enabling types (classes and interfaces) to be parameters when defining classes, interfaces and methods.',
    theory:`<div class="card"><h3>🏷️ Type Safety</h3><p>Before Java 5, Collections stored pure <code>Object</code> references. If you put a String in a List, and pulled it out later, the compiler didn't know it was a String. You had to manually cast it <code>(String) list.get(0)</code>. If you accidentally cast an Integer to a String, the program crashed at runtime!</p><h4>The Diamond Operator</h4><p><strong>Generics</strong> <code>&lt;T&gt;</code> allow you to specify the EXACT type a collection should hold at compile-time. If you create a <code>List&lt;String&gt;</code>, the compiler will strictly prevent you from adding an Integer to it, preventing runtime crashes.</p><div class="box b-ro"><h5>Type Erasure</h5><p>Generics only exist for the Compiler! When the code is compiled to Bytecode, all the <code>&lt;String&gt;</code> tags are completely erased and replaced with standard Object casts. This is called Type Erasure (done for backwards compatibility with old Java versions).</p></div></div>`,
    mcqs:[
      {q:"What was the primary reason Generics were introduced in Java 5?",opts:["A. To make code run faster","B. To provide compile-time Type Safety and eliminate the need for manual casting when retrieving objects from Collections","C. To encrypt data","D. To allow multiple inheritance"],ans:1,exp:"Catching a ClassCastException at compile-time is infinitely better than your app crashing at runtime."},
      {q:"What does the 'T' represent in a Generic class like Box<T>?",opts:["A. Thread","B. A Type Parameter placeholder. When you instantiate the Box, you replace T with a real class like String or Integer.","C. Time","D. Text"],ans:1,exp:"It makes classes highly reusable. You write the Box logic once, and it works for Box<String>, Box<Car>, etc."},
      {q:"Can you use primitive types in Generics (e.g. List<int>)?",opts:["A. Yes","B. No, Generics only work with Reference Types (Objects). You must use Wrapper classes like List<Integer>.","C. Only in Java 8+","D. Yes, but it's slower"],ans:1,exp:"This is a limitation of Java's Type Erasure. It needs to erase down to 'Object', and a primitive 'int' is not an Object."},
      {q:"What is 'Type Erasure'?",opts:["A. Deleting your source code","B. The process where the Java compiler removes all Generic type information during compilation to Bytecode, ensuring backward compatibility with older JVMs","C. Forgetting a variable type","D. A garbage collection feature"],ans:1,exp:"At runtime, the JVM has absolutely no idea that your List was a List<String>. It just sees List<Object>."},
      {q:"What does the wildcard '?' mean in Generics (e.g. List<? extends Number>)?",opts:["A. It means the list is empty","B. It means the list can hold objects of any type that is a subclass of Number (e.g., Integer, Double)","C. It means the type is unknown and cannot be used","D. It throws an error"],ans:1,exp:"Wildcards provide flexibility when writing methods that accept collections of various related types."}
    ],
    flows:[
      {title:"Compile-Time Safety",items:["start:List<String> list = new ArrayList<>()","proc:list.add('Hello') -> Success","dec:list.add(5) -> ?","end:COMPILER ERROR! Prevents runtime crash."]}
    ],
    game:{icon:"🏷️",title:"The Typer",desc:"Master generic types",badges:["🏷️ Type Safe","✏️ Eraser","❔ Wildcard"],challenges:[{icon:"📝",title:"Primitives",desc:"Why is List<int> illegal?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Generic Class",badge:"Box Maker",desc:"Create a highly reusable Box class using a Type Parameter.",tags:["Java","Generics"],steps:[{title:"Class",desc:"class Box<T>"},{"title:"Variable",desc:"private T item;"},{"title:"Methods",desc:"public void set(T item), public T get()"}],code:`// Highly reusable Generic Class\nclass Box<T> {\n  private T item;\n  \n  public void setItem(T item) {\n    this.item = item;\n  }\n  \n  public T getItem() {\n    return this.item;\n  }\n}\n\n// Usage:\nBox<String> stringBox = new Box<>();\nstringBox.setItem("Hello");\n// stringBox.setItem(123); // Compiler correctly blocks this!`}
  },
  t72: {
    tag:'Phase 2 · Backend (Java)', num:72,
    title:'Exception Handling',
    desc:'The mechanism to handle runtime errors, maintaining the normal flow of the application.',
    theory:`<div class="card"><h3>🛑 Graceful Degradation</h3><p>An <strong>Exception</strong> is an unwanted or unexpected event (e.g., network timeout, dividing by zero) that disrupts the normal flow of the program. If unhandled, the JVM crashes and prints a stack trace.</p><h4>The Hierarchy</h4><p>Everything stems from <code>Throwable</code>.</p><ul><li><strong>Error:</strong> Critical system failures (OutOfMemoryError). Do NOT try to catch these. The app is dead.</li><li><strong>Exception (Checked):</strong> Conditions outside your control (e.g., FileNotFoundException, IOException). The compiler <em>forces</em> you to handle them with try/catch.</li><li><strong>RuntimeException (Unchecked):</strong> Logic errors caused by the programmer (NullPointerException, IndexOutOfBounds). The compiler does not force you to catch them; you should fix your code instead!</li></ul></div>`,
    mcqs:[
      {q:"What is the difference between a Checked Exception and an Unchecked Exception (RuntimeException) in Java?",opts:["A. Checked exceptions are ignored","B. The compiler FORCES you to handle (try/catch) Checked Exceptions at compile-time. Unchecked exceptions are not forced.","C. Unchecked exceptions crash the OS","D. They are the same"],ans:1,exp:"Checked exceptions (like dealing with File IO or Databases) represent external risks you MUST prepare for."},
      {q:"Should you use a try/catch block to handle an 'Error' (like OutOfMemoryError)?",opts:["A. Yes, always","B. No, Errors represent severe, unrecoverable system failures. Your application should terminate.","C. Only on Windows","D. Yes, it fixes the memory"],ans:1,exp:"Exceptions are recoverable. Errors are not."},
      {q:"What is the purpose of the 'finally' block in a try/catch/finally structure?",opts:["A. It makes the program run faster","B. It contains code that is guaranteed to execute NO MATTER WHAT (whether an exception was thrown or not), typically used to close open resources like DB connections or file streams.","C. It restarts the app","D. It deletes the error"],ans:1,exp:"Even if the try block has a 'return' statement, the finally block will still execute before the method returns."},
      {q:"If you don't want to use a try/catch block to handle a Checked Exception, what must you do?",opts:["A. Delete the code","B. Add a 'throws' declaration to your method signature, passing the responsibility to whatever method called yours","C. Use a while loop","D. Use the volatile keyword"],ans:1,exp:"This is called 'Duck and Pass'. The exception bubbles up the Call Stack until it hits a try/catch (or hits the JVM and crashes)."},
      {q:"What is a NullPointerException?",opts:["A. An Error","B. A Checked Exception","C. An Unchecked Exception (RuntimeException) indicating you tried to call a method on an object reference that points to nothing (null)","D. A database error"],ans:2,exp:"NPEs are the most common bug in Java. You shouldn't try/catch them; you should use if(obj != null) to fix your logic."}
    ],
    flows:[
      {title:"Try/Catch/Finally Flow",items:["start:try { openFile(); read(); }","dec:Does read() throw IOException?","proc:(Yes) Jump instantly to catch(IOException e)","proc:(No) Skip catch block","end:Execute finally { closeFile(); }"]}
    ],
    game:{icon:"🛑",title:"The Catcher",desc:"Master error handling",badges:["🛑 Exception Catcher","🦆 Thrower","🧹 Finally Sweeper"],challenges:[{icon:"📝",title:"Checked vs Unchecked",desc:"Explain the difference",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Custom Exception",badge:"Rule Maker",desc:"Create and throw a custom business exception.",tags:["Java","Exceptions"],steps:[{title:"Class",desc:"class AgeException extends RuntimeException"},{"title:"Throw",desc:"if (age < 18) throw new AgeException('Too young!')"},{"title:"Catch",desc:"Use try/catch to handle it gracefully"}],code:`// Custom Unchecked Exception\nclass InvalidAgeException extends RuntimeException {\n  public InvalidAgeException(String message) {\n    super(message);\n  }\n}\n\npublic class Validator {\n  public void checkAge(int age) {\n    if (age < 18) {\n      // Disrupt the flow!\n      throw new InvalidAgeException("Must be 18+"); \n    }\n    System.out.println("Access granted.");\n  }\n}`}
  },
"""

start_marker = "};\n\nlet userXP"
inject_idx = content.find(start_marker)

if inject_idx != -1:
    new_content = content[:inject_idx] + ",\n" + rich_content + content[inject_idx:]
    with open(html_path, "w") as f:
        f.write(new_content)
    print("Successfully generated T69-T72 rich content!")
else:
    print("Could not find injection point.")
