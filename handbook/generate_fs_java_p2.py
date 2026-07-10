import re

html_path = "/Users/bhoomim/devops CI:CD/handbook/fullstack_ai_handbook.html"
with open(html_path, "r") as f:
    content = f.read()

rich_content = r"""
  t65: {
    tag:'Phase 2 · Backend (Java)', num:65,
    title:'Multithreading',
    desc:'Executing multiple threads concurrently to maximize CPU utilization.',
    theory:`<div class="card"><h3>🧵 Concurrent Execution</h3><p>By default, Java applications run on a single <strong>Main Thread</strong>. If you execute a heavy database query, your entire application freezes and waits (blocks). <strong>Multithreading</strong> allows you to spawn secondary threads that run in parallel on different CPU cores, keeping your main application responsive.</p><h4>Creating a Thread</h4><p>You can create a thread in Java by extending the <code>Thread</code> class, or better, implementing the <code>Runnable</code> interface and passing it to a Thread.</p><div class="box b-ro"><h5>⚠️ Thread Safety (Synchronization)</h5><p>If two threads try to modify the exact same variable (like a bank balance) at the exact same millisecond, data corruption occurs (Race Condition). You must use the <code>synchronized</code> keyword to lock the resource so only one thread can touch it at a time.</p></div></div>`,
    mcqs:[
      {q:"What is the primary benefit of Multithreading?",opts:["A. It makes the code shorter","B. It allows multiple tasks to run concurrently (or in parallel on multi-core CPUs), preventing long tasks from freezing the application","C. It uses less memory","D. It encrypts the application"],ans:1,exp:"Parallelism maximizes CPU usage and responsiveness."},
      {q:"In Java, what is the preferred way to define a task for a new Thread?",opts:["A. Extend the Object class","B. Implement the 'Runnable' interface and define the run() method","C. Write a while loop","D. Use the 'thread' keyword"],ans:1,exp:"Implementing Runnable is preferred because Java only allows single inheritance. If you extend Thread, you can't extend any other class."},
      {q:"What is a 'Race Condition'?",opts:["A. Two threads competing to finish first","B. A bug that occurs when two or more threads attempt to read and write to the same shared memory location simultaneously, leading to unpredictable/corrupt data","C. A network timeout","D. A JVM crash"],ans:1,exp:"Race conditions are the most notorious bugs in multithreaded programming."},
      {q:"How do you prevent a Race Condition in Java?",opts:["A. Use the 'synchronized' keyword on the method or block of code to lock it (Mutex)","B. Tell the threads to wait","C. Use a larger CPU","D. Run the program twice"],ans:0,exp:"The 'synchronized' keyword acts as a lock. If Thread A has the lock, Thread B must wait in line until A is finished."},
      {q:"What does calling myThread.join() do?",opts:["A. Merges two threads together","B. Forces the current thread (e.g., the Main Thread) to pause and wait until 'myThread' finishes its execution before continuing","C. Joins a network","D. Starts the thread"],ans:1,exp:"Join is used when the main program needs the result of the background thread before it can proceed."}
    ],
    flows:[
      {title:"Synchronized Lock",items:["start:Thread A and B call addMoney()","dec:Thread A grabs the Lock","proc:Thread B tries, but must WAIT","proc:Thread A updates balance","proc:Thread A releases Lock","end:Thread B grabs Lock, updates balance"]}
    ],
    game:{icon:"🧵",title:"The Weaver",desc:"Master parallel execution",badges:["🧵 Threader","🔒 Lock Master","🏁 Race Preventer"],challenges:[{icon:"📝",title:"Runnable",desc:"Why is Runnable preferred over extending Thread?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Basic Runnable",badge:"Multitasker",desc:"Spawn a background thread in Java.",tags:["Java","Threads"],steps:[{title:"Implement",desc:"class MyTask implements Runnable"},{"title:"Run Method",desc:"Override public void run() { ... }"},{"title:"Start",desc:"Thread t = new Thread(new MyTask()); t.start();"}],code:`// Creating a thread in Java\nclass BackgroundTask implements Runnable {\n  public void run() {\n    System.out.println("Running in background!");\n  }\n}\n\n// In Main:\nThread t = new Thread(new BackgroundTask());\nt.start(); // Spawns the thread and calls run()\n// NOT t.run() - that just runs it sequentially!`}
  },
  t66: {
    tag:'Phase 2 · Backend (Java)', num:66,
    title:'Concurrency Utilities',
    desc:'High-level APIs in java.util.concurrent that make multithreading safer and easier.',
    theory:`<div class="card"><h3>🎛️ The Thread Managers</h3><p>Manually creating <code>new Thread()</code> every time you need one is terrible for performance (thread creation is heavy). It also makes returning values and handling errors a nightmare.</p><h4>The Executor Framework</h4><p>Introduced in Java 5, the <code>java.util.concurrent</code> package provides <strong>Thread Pools</strong>. Instead of creating new threads, you create a pool of reusable threads (e.g., a pool of 10 threads). You submit "Tasks" (Runnables or Callables) to the pool, and the pool manages executing them.</p><div class="box b-vi"><h5>Callable & Future</h5><p>A <code>Runnable</code> cannot return a result. A <strong>Callable</strong> can! When you submit a Callable to a Thread Pool, it immediately returns a <strong>Future</strong> object. A Future is a promise that the result will be there eventually. You can call <code>future.get()</code> later to retrieve the actual data.</p></div></div>`,
    mcqs:[
      {q:"Why should you use an ExecutorService (Thread Pool) instead of manually creating 'new Thread()' in a loop?",opts:["A. It writes the code for you","B. Thread creation is very expensive for the OS. A Thread Pool reuses a fixed number of threads, drastically improving performance and preventing the server from crashing due to too many threads.","C. It encrypts the threads","D. It runs on the GPU"],ans:1,exp:"Thread Pools are the backbone of high-performance web servers like Tomcat."},
      {q:"What is the main difference between the 'Runnable' and 'Callable' interfaces?",opts:["A. Callable is for C++, Runnable is for Java","B. Runnable's run() method returns void and cannot throw checked exceptions. Callable's call() method can return a specific value and throw exceptions.","C. Callable is faster","D. Runnable is asynchronous, Callable is synchronous"],ans:1,exp:"If you need your background thread to calculate a number and give it back to you, you must use Callable."},
      {q:"When you submit a Callable to an ExecutorService, what object is immediately returned to you?",opts:["A. The final result","B. A 'Future' object representing the pending result of the asynchronous computation","C. A String","D. A Boolean"],ans:1,exp:"The Future acts as a placeholder. It allows the main thread to continue working while the Callable calculates."},
      {q:"What happens if you call future.get() but the background thread hasn't finished calculating yet?",opts:["A. It returns null","B. The main thread will block (pause) and wait at that exact line until the result is ready","C. It throws an error","D. It restarts the thread"],ans:1,exp:"Calling .get() too early defeats the purpose of async programming. You should usually check future.isDone() first."},
      {q:"Which class provides highly optimized, thread-safe collections (like ConcurrentHashMap)?",opts:["A. java.util.Collections","B. java.util.concurrent","C. java.lang","D. java.io"],ans:1,exp:"Concurrent collections use fine-grained locking (locking only specific segments of the map, not the whole thing) for massive performance gains."}
    ],
    flows:[
      {title:"Callable & Future Flow",items:["start:Submit Callable to Pool","proc:Pool returns a Future immediately","proc:Main Thread does other work","dec:Main Thread calls future.get()","proc:Blocks if not ready","end:Receives calculated data"]}
    ],
    game:{icon:"🎛️",title:"The Manager",desc:"Master ExecutorServices",badges:["🎛️ Pool Manager","🔮 Future Seer","📞 Caller"],challenges:[{icon:"📝",title:"Runnable vs Callable",desc:"List the 2 main differences",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Thread Pool Execution",badge:"Dispatcher",desc:"Submit tasks to an ExecutorService.",tags:["Java","Concurrency"],steps:[{title:"Create Pool",desc:"Executors.newFixedThreadPool(2)"},{"title:"Submit",desc:"Submit a Callable that returns a string"},{"title:"Get Future",desc:"Print future.get()"}],code:`ExecutorService pool = Executors.newFixedThreadPool(2);\n\n// Submit a Callable (returns a value)\nFuture<String> future = pool.submit(() -> {\n  Thread.sleep(1000); // Simulate work\n  return "Data calculated!";\n});\n\n// This will block until the 1 second passes\nSystem.out.println(future.get());\npool.shutdown();`}
  },
  t67: {
    tag:'Phase 2 · Backend (Java)', num:67,
    title:'Memory Model',
    desc:'How the JVM manages memory visibility and ordering across multiple threads.',
    theory:`<div class="card"><h3>🧠 The Brain's Caches</h3><p>The <strong>Java Memory Model (JMM)</strong> dictates how threads interact with memory. In modern hardware, CPUs have L1/L2 caches. When a Java thread reads a variable from the main Heap, it often copies it into its local CPU cache for speed.</p><h4>The Visibility Problem</h4><p>If Thread A changes a variable to 'true', it might only change it in its local cache! Thread B might still see 'false' because it's looking at main memory. This is a visibility bug.</p><h4>The 'volatile' Keyword</h4><p>Applying the <code>volatile</code> keyword to a variable forces all threads to bypass their local CPU caches and <strong>read/write directly to Main Memory</strong>. This guarantees that if Thread A changes it, Thread B will instantly see the change.</p></div>`,
    mcqs:[
      {q:"What specific problem does the Java Memory Model address?",opts:["A. Disk space limits","B. Visibility and ordering of variables across multiple concurrent threads, dealing with CPU caching issues","C. Garbage collection algorithms","D. HTML parsing"],ans:1,exp:"It standardizes how and when changes made by one thread become visible to others."},
      {q:"What does the 'volatile' keyword do?",opts:["A. It makes the variable highly explosive","B. It guarantees that any read or write to the variable bypasses local CPU caches and goes straight to Main Memory, ensuring instant visibility across all threads","C. It encrypts the variable","D. It locks the entire class"],ans:1,exp:"Volatile solves the 'Visibility Problem'."},
      {q:"Does 'volatile' prevent Race Conditions (like two threads incrementing a counter)?",opts:["A. Yes, absolutely","B. No. Volatile ensures visibility, but it does NOT provide synchronization/locking (Atomicity). Two threads can still read the same memory at the exact same time and overwrite each other.","C. Only for strings","D. Yes, if used with integers"],ans:1,exp:"For a counter (count++), you still need 'synchronized' or AtomicInteger. Volatile is best for simple boolean flags (e.g., isRunning = false)."},
      {q:"What is 'Atomicity'?",opts:["A. An operation that is indivisible. It completely succeeds or completely fails, and cannot be interrupted halfway through by another thread.","B. A nuclear reaction","C. Splitting a variable in half","D. Caching a variable"],ans:0,exp:"'count++' is NOT atomic. It is actually 3 steps (Read, Add 1, Write). A thread can be interrupted in the middle."},
      {q:"Which Java class provides thread-safe, lock-free atomic operations on integers?",opts:["A. SafeInt","B. AtomicInteger (in java.util.concurrent.atomic)","C. VolatileInt","D. Integer"],ans:1,exp:"AtomicInteger uses low-level CPU instructions (Compare-And-Swap) to do 'count++' safely without needing slow 'synchronized' blocks."}
    ],
    flows:[
      {title:"The Visibility Problem",items:["start:Main Memory: flag=false","proc:Thread A reads flag to local cache","proc:Thread A sets cache flag=true","dec:Thread B reads Main Memory flag","end:Thread B reads FALSE! (Bug)"]}
    ],
    game:{icon:"🧠",title:"The Architect",desc:"Master the JMM",badges:["🧠 Memory Mapper","⚡ Volatile User","⚛️ Atomic Pro"],challenges:[{icon:"📝",title:"Atomicity",desc:"Explain why count++ is not atomic",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Atomic Counter",badge:"Thread Safe",desc:"Use AtomicInteger to safely count across threads.",tags:["Java","Memory Model"],steps:[{title:"Init",desc:"AtomicInteger count = new AtomicInteger(0)"},{"title:"Thread Action",desc:"count.incrementAndGet()"},{"title:"Result",desc:"Guaranteed to be accurate even with 1000 threads"}],code:`import java.util.concurrent.atomic.AtomicInteger;\n\nclass SafeCounter {\n  // Thread-safe, lock-free counter\n  private AtomicInteger count = new AtomicInteger(0);\n  \n  public void increment() {\n    // Atomic operation: Read, Add, Write all in one unbreakable step\n    count.incrementAndGet();\n  }\n}`}
  },
  t68: {
    tag:'Phase 2 · Backend (Java)', num:68,
    title:'Java Streams API',
    desc:'A declarative pipeline approach to processing collections of objects (Introduced in Java 8).',
    theory:`<div class="card"><h3>🌊 The Data Pipeline</h3><p>Before Java 8, processing a list (e.g., finding all users older than 18 and getting their names) required writing messy, multi-line <code>for-loops</code> and <code>if-statements</code> (Imperative programming). The <strong>Streams API</strong> allows you to process data <strong>Declaratively</strong> (like SQL).</p><h4>Core Concepts</h4><ul><li><strong>Source:</strong> Typically a Collection (<code>list.stream()</code>).</li><li><strong>Intermediate Operations:</strong> Operations that return a new Stream (e.g., <code>filter</code>, <code>map</code>, <code>sorted</code>). They are <em>Lazy</em> and don't execute until a terminal operation is called.</li><li><strong>Terminal Operations:</strong> The final operation that produces a non-stream result (e.g., <code>collect(toList)</code>, <code>forEach</code>, <code>count</code>). This triggers the whole pipeline.</li></ul></div>`,
    mcqs:[
      {q:"What is the primary benefit of the Java Streams API?",opts:["A. It downloads data from the internet","B. It provides a clean, declarative, functional-style pipeline for processing collections (filtering, mapping, reducing) without writing verbose loops","C. It streams video files","D. It replaces SQL databases"],ans:1,exp:"Streams make code immensely more readable and less error-prone."},
      {q:"What does it mean that Intermediate Operations (like .filter() and .map()) are 'Lazy'?",opts:["A. They run very slowly","B. They don't actually execute any processing until a Terminal Operation (like .collect()) is invoked at the end of the chain","C. They only process half the data","D. They drop errors"],ans:1,exp:"Laziness allows the JVM to optimize the pipeline under the hood (e.g., fusing filter and map into a single pass)."},
      {q:"Which Stream operation takes an object and transforms it into a completely different object (e.g., User object -> String name)?",opts:["A. .filter()","B. .map()","C. .reduce()","D. .forEach()"],ans:1,exp:"Map 'maps' (transforms) an input value to an output value."},
      {q:"Which Stream operation takes an entire stream of values and condenses it into a single final value (e.g., summing all numbers)?",opts:["A. .filter()","B. .map()","C. .reduce()","D. .sorted()"],ans:2,exp:"Reduce takes an accumulator and the current element, reducing the stream to one value."},
      {q:"How can you instantly make a Stream process elements in parallel across multiple CPU cores?",opts:["A. It's impossible","B. Just call .parallelStream() instead of .stream() on the collection","C. Write a multi-threaded ExecutorService","D. Add the 'volatile' keyword"],ans:1,exp:"This is the hidden superpower of Streams. Parallelism becomes a one-word change (though it should be used cautiously on small datasets)."}
    ],
    flows:[
      {title:"Stream Pipeline",items:["start:List of Users","proc:.stream()","proc:.filter(user -> user.age > 18)","proc:.map(user -> user.name)","end:.collect(Collectors.toList()) -> List of Strings"]}
    ],
    game:{icon:"🌊",title:"The Plumber",desc:"Master data pipelines",badges:["🌊 Streamer","🗺️ Mapper","🤏 Reducer"],challenges:[{icon:"📝",title:"Intermediate vs Terminal",desc:"Explain the difference",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Stream Filtering",badge:"Declarative Pro",desc:"Filter and map a list of numbers.",tags:["Java","Streams"],steps:[{title:"List",desc:"Arrays.asList(1, 2, 3, 4, 5)"},{"title:"Stream",desc:"list.stream().filter(n -> n % 2 == 0)"},{"title:"Map & Collect",desc:".map(n -> n * 10).collect(Collectors.toList())"}],code:`List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);\n\n// Declarative Pipeline: Find evens, multiply by 10\nList<Integer> result = numbers.stream()\n  .filter(n -> n % 2 == 0) // Keep 2, 4\n  .map(n -> n * 10)        // Transform to 20, 40\n  .collect(Collectors.toList()); // Terminal: Output List\n  \nSystem.out.println(result); // [20, 40]`}
  },
"""

start_marker = "};\n\nlet userXP"
inject_idx = content.find(start_marker)

if inject_idx != -1:
    new_content = content[:inject_idx] + ",\n" + rich_content + content[inject_idx:]
    with open(html_path, "w") as f:
        f.write(new_content)
    print("Successfully generated T65-T68 rich content!")
else:
    print("Could not find injection point.")
