import re

html_path = "/Users/bhoomim/devops CI:CD/handbook/fullstack_ai_handbook.html"
with open(html_path, "r") as f:
    content = f.read()

rich_content = r"""
  t60: {
    tag:'Phase 2 · Backend (Java)', num:60,
    title:'JVM Architecture',
    desc:'The engine that powers Java, enabling its "Write Once, Run Anywhere" philosophy.',
    theory:`<div class="card"><h3>⚙️ The Virtual Machine</h3><p>The <strong>Java Virtual Machine (JVM)</strong> is a highly sophisticated, abstract computing machine that enables a computer to run a Java program. Unlike C or C++, which compile directly to machine code specific to the operating system (Windows/Mac/Linux), Java compiles to an intermediate state called <strong>Bytecode</strong>. The JVM then translates this Bytecode into native machine code at runtime.</p><h4>Detailed Components of the JVM</h4><ul><li><strong>Classloader Subsystem:</strong> Responsible for loading, linking, and initializing the Java classes (.class files) into memory.</li><li><strong>Memory Area (Runtime Data Area):</strong><ul><li><em>Method Area:</em> Stores class-level data (variables, static blocks, method code).</li><li><em>Heap:</em> Where all objects and instance variables are allocated.</li><li><em>Stack:</em> Where local variables and method calls are stored (Thread-specific).</li><li><em>PC Register:</em> Keeps track of the current instruction executing.</li></ul></li><li><strong>Execution Engine:</strong> Translates Bytecode to machine code. It contains the <em>Interpreter</em> (reads line by line) and the <em>JIT (Just-In-Time) Compiler</em> (optimizes frequently executed code by pre-compiling it to native machine code).</li></ul></div>`,
    mcqs:[
      {q:"What is the primary function of the JVM (Java Virtual Machine)?",opts:["A. To write Java code","B. To act as a runtime environment that translates Java Bytecode into native OS machine code","C. To design user interfaces","D. To host databases"],ans:1,exp:"The JVM acts as a translator between the compiled Java program and the underlying hardware."},
      {q:"Which component of the JVM is responsible for allocating memory for objects?",opts:["A. Method Area","B. Stack","C. Heap","D. PC Register"],ans:2,exp:"The Heap is the global memory pool where objects live. The Stack is for local primitive variables and method frames."},
      {q:"What does the JIT (Just-In-Time) Compiler do?",opts:["A. It writes code for you","B. It pauses the program to clean memory","C. It monitors frequently executed bytecode ('hot spots') and compiles it directly into native machine code to drastically improve performance","D. It compiles Java to Python"],ans:2,exp:"Without JIT, the JVM interpreter would be very slow reading bytecode line-by-line. JIT brings Java's speed close to C++."},
      {q:"Which of these memory areas is NOT shared across all threads in the JVM?",opts:["A. Heap","B. Method Area","C. The Stack","D. None of the above"],ans:2,exp:"Every thread gets its own private Stack to keep track of its local variables and function calls. The Heap is shared globally."},
      {q:"What principle does the JVM enable for Java?",opts:["A. Write Once, Compile Never","B. Write Once, Run Anywhere (WORA)","C. Run Once, Write Anywhere","D. Compile Everything Always"],ans:1,exp:"Because you compile to Bytecode, that same Bytecode can run on a Windows JVM, a Mac JVM, or a Linux JVM without changing the code."}
    ],
    flows:[
      {title:"JVM Execution Flow",items:["start:Source Code (.java)","proc:Javac Compiler","proc:Bytecode (.class)","dec:JVM Classloader","proc:JVM Execution Engine (Interpreter + JIT)","end:Native OS Machine Code"]}
    ],
    game:{icon:"⚙️",title:"The Engine",desc:"Master JVM internals",badges:["⚙️ Virtualizer","🔥 JIT Compiler","🧱 Memory Mapper"],challenges:[{icon:"📝",title:"Heap vs Stack",desc:"Define the difference in detail",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Simulate JIT (Mental Model)",badge:"Optimizer",desc:"Understand how JIT optimizes loops.",tags:["Java","JVM"],steps:[{title:"Interpreter",desc:"Reads loop 1000 times, translating every time (Slow)"},{"title:"Hotspot Detected",desc:"JIT notices the loop is run frequently"},{"title:"Compilation",desc:"JIT compiles loop to native machine code once, saving massive time"}],code:`// Mental Model\nfunction runLoop() {\n  for(let i=0; i<10000; i++) {\n    // Interpreter is slow here\n    // JIT steps in, compiles this block to native code\n    doMath(i);\n  }\n}`}
  },
  t61: {
    tag:'Phase 2 · Backend (Java)', num:61,
    title:'JRE vs JDK',
    desc:'Understanding the Java ecosystem tooling and deployment environments.',
    theory:`<div class="card"><h3>🛠️ The Builder vs The Player</h3><p>If you want to play a video game, you just need a console. If you want to <em>build</em> a video game, you need a complex game engine and SDKs. Java works the same way.</p><h4>JRE (Java Runtime Environment)</h4><p>The JRE is everything you need to <strong>run</strong> a Java application. It contains the JVM, the core Java classes (java.lang, java.util), and supporting libraries. <em>(Analogy: The video game console).</em></p><h4>JDK (Java Development Kit)</h4><p>The JDK is everything you need to <strong>develop</strong> a Java application. It includes the entire JRE, plus development tools like the compiler (<code>javac</code>), the archiver (<code>jar</code>), and debugging tools (<code>jdb</code>). <em>(Analogy: The game engine/developer kit).</em></p></div>`,
    mcqs:[
      {q:"If your client only wants to RUN your finished Java application, what do they need to install?",opts:["A. Only the JVM","B. The JRE (Java Runtime Environment)","C. The JDK (Java Development Kit)","D. Node.js"],ans:1,exp:"The JRE contains the JVM and the necessary libraries to run compiled code. They don't need compilers."},
      {q:"What essential tool does the JDK contain that the JRE does NOT?",opts:["A. The JVM","B. The Garbage Collector","C. javac (The Java Compiler)","D. Threading libraries"],ans:2,exp:"The compiler ('javac') is strictly for developers converting .java text files into .class bytecode files."},
      {q:"Which of the following equations is correct?",opts:["A. JRE = JDK + JVM","B. JDK = JRE + Development Tools (Compilers, Debuggers)","C. JVM = JDK + JRE","D. JRE = JVM + Compilers"],ans:1,exp:"The JDK is a superset. It wraps around the JRE, which wraps around the JVM."},
      {q:"What is a .jar file?",opts:["A. A text file containing Java source code","B. Java ARchive - A zipped package of compiled .class files and metadata, ready to be executed by the JRE","C. A database file","D. An image format"],ans:1,exp:"JAR files are how Java applications are distributed."},
      {q:"If you try to run 'javac MyProgram.java' and get a 'command not found' error, what is the likely issue?",opts:["A. Your code has a syntax error","B. You only have the JRE installed, not the JDK (or your PATH is not set)","C. The JVM is broken","D. Java is outdated"],ans:1,exp:"'javac' requires the JDK."}
    ],
    flows:[
      {title:"The Ecosystem Hierarchy",items:["start:JDK (Java Development Kit)","proc:Contains -> Compilers (javac), Debuggers","dec:Contains -> JRE (Java Runtime Environment)","proc:Contains -> Core Libraries (java.util)","end:Contains -> JVM (Executes the code)"]}
    ],
    game:{icon:"🛠️",title:"The Toolsmith",desc:"Master the Java environment",badges:["🛠️ Kit Builder","🏃 Runtime Runner","📦 JAR Packager"],challenges:[{icon:"📝",title:"Equation",desc:"Write the JDK/JRE equation",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Terminal Developer",badge:"CLI Wizard",desc:"Understand the compilation and execution commands.",tags:["Java","Tooling"],steps:[{title:"Source",desc:"You write 'Hello.java'"},{"title:"JDK Tool",desc:"Run 'javac Hello.java' to create 'Hello.class'"},{"title:"JRE Tool",desc:"Run 'java Hello' to start the JVM and execute it"}],code:`# Terminal Commands (Mental Model)\n\n# 1. Developer uses JDK to compile\n$ javac HelloWorld.java\n# (Outputs HelloWorld.class)\n\n# 2. User uses JRE to run\n$ java HelloWorld\n# (Prints: Hello World!)`}
  },
  t62: {
    tag:'Phase 2 · Backend (Java)', num:62,
    title:'Bytecode',
    desc:'The highly optimized, platform-independent intermediate instruction set of Java.',
    theory:`<div class="card"><h3>📜 The Universal Language</h3><p>When you compile C++, it turns into binary 1s and 0s that are strictly tied to the CPU architecture (e.g., x86 vs ARM). If you compile C++ on a Mac, that executable will completely fail on Windows.</p><p>Java solves this by compiling into <strong>Bytecode</strong> (the <code>.class</code> file). Bytecode is essentially machine code for a <em>fake, imaginary computer</em> (The JVM). It is incredibly compact and optimized.</p><h4>Why is it brilliant?</h4><p>You can compile your code on a Mac into Bytecode, email that Bytecode file to a friend on Windows, and their Windows JVM will translate it perfectly. This is the heart of platform independence.</p></div>`,
    mcqs:[
      {q:"What is Java Bytecode?",opts:["A. Native machine code for Intel processors","B. An intermediate, platform-independent instruction set that is executed by the JVM","C. Human-readable Java source code","D. A type of database"],ans:1,exp:"Bytecode is the magic intermediate step that makes WORA (Write Once Run Anywhere) possible."},
      {q:"What file extension does compiled Java Bytecode have?",opts:["A. .java","B. .exe","C. .class","D. .byte"],ans:2,exp:"The javac compiler takes a .java file and outputs a .class file containing the bytecode."},
      {q:"Why is Bytecode considered 'secure'?",opts:["A. It is encrypted with AES-256","B. Before execution, the JVM's Bytecode Verifier checks it for illegal operations (like direct memory pointer manipulation) to prevent malicious code from crashing the host OS","C. It requires a password","D. It cannot be decompiled"],ans:1,exp:"The JVM acts as a sandbox, strictly verifying the bytecode before allowing it to run."},
      {q:"Can languages other than Java compile to Java Bytecode?",opts:["A. No, only Java","B. Yes! Languages like Kotlin, Scala, and Groovy compile down to standard Bytecode and run on the JVM flawlessly.","C. Yes, but only Python","D. Yes, but it runs slower"],ans:1,exp:"The JVM doesn't care what language you wrote in, as long as the compiler outputs valid Bytecode."},
      {q:"Is Bytecode human-readable?",opts:["A. Yes, it looks just like Java","B. No, it looks like gibberish binary/hex to humans (unless you use a disassembler like 'javap')","C. Yes, it's just JSON","D. Yes, it's HTML"],ans:1,exp:"It is optimized for the JVM, not for human eyes."}
    ],
    flows:[
      {title:"Platform Independence",items:["start:Mac Developer -> compiles to Bytecode","proc:Sends .class file to Server","dec:Server is Linux OS","proc:Linux JVM translates Bytecode to Linux Machine Code","end:Runs flawlessly!"]}
    ],
    game:{icon:"📜",title:"The Translator",desc:"Master the universal format",badges:["📜 Scroll Reader","🛡️ Verifier","🌍 Universal Executor"],challenges:[{icon:"📝",title:"Other Langs",desc:"Name 2 other JVM languages",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Bytecode Disassembly",badge:"Hacker",desc:"Understand how to peek inside a .class file.",tags:["Java","Bytecode"],steps:[{title:"Compile",desc:"javac App.java"},{"title:"Disassemble",desc:"Run 'javap -c App.class'"},{"title:"Analyze",desc:"You will see JVM instructions like 'aload_0', 'invokespecial'"}],code:`// If you disassemble a basic constructor, it looks like this:\n// 0: aload_0\n// 1: invokespecial #1   // Method java/lang/Object."<init>":()V\n// 4: return\n\n// This is the literal assembly language of the JVM!`}
  },
  t63: {
    tag:'Phase 2 · Backend (Java)', num:63,
    title:'Garbage Collection',
    desc:'The automatic memory management process that frees developers from manual memory deallocation.',
    theory:`<div class="card"><h3>🗑️ The Automatic Maid</h3><p>In languages like C or C++, when you create an object, you manually reserve memory. When you are done, you MUST manually delete it (<code>free()</code>). If you forget, your app suffers a <strong>Memory Leak</strong> and eventually crashes.</p><p>Java uses an automatic <strong>Garbage Collector (GC)</strong>. It constantly runs in the background as a low-priority thread, looking for objects on the Heap that no longer have any active references pointing to them. If an object is "unreachable," the GC deletes it and frees the memory.</p><h4>Generational Garbage Collection</h4><p>The Java Heap is heavily optimized into generations:</p><ul><li><strong>Young Generation (Eden Space):</strong> Where all new objects are born. Most objects die very quickly here (e.g., local variables inside a loop).</li><li><strong>Old Generation (Tenured):</strong> Objects that survive multiple garbage collection sweeps in the Young Generation are promoted here.</li></ul></div>`,
    mcqs:[
      {q:"What is the main advantage of Java's Garbage Collector?",opts:["A. It makes the program run faster than C++","B. It prevents developers from having to manually allocate and free memory, drastically reducing memory leaks and segmentation faults","C. It sorts data automatically","D. It writes code for you"],ans:1,exp:"Manual memory management is one of the leading causes of bugs and security vulnerabilities in C/C++."},
      {q:"How does the Garbage Collector decide which objects to destroy?",opts:["A. It destroys the oldest objects","B. It destroys the largest objects","C. It destroys objects that are 'Unreachable' (no active variables or pointers refer to them anymore)","D. It asks the user"],ans:2,exp:"If nothing in your active code can possibly reach the object, it is garbage."},
      {q:"What is the 'Young Generation' (Eden Space) in the JVM Heap?",opts:["A. Where old code is stored","B. The memory area where all brand-new objects are allocated. It is swept frequently because most objects have very short lifespans.","C. A cache for integers","D. A database"],ans:1,exp:"The GC assumes that 'most objects die young' (e.g. temporary variables). Sweeping the Eden space is very fast."},
      {q:"What happens during a 'Stop-The-World' Garbage Collection event?",opts:["A. The computer restarts","B. The JVM completely pauses all application threads to safely reorganize memory and perform a major collection","C. The database drops tables","D. Network connections are severed"],ans:1,exp:"Major GCs (cleaning the Old Generation) can cause noticeable lag spikes (pauses) in high-performance applications."},
      {q:"Can a developer force the Garbage Collector to run immediately by calling System.gc()?",opts:["A. Yes, it guarantees immediate collection","B. No, calling System.gc() is merely a 'suggestion' to the JVM. The JVM ultimately decides when to run it.","C. Yes, but only on Macs","D. Only if the app is paused"],ans:1,exp:"You cannot force the GC. You can only politely request it."}
    ],
    flows:[
      {title:"Generational Promotion",items:["start:Object created in Eden","proc:Minor GC occurs","dec:Is Object still referenced?","proc:(Yes) Moved to Survivor Space","dec:Survives 15 more GCs?","end:(Yes) Promoted to Old Generation"]}
    ],
    game:{icon:"🗑️",title:"The Maid",desc:"Master memory management",badges:["🗑️ Sweeper","⏳ Generational Sage","🛑 Stop-The-World"],challenges:[{icon:"📝",title:"Stop the World",desc:"Explain a STW pause",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Triggering GC (Conceptual)",badge:"Memory Leaker",desc:"Create unreachable objects to feed the GC.",tags:["Java","Memory"],steps:[{title:"Loop",desc:"Create a while(true) loop"},{"title:"Instantiate",desc:"Create huge arrays inside the loop"},{"title:"Orphan",desc:"Do not store them in external variables. They become instantly unreachable!"}],code:`// Generating Garbage\nfunction makeGarbage() {\n  while(true) {\n    // Creates a new array, but immediately loses the reference\n    // next time the loop runs. \n    let massiveData = new Array(1000000);\n    \n    // The GC will frantically clean these up in the background\n    // to prevent an OutOfMemoryError.\n  }\n}`}
  },
  t64: {
    tag:'Phase 2 · Backend (Java)', num:64,
    title:'ClassLoaders',
    desc:'The subsystem of JVM dedicated to loading class files when they are needed.',
    theory:`<div class="card"><h3>🚚 Dynamic Delivery</h3><p>Java is highly dynamic. It doesn't load every single class into memory when the application starts. Instead, it loads them <strong>lazily (on-demand)</strong>. The <strong>ClassLoader Subsystem</strong> is responsible for this.</p><h4>The Delegation Hierarchy</h4><p>ClassLoaders follow a strict hierarchy to prevent security issues (like someone trying to override the core <code>java.lang.String</code> class with a malicious version):</p><ol><li><strong>Bootstrap ClassLoader:</strong> Loads core Java APIs (rt.jar). Written in native C/C++.</li><li><strong>Extension ClassLoader:</strong> Loads classes from the JDK extensions directory.</li><li><strong>Application ClassLoader:</strong> Loads classes from your application's classpath (your code and dependencies).</li></ol></div>`,
    mcqs:[
      {q:"When does the JVM load a class into memory?",opts:["A. All classes are loaded instantly at boot","B. Dynamically, only at the exact moment the class is first referenced or instantiated in the code (Lazy Loading)","C. When the OS tells it to","D. After the program finishes"],ans:1,exp:"Lazy loading saves massive amounts of RAM and boot time."},
      {q:"What is the 'Delegation Principle' of ClassLoaders?",opts:["A. Classloaders ask the user what to do","B. A ClassLoader will always delegate the request to its Parent ClassLoader first. It only tries to load the class if the parent fails.","C. It delegates to the network","D. It delegates to the database"],ans:1,exp:"This is a security feature. The Application loader asks the Bootstrap loader to load 'java.lang.String'. The Bootstrap loader finds the real one, preventing you from loading a fake one."},
      {q:"Which ClassLoader is responsible for loading the core, foundational Java classes (like String, Integer, Object)?",opts:["A. Application ClassLoader","B. Network ClassLoader","C. Bootstrap ClassLoader","D. Extension ClassLoader"],ans:2,exp:"The Bootstrap loader is the very top of the hierarchy, deeply embedded in the JVM."},
      {q:"If a class is not found in the classpath by any ClassLoader, what happens?",opts:["A. The program ignores it","B. A ClassNotFoundException (or NoClassDefFoundError) is thrown at runtime","C. It writes the class for you","D. It reboots"],ans:1,exp:"This is the classic error when you forget to include a .jar dependency."},
      {q:"Can developers write their own Custom ClassLoaders?",opts:["A. No, it is locked by Oracle","B. Yes, by extending java.lang.ClassLoader (often used by Application Servers like Tomcat to load web apps dynamically without rebooting)","C. Yes, but only in C++","D. Only for primitive types"],ans:1,exp:"Custom classloaders allow advanced features like hot-reloading code or loading classes over a network."}
    ],
    flows:[
      {title:"ClassLoader Delegation",items:["start:App requests 'MyClass'","proc:AppLoader asks ExtLoader","proc:ExtLoader asks BootstrapLoader","dec:Bootstrap find it?","proc:(No) Drops down to ExtLoader","dec:Ext find it?","proc:(No) Drops down to AppLoader","end:AppLoader loads 'MyClass'"]}
    ],
    game:{icon:"🚚",title:"The Loader",desc:"Master class loading",badges:["🚚 Delivery Driver","🛡️ Delegator","📦 Lazy Loader"],challenges:[{icon:"📝",title:"Delegation",desc:"Explain why delegation is secure",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"ClassNotFound",badge:"Debugger",desc:"Understand the most common ClassLoader error.",tags:["Java","Debugging"],steps:[{title:"Missing Jar",desc:"Imagine a project relying on 'Gson'"},{"title:"Execution",desc:"You run it, but forgot to include gson.jar in the classpath"},{"title:"Crash",desc:"ClassLoader fails to find it and throws ClassNotFoundException"}],code:`// If you try to dynamically load a class that doesn't exist:\ntry {\n  // The Application ClassLoader attempts to find this path\n  Class.forName("com.fake.MissingClass");\n} catch (ClassNotFoundException e) {\n  System.out.println("The ClassLoader could not find the file!");\n}`}
  },
"""

start_marker = "};\n\nlet userXP"
inject_idx = content.find(start_marker)

if inject_idx != -1:
    new_content = content[:inject_idx] + ",\n" + rich_content + content[inject_idx:]
    with open(html_path, "w") as f:
        f.write(new_content)
    print("Successfully generated T60-T64 rich content!")
else:
    print("Could not find injection point.")
