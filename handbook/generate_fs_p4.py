import re

html_path = "/Users/bhoomim/devops CI:CD/handbook/fullstack_ai_handbook.html"
with open(html_path, "r") as f:
    content = f.read()

rich_content = """
  t10: {
    tag:'Phase 1 · Core Foundations', num:10,
    title:'Recursion',
    desc:'A function that calls itself until it reaches a base case.',
    theory:`<div class="card"><h3>🪆 The Russian Nesting Doll</h3><p>Recursion is a method of solving a problem where the solution depends on solutions to smaller instances of the same problem. A recursive function <strong>calls itself</strong>.</p><h4>Two Rules of Recursion</h4><ol><li><strong>Base Case:</strong> The condition under which the function stops calling itself. Without this, you get infinite recursion (Stack Overflow).</li><li><strong>Recursive Step:</strong> The part where the function calls itself with a modified, smaller input, moving closer to the base case.</li></ol><div class="cb"><span class="cm">// Recursive Factorial (5! = 5 * 4 * 3 * 2 * 1)</span>
<span class="ck">function</span> <span class="cv">factorial</span>(n) {
    <span class="cm">// 1. Base Case</span>
    <span class="ck">if</span> (n === <span class="cs">1</span>) <span class="ck">return</span> <span class="cs">1</span>;
    
    <span class="cm">// 2. Recursive Step</span>
    <span class="ck">return</span> n * factorial(n - <span class="cs">1</span>);
}</div></div>`,
    mcqs:[
      {q:"What is a Base Case in recursion?",opts:["A. The starting point of the function","B. The condition that stops the recursion from continuing indefinitely","C. The hardest part of the problem","D. The database connection"],ans:1,exp:"The base case prevents infinite loops and Stack Overflow errors."},
      {q:"What happens if a recursive function lacks a Base Case?",opts:["A. It runs perfectly","B. It throws a Syntax Error","C. It causes a Stack Overflow exception because it calls itself infinitely","D. It returns 0"],ans:2,exp:"Every function call adds a frame to the Call Stack. Infinite calls will exceed the stack memory limit."},
      {q:"How does the Recursive Step move towards the base case?",opts:["A. By increasing the complexity of the input","B. By passing a modified, usually smaller or simpler version of the original input","C. By using a for loop","D. By waiting 1 second"],ans:1,exp:"e.g., passing (n-1) to the next call brings it closer to the base case of n==1."},
      {q:"Any problem that can be solved with recursion can also be solved with:",opts:["A. A database","B. Iteration (loops) like a 'while' loop","C. Machine Learning","D. HTML"],ans:1,exp:"Recursion and iteration are theoretically equivalent, though recursion is often cleaner for things like Tree traversal."},
      {q:"Why might recursion be worse than iteration in some languages?",opts:["A. It takes more lines of code","B. It uses more memory because each call adds a new frame to the Call Stack (unless tail-call optimized)","C. It's too fast","D. It cannot return strings"],ans:1,exp:"Iterative loops reuse the same memory frame. Recursion builds up a massive call stack."}
    ],
    flows:[
      {title:"Recursive Call Stack (factorial 3)",items:["start:factorial(3)","proc:Calls 3 * factorial(2)","proc:Calls 2 * factorial(1)","proc:Base Case: Returns 1","proc:Returns 2 * 1 = 2","end:Returns 3 * 2 = 6"]}
    ],
    game:{icon:"🪆",title:"Recursion Ranger",desc:"Master self-calling functions",badges:["🪆 Nester","🛑 Base Case Boss","🥞 Stack Overflow Survivor"],challenges:[{icon:"📝",title:"Trace it",desc:"Trace the stack for factorial(4)",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Fibonacci Generator",badge:"Mathematician",desc:"Write a recursive function to find the Nth Fibonacci number.",tags:["JavaScript","Recursion"],steps:[{title:"Base Cases",desc:"If n===0 return 0, if n===1 return 1"},{title:"Recursive Step",desc:"Return fib(n-1) + fib(n-2)"},{title:"Test",desc:"Console log fib(5)"}],code:`function fibonacci(n) {\n  if (n === 0) return 0;\n  if (n === 1) return 1;\n  return fibonacci(n - 1) + fibonacci(n - 2);\n}\n\nconsole.log(fibonacci(6)); // 8`}
  },
  t11: {
    tag:'Phase 1 · Core Foundations', num:11,
    title:'Time Complexity',
    desc:'How the runtime of an algorithm grows as the size of the input grows.',
    theory:`<div class="card"><h3>⏱️ Measuring Algorithm Speed</h3><p>Time Complexity doesn't measure speed in "seconds" (since a supercomputer is faster than a phone). Instead, it measures how the number of <strong>operations</strong> increases as the input size (<strong>N</strong>) increases.</p><h4>Common Complexities</h4><ul><li><strong>O(1) - Constant:</strong> Takes the same amount of time regardless of N (e.g., getting the first item in an array).</li><li><strong>O(log N) - Logarithmic:</strong> Extremely fast for large datasets. Usually halves the dataset each step (e.g., Binary Search).</li><li><strong>O(N) - Linear:</strong> Time grows directly with N. (e.g., looping through an array once).</li><li><strong>O(N^2) - Quadratic:</strong> Very slow for large N. (e.g., a loop inside a loop, comparing every item to every other item).</li></ul></div>`,
    mcqs:[
      {q:"Why do we use Time Complexity instead of measuring seconds?",opts:["A. Seconds are too hard to calculate","B. Execution time varies by hardware; Time Complexity evaluates the theoretical scalability of the algorithm itself","C. Clocks are inaccurate","D. Time Complexity is required by JavaScript"],ans:1,exp:"An O(N^2) algorithm will eventually choke any hardware if N is large enough."},
      {q:"What is the time complexity of finding a specific value in an unsorted array of size N by checking every item?",opts:["A. O(1)","B. O(log N)","C. O(N)","D. O(N^2)"],ans:2,exp:"You might have to check all N items (Linear search), making it O(N)."},
      {q:"If an algorithm processes 10 items in 10 operations, and 100 items in 10,000 operations, what is its likely complexity?",opts:["A. O(N)","B. O(log N)","C. O(N^2)","D. O(1)"],ans:2,exp:"10^2 = 100. 100^2 = 10,000. This is quadratic scaling O(N^2)."},
      {q:"Which time complexity is generally considered the fastest/best?",opts:["A. O(N!)","B. O(N)","C. O(N^2)","D. O(1)"],ans:3,exp:"O(1) Constant Time is instantaneous regardless of data size."},
      {q:"A nested 'for' loop (a loop inside a loop) over the same array of size N typically has a time complexity of:",opts:["A. O(1)","B. O(N)","C. O(2N)","D. O(N^2)"],ans:3,exp:"For every N item, it loops N times. N * N = N^2."}
    ],
    flows:[
      {title:"Algorithm Selection",items:["start:Analyze Input Size (N)","dec:N is Massive?","proc:(Yes) Must use O(1) or O(log N)","proc:(No) O(N) or O(N log N) is fine","end:Write Code"]}
    ],
    game:{icon:"⏱️",title:"Time Lord",desc:"Master algorithm speed",badges:["⚡ O(1) Optimizer","🐢 Quadratic Snail","📈 Scaler"],challenges:[{icon:"📝",title:"Analyze Code",desc:"Determine complexity of a nested loop",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Speed Tester",badge:"Benchmarker",desc:"Write a script to compare O(N) vs O(1) lookups.",tags:["JavaScript","Performance"],steps:[{title:"Setup Array & Set",desc:"Create an array of 1M items, and a Set of 1M items"},{title:"Time Array",desc:"Use console.time to measure array.includes()"},{title:"Time Set",desc:"Use console.time to measure set.has()"}],code:`let arr = Array.from({length: 1000000}, (_, i) => i);\nlet set = new Set(arr);\n\nconsole.time("Array O(N)");\narr.includes(999999);\nconsole.timeEnd("Array O(N)");\n\nconsole.time("Set O(1)");\nset.has(999999);\nconsole.timeEnd("Set O(1)");`}
  },
  t12: {
    tag:'Phase 1 · Core Foundations', num:12,
    title:'Space Complexity',
    desc:'How much additional memory an algorithm requires as the input size grows.',
    theory:`<div class="card"><h3>🗄️ Measuring RAM Usage</h3><p>While Time Complexity is about CPU cycles, <strong>Space Complexity</strong> is about RAM usage. An algorithm might be extremely fast (O(1) time) but require massive amounts of memory (O(N) space) to achieve that speed.</p><h4>Common Space Complexities</h4><ul><li><strong>O(1) Space:</strong> The algorithm uses a fixed number of variables, regardless of input size. (e.g., sorting an array in-place).</li><li><strong>O(N) Space:</strong> The algorithm creates a new data structure (like a duplicate array or a hash map) that grows proportionally to the input size.</li></ul><div class="box b-vi"><h5>💡 The Time-Space Tradeoff</h5><p>In software engineering, you can often make an algorithm faster by using more memory (e.g., Caching/Memoization), or you can use less memory by computing things on the fly (which takes more time).</p></div></div>`,
    mcqs:[
      {q:"What does Space Complexity measure?",opts:["A. Hard drive space taken by the source code","B. The additional working memory (RAM) needed by an algorithm as input grows","C. Cloud storage cost","D. CPU temperature"],ans:1,exp:"It evaluates how memory requirements scale with input size."},
      {q:"An algorithm that reverses an array by swapping elements in the original array (without creating a new array) has a space complexity of:",opts:["A. O(N)","B. O(N^2)","C. O(1)","D. O(log N)"],ans:2,exp:"Because it modifies the array 'in-place' using only one temporary variable for the swap, space is constant O(1)."},
      {q:"An algorithm that takes an array of size N, creates a brand new copy of that array, and returns the copy has a space complexity of:",opts:["A. O(1)","B. O(N)","C. O(N^2)","D. O(log N)"],ans:1,exp:"The new array's size scales 1:1 with the input array, so it requires O(N) extra space."},
      {q:"What is the 'Time-Space Tradeoff'?",opts:["A. The theory of relativity","B. A principle where you can often speed up execution time by storing pre-calculated data (using more space), or save space by re-calculating (taking more time)","C. A way to compress files","D. Buying more RAM saves CPU time"],ans:1,exp:"Caching (like Redis) is the ultimate time-space tradeoff: use RAM to avoid slow DB queries."},
      {q:"Does a recursive function use extra space?",opts:["A. No, it's O(1) space","B. Yes, every recursive call adds a frame to the Call Stack, meaning depth of N recursion takes O(N) space","C. Only if you use arrays","D. Only in Java"],ans:1,exp:"The call stack consumes memory. Deep recursion means high space complexity."}
    ],
    flows:[
      {title:"In-Place vs Out-of-Place",items:["start:Input Array [A,B,C]","dec:Algorithm Type?","proc:(In-Place) Swap inside same array (O(1) space)","proc:(Out-of-Place) Create new array [C,B,A] (O(N) space)","end:Return"]}
    ],
    game:{icon:"🗄️",title:"Memory Miser",desc:"Optimize your RAM footprint",badges:["🗄️ In-Placer","⚖️ Tradeoff Master","🧠 Allocator"],challenges:[{icon:"📝",title:"Identify Space",desc:"Find the space complexity of map()",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"In-Place Reversal",badge:"Miser",desc:"Reverse an array using O(1) space instead of O(N) space.",tags:["JavaScript","Algorithms"],steps:[{title:"Two Pointers",desc:"Set left=0, right=len-1"},{title:"While Loop",desc:"While left < right"},{title:"Swap",desc:"Swap arr[left] and arr[right], then increment/decrement"}],code:`function reverseInPlace(arr) {\n  let left = 0;\n  let right = arr.length - 1;\n  while (left < right) {\n    let temp = arr[left];\n    arr[left] = arr[right];\n    arr[right] = temp;\n    left++;\n    right--;\n  }\n  return arr;\n}\n\nlet data = [1,2,3,4];\nconsole.log(reverseInPlace(data));`}
  },
  t13: {
    tag:'Phase 1 · Core Foundations', num:13,
    title:'Big O Notation',
    desc:'The mathematical notation used to classify algorithms according to how their run time or space requirements grow.',
    theory:`<div class="card"><h3>📈 Speaking the Interview Language</h3><p>Big O Notation evaluates the <strong>Worst Case Scenario</strong>. We drop constants and non-dominant terms because we only care about massive scalability.</p><h4>Rules of Big O</h4><ul><li><strong>Drop Constants:</strong> O(2N) simplifies to <strong>O(N)</strong>. (If data doubles, time doubles. The multiplier doesn't matter for scaling).</li><li><strong>Drop Non-Dominant Terms:</strong> O(N² + N) simplifies to <strong>O(N²)</strong>. (At N=1,000,000, the N² part is so massive that the +N is mathematically irrelevant).</li></ul><div class="box b-em"><h5>🚀 Big O Cheat Sheet (Best to Worst)</h5><p>O(1) → O(log N) → O(N) → O(N log N) → O(N²) → O(2^N) → O(N!)</p></div></div>`,
    mcqs:[
      {q:"What does Big O notation primarily describe?",opts:["A. The exact time in milliseconds an algorithm will take","B. How the runtime or space requirements scale relative to the input size (N) in the worst-case scenario","C. The memory usage of a hard drive","D. How many bugs are in the code"],ans:1,exp:"Big O is about asymptotic scaling, not exact benchmarking."},
      {q:"If an algorithm takes O(N) time to run, and O(N^2) time to prepare the data, what is the final Big O?",opts:["A. O(N)","B. O(N^3)","C. O(N^2)","D. O(N + N^2)"],ans:2,exp:"We drop the non-dominant term. O(N^2 + N) becomes O(N^2)."},
      {q:"Why do we drop constants in Big O? (e.g. O(5N) becomes O(N))",opts:["A. Because 5 is a small number","B. Because Big O looks at the shape of the growth curve at infinity, and constants don't change the linear nature of the curve","C. Because compilers optimize it out","D. It's a mistake, you shouldn't drop constants"],ans:1,exp:"Constants represent hardware/implementation speed. Big O represents theoretical scaling."},
      {q:"Which is worse (slower for large datasets)?",opts:["A. O(1)","B. O(N)","C. O(log N)","D. O(2^N)"],ans:3,exp:"O(2^N) is Exponential time (e.g. recursive Fibonacci). It will crash your computer for N=50."},
      {q:"What is the Big O of finding a value in a standard Hash Map (Object/Dictionary)?",opts:["A. O(N)","B. O(log N)","C. O(1) average case","D. O(N^2)"],ans:2,exp:"Hash maps provide constant O(1) time lookups, which makes them incredibly powerful."}
    ],
    flows:[
      {title:"Simplifying Big O",items:["start:Formula: O(3N^2 + 5N + 100)","proc:Drop Constants: O(N^2 + N + 1)","proc:Drop Non-Dominant: O(N^2)","end:Final: O(N^2)"]}
    ],
    game:{icon:"📈",title:"Big O Boss",desc:"Master complexity theory",badges:["✂️ Simplifier","📉 Curve Rider","🚀 O(1) Hero"],challenges:[{icon:"✂️",title:"Simplify",desc:"Simplify O(10N + N^3)",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Big O Analyzer",badge:"Theorist",desc:"Given a code snippet, identify its Big O.",tags:["Theory","Big O"],steps:[{title:"Analyze Snippet 1",desc:"A single loop = O(N)"},{title:"Analyze Snippet 2",desc:"Two nested loops = O(N^2)"},{title:"Analyze Snippet 3",desc:"Two separate sequential loops = O(N)"}],code:`// Snippet 1: O(N)\nfor(let i=0; i<n; i++) {}\n\n// Snippet 2: O(N^2)\nfor(let i=0; i<n; i++) {\n  for(let j=0; j<n; j++) {}\n}\n\n// Snippet 3: O(N)\nfor(let i=0; i<n; i++) {}\nfor(let j=0; j<n; j++) {}`}
  },
"""

start_marker = "};\n\nlet userXP"
inject_idx = content.find(start_marker)

if inject_idx != -1:
    new_content = content[:inject_idx] + ",\n" + rich_content + content[inject_idx:]
    with open(html_path, "w") as f:
        f.write(new_content)
    print("Successfully generated T10-T13 rich content!")
else:
    print("Could not find injection point.")
