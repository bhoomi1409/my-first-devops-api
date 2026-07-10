import re

html_path = "/Users/bhoomim/devops CI:CD/handbook/fullstack_ai_handbook.html"
with open(html_path, "r") as f:
    content = f.read()

rich_content = """
  t7: {
    tag:'Phase 1 · Core Foundations', num:7,
    title:'Scope',
    desc:'Understanding where variables live and where they can be accessed within your code.',
    theory:`<div class="card"><h3>🔭 The Boundaries of Code</h3><p>Scope determines the visibility and lifespan of variables and functions in your code. If you try to access a variable outside of its scope, your program will crash or return undefined.</p><h4>Types of Scope</h4><ul><li><strong>Global Scope:</strong> Variables declared outside of any function or block. They are accessible everywhere. <em>(Use sparingly to avoid conflicts!)</em></li><li><strong>Function (Local) Scope:</strong> Variables declared inside a function. They only exist while the function is running.</li><li><strong>Block Scope:</strong> Introduced by <code>let</code> and <code>const</code> (in JS/C++). Variables exist only within the nearest curly braces <code>{}</code> (like inside an if-statement or for-loop).</li></ul><div class="cb"><span class="cm">// Scope Example</span>
<span class="ck">let</span> <span class="cv">globalVar</span> = <span class="cs">"I am everywhere"</span>;

<span class="ck">function</span> <span class="cv">checkScope</span>() {
    <span class="ck">let</span> <span class="cv">functionVar</span> = <span class="cs">"I am trapped in here"</span>;
    <span class="ck">if</span> (<span class="cs">true</span>) {
        <span class="ck">let</span> <span class="cv">blockVar</span> = <span class="cs">"I am trapped in this block"</span>;
    }
    <span class="cm">// blockVar is NOT accessible here!</span>
}
<span class="cm">// functionVar is NOT accessible here!</span></div></div>`,
    mcqs:[
      {q:"What is Global Scope?",opts:["A. A variable accessible only in the main function","B. A variable accessible from anywhere in the program","C. A variable that stores web addresses","D. A variable stored in a database"],ans:1,exp:"Global variables can be read and modified by any part of the program, which is why they can lead to bugs if overused."},
      {q:"Why is using too many global variables considered bad practice?",opts:["A. They take up too much hard drive space","B. They cause naming collisions and make state changes hard to track (Global State Mutation)","C. They are slower to read","D. They require special compilers"],ans:1,exp:"If any function can change a global variable at any time, debugging becomes a nightmare."},
      {q:"What happens if you try to log a Function Scoped variable from outside the function?",opts:["A. It prints the value","B. It prints 'undefined' or throws a ReferenceError","C. It prints 0","D. It works normally"],ans:1,exp:"The variable is destroyed once the function finishes executing (its stack frame is popped)."},
      {q:"In JavaScript, what is the difference between 'var' and 'let' regarding scope?",opts:["A. They are identical","B. 'var' is block-scoped, 'let' is function-scoped","C. 'let' is block-scoped, 'var' is function-scoped (or globally scoped)","D. 'let' is a constant"],ans:2,exp:"'let' respects the curly braces of if/for blocks. 'var' ignores them and scopes to the enclosing function."},
      {q:"If an inner function accesses a variable from its outer function, what is this called?",opts:["A. An Array","B. A Closure","C. A Promise","D. A Loop"],ans:1,exp:"Closures allow inner functions to remember the scope of the outer function even after the outer function has finished."}
    ],
    flows:[
      {title:"Scope Resolution (Scope Chain)",items:["start:Variable Called","dec:In Current Scope?","proc:(Yes) Use it","proc:(No) Check Parent Scope","dec:Found?","proc:(No) Check Global Scope","end:Return Error or Value"]}
    ],
    game:{icon:"🔭",title:"Scope Sniper",desc:"Master variable boundaries",badges:["🌍 Globalist","🔒 Localizer","📦 Block Builder"],challenges:[{icon:"📝",title:"Identify Scope",desc:"Find the scope of 3 variables",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Closure Counter",badge:"Scoper",desc:"Use closures to create a private variable scope.",tags:["JavaScript","Scope","Closures"],steps:[{title:"Outer Function",desc:"Create createCounter()"},{title:"Private Variable",desc:"Declare 'count' inside it"},{title:"Inner Function",desc:"Return a function that increments and returns 'count'"}],code:`function createCounter() {\n  let count = 0; // Private block scope\n  return function() {\n    count++;\n    return count;\n  };\n}\n\nlet myCounter = createCounter();\nconsole.log(myCounter()); // 1\nconsole.log(myCounter()); // 2`}
  },
  t8: {
    tag:'Phase 1 · Core Foundations', num:8,
    title:'Memory Management',
    desc:'How languages allocate and free RAM, and why memory leaks occur.',
    theory:`<div class="card"><h3>🧠 RAM and the OS</h3><p>Every time you declare a variable or create an object, the program asks the Operating System (OS) for a tiny slice of Random Access Memory (RAM). When you are done using it, that memory must be returned (freed).</p><h4>Manual vs Automatic</h4><ul><li><strong>Manual (C, C++):</strong> The programmer explicitly writes <code>malloc()</code> to get memory and <code>free()</code> to return it. Powerful, fast, but prone to memory leaks.</li><li><strong>Automatic (Java, Python, JS):</strong> A background process called the <strong>Garbage Collector (GC)</strong> automatically frees memory when variables are no longer needed.</li></ul><div class="box b-am"><h5>⚠️ What is a Memory Leak?</h5><p>A memory leak occurs when your program allocates memory but forgets to free it. Over time, the program consumes all available RAM and the OS kills it (Out Of Memory Error).</p></div></div>`,
    mcqs:[
      {q:"What does a Garbage Collector (GC) do?",opts:["A. Deletes old log files","B. Automatically identifies and frees memory that is no longer referenced by the program","C. Formats the hard drive","D. Optimizes CPU usage"],ans:1,exp:"The GC scans memory for objects that cannot be reached by the code anymore and recycles that RAM."},
      {q:"Which language requires manual memory management?",opts:["A. Java","B. Python","C. C++","D. JavaScript"],ans:2,exp:"In C/C++, you must explicitly manage pointers and free memory yourself."},
      {q:"What is a Memory Leak?",opts:["A. When data spills onto the hard drive","B. When the program forgets to release memory it no longer needs, eventually crashing the system","C. When a hacker steals data from RAM","D. When the CPU overheats"],ans:1,exp:"Memory leaks slowly consume RAM until an Out Of Memory (OOM) exception occurs."},
      {q:"How do most modern Garbage Collectors determine if an object can be deleted?",opts:["A. By checking its file size","B. Reachability / Mark-and-Sweep (if no variables point to it, delete it)","C. By asking the user","D. By deleting the oldest objects"],ans:1,exp:"If an object is not referenced by any active variable in the scope chain, it is considered 'garbage'."},
      {q:"Why might you choose a language with manual memory management over GC?",opts:["A. Because writing free() is fun","B. Because GC causes unpredictable pauses (latency) which is bad for games or high-frequency trading","C. Because it's easier to learn","D. Because GC uses too much hard drive space"],ans:1,exp:"Garbage collection requires CPU cycles and can pause execution ('stop-the-world' events)."}
    ],
    flows:[
      {title:"Mark & Sweep Garbage Collection",items:["start:GC Cycle Starts","proc:Pause Execution","proc:Mark all reachable objects","proc:Sweep (delete) unmarked objects","end:Resume Execution"]}
    ],
    game:{icon:"🧠",title:"Memory Maestro",desc:"Master RAM allocation",badges:["🧠 Allocator","🧹 Sweeper","🗑️ Garbage Collector"],challenges:[{icon:"📝",title:"Find the Leak",desc:"Identify a memory leak in JS code",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Leak Simulator",badge:"Leaker",desc:"Create an intentional memory leak to see how JS handles it.",tags:["JavaScript","Memory"],steps:[{title:"Global Array",desc:"Create a massive global array"},{title:"Infinite Loop",desc:"Use setInterval to push huge strings into it"},{title:"Observe",desc:"Watch your browser tab's RAM usage spike"}],code:`let leakedMemory = [];\n\n// Run at your own risk!\nsetInterval(() => {\n  let hugeString = new Array(1000000).join('x');\n  leakedMemory.push(hugeString);\n  console.log("Memory Array Length: " + leakedMemory.length);\n}, 100);`}
  },
  t9: {
    tag:'Phase 1 · Core Foundations', num:9,
    title:'Stack vs Heap',
    desc:'The two distinct areas of memory used during program execution.',
    theory:`<div class="card"><h3>🥞 The Stack</h3><p>The Stack is used for static memory allocation. It stores <strong>primitive types</strong> (numbers, booleans) and <strong>function frames</strong>. It works on a Last-In, First-Out (LIFO) basis.</p><ul><li>Very fast access.</li><li>Memory is automatically freed when the function exits (frame popped).</li><li>Limited in size (causes Stack Overflow if exceeded).</li></ul><h3>📦 The Heap</h3><p>The Heap is used for dynamic memory allocation. It stores <strong>reference types</strong> (large objects, arrays, instances of classes).</p><ul><li>Slower access than the stack.</li><li>Requires a Garbage Collector (or manual freeing) to clean up.</li><li>Huge size (limited only by your physical RAM).</li></ul><div class="box b-cy"><h5>💡 The Pointer Connection</h5><p>When you create an array: <code>let arr = [1, 2, 3]</code>, the actual array data <code>[1, 2, 3]</code> is stored in the <strong>Heap</strong>. The variable <code>arr</code> is stored on the <strong>Stack</strong>, containing a memory address (pointer) pointing to the Heap data.</p></div></div>`,
    mcqs:[
      {q:"Which data structure does the Stack memory use?",opts:["A. FIFO (First In First Out)","B. LIFO (Last In First Out)","C. Tree","D. Graph"],ans:1,exp:"The last function called is the first one to finish and be popped off the stack."},
      {q:"Where are primitive values (like 'let age = 30') usually stored?",opts:["A. The Heap","B. The Stack","C. The Hard Drive","D. The CPU Cache"],ans:1,exp:"Primitives have a fixed size and are stored directly on the stack for fast access."},
      {q:"Where is a massive 10,000 item Array stored?",opts:["A. The Stack","B. The Heap","C. In the Cloud","D. In the GPU"],ans:1,exp:"Large, dynamic data structures are stored in the heap."},
      {q:"What causes a 'Stack Overflow'?",opts:["A. Writing too much data to the heap","B. Pushing too many function frames onto the stack (usually via infinite recursion) until it runs out of space","C. A website error","D. Dividing by zero"],ans:1,exp:"The stack has a strict size limit. Infinite recursion exceeds it immediately."},
      {q:"Why is the Heap slower than the Stack?",opts:["A. Because it's further away from the CPU","B. Because finding an open block of memory and following pointers adds overhead","C. Because it's encrypted","D. It's actually faster"],ans:1,exp:"Stack allocation is just moving a pointer. Heap allocation requires searching for contiguous free space."}
    ],
    flows:[
      {title:"Object Allocation Flow",items:["start:let obj = {x: 1}","proc:OS finds space in Heap","proc:Writes {x: 1} to Heap","proc:Stack stores pointer to Heap address","end:Ready"]}
    ],
    game:{icon:"🥞",title:"Stack Stacker",desc:"Master the dual memory models",badges:["🥞 Stacker","📦 Heaper","🎯 Pointer Sniper"],challenges:[{icon:"📝",title:"Memory Map",desc:"Map a variable to stack vs heap",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Reference vs Value",badge:"Pointer",desc:"Prove that objects are stored by reference and primitives by value.",tags:["JavaScript","Memory"],steps:[{title:"Primitive Copy",desc:"Copy a primitive, change the copy, check original"},{title:"Object Copy",desc:"Copy an object, change property, check original"},{title:"Observe",desc:"Notice the original object changed too! (Pointer)"}],code:`// Stack (Value)\nlet a = 10;\nlet b = a;\nb = 20;\nconsole.log(a); // Still 10\n\n// Heap (Reference/Pointer)\nlet obj1 = { name: "Bhoomi" };\nlet obj2 = obj1;\nobj2.name = "Hacked";\nconsole.log(obj1.name); // Hacked! (Both point to same Heap address)`}
  },
"""

start_marker = "};\n\nlet userXP"
inject_idx = content.find(start_marker)

if inject_idx != -1:
    new_content = content[:inject_idx] + ",\n" + rich_content + content[inject_idx:]
    with open(html_path, "w") as f:
        f.write(new_content)
    print("Successfully generated T7-T9 rich content!")
else:
    print("Could not find injection point.")
