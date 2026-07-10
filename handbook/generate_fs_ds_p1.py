import re

html_path = "/Users/bhoomim/devops CI:CD/handbook/fullstack_ai_handbook.html"
with open(html_path, "r") as f:
    content = f.read()

rich_content = """
  t27: {
    tag:'Phase 1 · Data Structures', num:27,
    title:'Arrays',
    desc:'A collection of items stored at contiguous memory locations.',
    theory:`<div class="card"><h3>📦 The Foundation of Data</h3><p>An <strong>Array</strong> (or List in Python) is the simplest and most widely used data structure. It stores elements of the same type in <em>contiguous</em> (side-by-side) memory blocks.</p><h4>Time Complexities</h4><ul><li><strong>Access:</strong> <code>O(1)</code>. Because memory is contiguous, the computer can instantly jump to <code>array[5]</code> using simple math: (Base Address + (5 * Size of Type)).</li><li><strong>Search:</strong> <code>O(N)</code>. You have to check every item until you find it.</li><li><strong>Insertion/Deletion (at end):</strong> <code>O(1)</code> (Usually, unless resizing).</li><li><strong>Insertion/Deletion (at beginning/middle):</strong> <code>O(N)</code>. If you insert an item at index 0, you must shift <em>every other element</em> one space to the right.</li></ul><div class="box b-ro"><h5>⚠️ Static vs Dynamic Arrays</h5><p>In low-level languages (C, Java), static arrays have a fixed size. If an array of size 5 fills up, you must create a brand new array of size 10 and copy everything over. Modern languages (JS, Python) handle this dynamic resizing automatically behind the scenes.</p></div></div>`,
    mcqs:[
      {q:"Why is reading an element at a specific index in an array so fast (O(1))?",opts:["A. Because the CPU memorizes it","B. Because elements are stored in contiguous memory, allowing instant mathematical address calculation","C. Because arrays use hash functions","D. Because arrays are always sorted"],ans:1,exp:"The computer just calculates: Base Memory Address + (Index * Data Size)."},
      {q:"What is the Time Complexity of inserting a new element at the very BEGINNING (index 0) of a standard array?",opts:["A. O(1)","B. O(log N)","C. O(N)","D. O(N^2)"],ans:2,exp:"You must shift every existing element one index to the right, which takes O(N) operations."},
      {q:"What happens behind the scenes when a Dynamic Array (like an ArrayList or JS Array) runs out of space?",opts:["A. The program crashes","B. It deletes the oldest item","C. It creates a new, larger array (usually double the size) in memory, copies the old elements over, and deletes the old array","D. It compresses the data"],ans:2,exp:"This is why pushing to an array is O(1) amortized, but occasionally O(N) when a resize triggers."},
      {q:"Which scenario is an Array perfectly suited for?",opts:["A. Frequent insertions and deletions at the beginning","B. Fast random access to elements via an index (e.g., retrieving the 100th item instantly)","C. Fast searching for a specific string value without knowing its index","D. Connecting graph nodes"],ans:1,exp:"O(1) random access is the primary superpower of an array."},
      {q:"Is a JavaScript Array technically a traditional contiguous array?",opts:["A. Yes","B. No, JS Arrays are actually hash map-like objects under the hood (though modern JS engines optimize them to contiguous blocks when possible)","C. Yes, but only for strings","D. No, it's a Linked List"],ans:1,exp:"JS abstracts away memory management, but V8 engine tries to store dense arrays contiguously for speed."}
    ],
    flows:[
      {title:"O(N) Insertion at Index 0",items:["start:Array: [A, B, C]","proc:Target: Insert 'X' at 0","proc:Shift C to index 3","proc:Shift B to index 2","proc:Shift A to index 1","end:Insert X at 0 -> [X, A, B, C]"]}
    ],
    game:{icon:"📦",title:"Array Alchemist",desc:"Master contiguous memory",badges:["📦 Box Stacker","⚡ O(1) Sniper","🧱 Shifter"],challenges:[{icon:"📝",title:"Shift It",desc:"Explain why shift() is O(N)",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Custom Array Resizer",badge:"Memory Manager",desc:"Simulate dynamic array resizing logic.",tags:["Concepts","Arrays"],steps:[{title:"Init",desc:"Create class with capacity 2"},{"title:"Push",desc:"If length === capacity, double the capacity"},{"title:"Copy",desc:"Console log 'Resizing from 2 to 4...'"}],code:`class CustomArray {\n  constructor() {\n    this.capacity = 2;\n    this.length = 0;\n  }\n  push(val) {\n    if (this.length === this.capacity) {\n      console.log(\`Resizing from \${this.capacity} to \${this.capacity * 2}\`);\n      this.capacity *= 2;\n    }\n    this.length++;\n  }\n}\n\nlet arr = new CustomArray();\narr.push(1); arr.push(2); arr.push(3); // Triggers resize!`}
  },
  t28: {
    tag:'Phase 1 · Data Structures', num:28,
    title:'Strings',
    desc:'An immutable sequence of characters, heavily used in textual data processing.',
    theory:`<div class="card"><h3>🔤 Arrays of Characters</h3><p>Under the hood, most languages treat Strings as <strong>an array of characters</strong>. (e.g., "Hello" is essentially <code>['H', 'e', 'l', 'l', 'o']</code>).</p><h4>Immutability</h4><p>In many languages (Java, Python, JS, C#), strings are <strong>Immutable</strong>. This means once a string is created in memory, it cannot be changed. If you do <code>str = str + " World"</code>, the computer does NOT modify the original string; it creates a brand new string in memory and updates the pointer.</p><div class="cb"><span class="cm">// Why string concatenation in a loop is bad in Java/C#:</span>
String s = <span class="cs">""</span>;
<span class="ck">for</span>(<span class="ck">int</span> i = <span class="cs">0</span>; i < <span class="cs">10000</span>; i++) {
    <span class="cm">// Creates a NEW string object in Heap 10,000 times!</span>
    s += <span class="cs">"a"</span>; 
}
<span class="cm">// Solution: Use StringBuilder!</span></div></div>`,
    mcqs:[
      {q:"What does it mean that a String is 'Immutable'?",opts:["A. It cannot be deleted","B. Once created in memory, its contents cannot be altered. Operations like concatenation create entirely new strings.","C. It can only hold letters, not numbers","D. It is encrypted"],ans:1,exp:"Immutability is great for thread safety and memory caching, but bad for performance if you do heavy string manipulation in a loop."},
      {q:"Because strings are essentially arrays of characters, what is the time complexity to find the length of a string in a C-style language (null-terminated)?",opts:["A. O(1)","B. O(log N)","C. O(N)","D. O(N^2)"],ans:2,exp:"In C, you must count characters until you hit the '\\0' terminator. (Note: High-level languages like JS/Java store the length separately, making it O(1))."},
      {q:"Why should you use a StringBuilder (Java/C#) or array.join (JS) when building massive strings in a loop?",opts:["A. To prevent O(N^2) Time Complexity caused by copying the string over and over again into new memory blocks","B. To make it readable","C. To convert them to numbers","D. Because normal strings have a 255 character limit"],ans:0,exp:"Concatenating 'A' + 'B' requires allocating space for 2 chars. Adding 'C' requires allocating space for 3 chars and copying A and B over. This scales quadratically!"},
      {q:"Which data structure is best for extremely fast autocomplete/prefix string searching (e.g., searching a dictionary)?",opts:["A. Array","B. Linked List","C. Trie (Prefix Tree)","D. Stack"],ans:2,exp:"A Trie is a specialized tree structure perfectly designed for string prefix matching."},
      {q:"How do you access the 3rd character of a string in JS/Python?",opts:["A. str.third()","B. str[2]","C. str.get(3)","D. str.char(3)"],ans:1,exp:"Strings are 0-indexed character arrays, so the 3rd character is at index 2."}
    ],
    flows:[
      {title:"Immutable String Concatenation",items:["start:s = 'Hi'","proc:s = s + 'ya'","dec:Modify original 'Hi'?","proc:(No) Create new memory for 'Hiya'","proc:Update 's' pointer","end:Old 'Hi' garbage collected"]}
    ],
    game:{icon:"🔤",title:"Word Weaver",desc:"Master string manipulation",badges:["🔤 Weaver","🧱 StringBuilder","🛡️ Immutable"],challenges:[{icon:"📝",title:"Immutability",desc:"Explain why strings are immutable",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Palindrome Checker",badge:"Symmetry",desc:"Check if a string is read the same forwards and backwards.",tags:["Strings","Algorithms"],steps:[{title:"Clean String",desc:"Remove spaces and lower case it"},{"title:"Two Pointers",desc:"Start at beginning and end, move inwards"},{"title:"Compare",desc:"If chars don't match, return false"}],code:`function isPalindrome(str) {\n  str = str.toLowerCase().replace(/\\s/g, '');\n  let left = 0, right = str.length - 1;\n  while (left < right) {\n    if (str[left] !== str[right]) return false;\n    left++; right--;\n  }\n  return true;\n}\nconsole.log(isPalindrome("Race car")); // true`}
  },
  t29: {
    tag:'Phase 1 · Data Structures', num:29,
    title:'Linked Lists',
    desc:'A linear collection of data elements where each element points to the next one.',
    theory:`<div class="card"><h3>🔗 The Chain of Nodes</h3><p>Unlike Arrays (which require contiguous memory), a <strong>Linked List</strong> stores its elements (Nodes) scattered anywhere in memory. Each Node contains two things:</p><ol><li><strong>Data:</strong> The actual value (e.g., 5).</li><li><strong>Next Pointer:</strong> A reference to the memory address of the next Node.</li></ol><h4>Array vs Linked List</h4><ul><li><strong>Insertion/Deletion at start:</strong> Linked List is <code>O(1)</code>! You just change the Head pointer. Array is <code>O(N)</code>.</li><li><strong>Random Access:</strong> Linked List is <code>O(N)</code>! You can't say "give me index 500". You must start at the head and traverse 500 links. Array is <code>O(1)</code>.</li></ul><div class="box b-vi"><h5>Singly vs Doubly</h5><p>A Singly Linked List only points forward. A <strong>Doubly Linked List</strong> has a 'prev' pointer as well, allowing backward traversal at the cost of extra memory.</p></div></div>`,
    mcqs:[
      {q:"What is the Time Complexity of finding a specific value in an unsorted Singly Linked List?",opts:["A. O(1)","B. O(log N)","C. O(N)","D. O(N^2)"],ans:2,exp:"You must start at the Head and follow the pointers one by one until you find the value."},
      {q:"Why is inserting a Node at the very beginning (Head) of a Linked List O(1), while doing so in an Array is O(N)?",opts:["A. Linked Lists are faster than Arrays","B. You don't have to shift any other elements; you just create the new node, point it to the old Head, and update the Head reference","C. Arrays are stored on the hard drive","D. Because the list is sorted"],ans:1,exp:"Pointer reassignment is an instant O(1) operation."},
      {q:"What does the 'Next' pointer of the final Node (the Tail) in a Singly Linked List point to?",opts:["A. The Head","B. Null","C. 0","D. Itself"],ans:1,exp:"Null signifies the end of the chain."},
      {q:"What is the primary disadvantage of a Linked List compared to an Array?",opts:["A. It uses less memory","B. It cannot store strings","C. Lack of Random Access (No O(1) index lookups) and poor Cache Locality (data is scattered in RAM)","D. Deletion is slow"],ans:2,exp:"CPUs love contiguous memory (Arrays) because they can load chunks into the L1 cache. Scattered nodes cause cache misses."},
      {q:"What makes a Doubly Linked List different from a Singly Linked List?",opts:["A. It holds two data values per node","B. Each node has a pointer to the Next node AND a pointer to the Previous node","C. It runs twice as fast","D. It is stored in two places"],ans:1,exp:"This allows O(1) deletion if you have the node reference, and backward traversal."}
    ],
    flows:[
      {title:"O(1) Prepend Flow",items:["start:Head -> [A] -> [B]","proc:Create New Node [X]","proc:Set [X].next = Head ([A])","proc:Set Head = [X]","end:Head -> [X] -> [A] -> [B]"]}
    ],
    game:{icon:"🔗",title:"Chain Master",desc:"Master node pointers",badges:["🔗 Linker","🔁 Traverser","⏪ Doubly Master"],challenges:[{icon:"📝",title:"Reverse it",desc:"Explain how to reverse a linked list",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Reverse a Linked List",badge:"Pointer Pro",desc:"The classic FAANG interview question.",tags:["Algorithms","Linked List"],steps:[{title:"Init Pointers",desc:"prev = null, current = head, next = null"},{"title:"Loop",desc:"While current is not null"},{"title:"Flip Pointers",desc:"Save next, point current backwards to prev, advance prev and current"}],code:`// Node definition: {val: 1, next: null}\nfunction reverseList(head) {\n  let prev = null;\n  let current = head;\n  \n  while (current !== null) {\n    let nextTemp = current.next;\n    current.next = prev; // The flip!\n    prev = current;\n    current = nextTemp;\n  }\n  return prev; // New head\n}`}
  },
  t30: {
    tag:'Phase 1 · Data Structures', num:30,
    title:'Stack',
    desc:'A Last-In, First-Out (LIFO) data structure.',
    theory:`<div class="card"><h3>🥞 The Plate Stack</h3><p>A <strong>Stack</strong> is an abstract data type that restricts how you can insert and remove items. It follows <strong>LIFO (Last-In, First-Out)</strong>. Think of a stack of plates in a cafeteria: you can only add a plate to the top, and you can only take a plate off the top.</p><h4>Core Operations (All O(1))</h4><ul><li><strong>Push:</strong> Add an item to the top.</li><li><strong>Pop:</strong> Remove and return the top item.</li><li><strong>Peek (Top):</strong> Look at the top item without removing it.</li></ul><div class="box b-am"><h5>Common Use Cases</h5><p>The Call Stack (function execution), Undo/Redo mechanisms in text editors, and Browser History (Back button).</p></div></div>`,
    mcqs:[
      {q:"What ordering principle does a Stack follow?",opts:["A. FIFO (First In First Out)","B. LIFO (Last In First Out)","C. Random","D. Sorted"],ans:1,exp:"Last In, First Out. The most recently added item is the first one removed."},
      {q:"If you push 1, then 2, then 3 onto a stack, what will be the first item popped off?",opts:["A. 1","B. 2","C. 3","D. Null"],ans:2,exp:"3 was the last item pushed onto the top, so it is the first to be popped."},
      {q:"What is the Time Complexity of Push and Pop operations?",opts:["A. O(1)","B. O(log N)","C. O(N)","D. O(N^2)"],ans:0,exp:"Because you only ever interact with the very top element, it is an instant O(1) operation."},
      {q:"Which real-world application relies heavily on a Stack data structure?",opts:["A. A printer queue","B. The 'Undo' feature in a text editor (Ctrl+Z)","C. A database index","D. Google Maps routing"],ans:1,exp:"Every action you take is pushed. When you hit Undo, it pops the last action off the stack."},
      {q:"Can a Stack be implemented using an Array under the hood?",opts:["A. Yes, using push() and pop() methods on the array","B. No, it must use a Linked List","C. Only in Java","D. No, arrays are FIFO"],ans:0,exp:"In JS/Python, an array IS a stack if you strictly restrict yourself to only using push() and pop()."}
    ],
    flows:[
      {title:"Stack Operations (LIFO)",items:["start:Empty Stack","proc:Push(A) -> [A]","proc:Push(B) -> [A, B]","proc:Pop() returns B -> [A]","end:Top is now A"]}
    ],
    game:{icon:"🥞",title:"Stacker",desc:"Master LIFO logic",badges:["🥞 Pusher","📤 Popper","👀 Peeker"],challenges:[{icon:"📝",title:"Identify LIFO",desc:"List 3 real world LIFO examples",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Valid Parentheses",badge:"Syntax Checker",desc:"Use a stack to check if brackets are closed properly (e.g. '{[()]}').",tags:["Algorithms","Stack"],steps:[{title:"Loop",desc:"Iterate through string"},{"title:"Push Openers",desc:"If it's '(', '{', or '[', push to stack"},{"title:"Pop Matchers",desc:"If it's a closer, pop stack and check if it matches"}],code:`function isValid(s) {\n  let stack = [];\n  let map = { ')':'(', '}':'{', ']':'[' };\n  \n  for (let char of s) {\n    if (char === '(' || char === '{' || char === '[') {\n      stack.push(char);\n    } else {\n      let top = stack.pop();\n      if (top !== map[char]) return false;\n    }\n  }\n  return stack.length === 0;\n}`}
  },
  t31: {
    tag:'Phase 1 · Data Structures', num:31,
    title:'Queue',
    desc:'A First-In, First-Out (FIFO) data structure.',
    theory:`<div class="card"><h3>🚶🚶🚶 The Waiting Line</h3><p>A <strong>Queue</strong> is the opposite of a Stack. It follows <strong>FIFO (First-In, First-Out)</strong>. Think of a line at a grocery store: the first person to get in line is the first person to be served.</p><h4>Core Operations</h4><ul><li><strong>Enqueue (Add):</strong> Add an item to the <em>rear/tail</em> of the queue.</li><li><strong>Dequeue (Remove):</strong> Remove an item from the <em>front/head</em> of the queue.</li></ul><div class="box b-ro"><h5>⚠️ Array Queue Pitfall</h5><p>If you implement a Queue using a basic Array in JS/Python by using <code>array.shift()</code> to Dequeue, it takes <strong>O(N)</strong> time! Every shift forces all other elements to move left. A true O(1) Queue must be implemented using a Linked List or a Ring Buffer.</p></div></div>`,
    mcqs:[
      {q:"What ordering principle does a Queue follow?",opts:["A. LIFO (Last In First Out)","B. FIFO (First In First Out)","C. Random","D. Sorted"],ans:1,exp:"First In, First Out. The oldest item in the queue is processed first."},
      {q:"Which real-world scenario perfectly matches a Queue?",opts:["A. Browser back history","B. A printer managing print jobs","C. Undoing text","D. Searching a database"],ans:1,exp:"The first print job submitted is the first one printed."},
      {q:"If you Enqueue 1, then 2, then 3, what will the first Dequeue operation return?",opts:["A. 1","B. 2","C. 3","D. Null"],ans:0,exp:"1 was first in, so it is first out."},
      {q:"Why is using a standard Array for a Queue (push to add, shift to remove) bad for performance on massive datasets?",opts:["A. Arrays cannot hold data","B. Array.shift() is O(N) because it forces every remaining element to shift left by one index","C. Array.push() is O(N)","D. It causes memory leaks"],ans:1,exp:"To achieve true O(1) enqueue and dequeue, use a Linked List or pointers."},
      {q:"Which algorithm relies heavily on a Queue?",opts:["A. DFS (Depth First Search)","B. BFS (Breadth First Search)","C. Binary Search","D. Quick Sort"],ans:1,exp:"BFS explores neighbors level by level, utilizing a FIFO queue to keep track of nodes to visit next."}
    ],
    flows:[
      {title:"Queue Operations (FIFO)",items:["start:Empty Queue","proc:Enqueue(A) -> [A]","proc:Enqueue(B) -> [A, B]","proc:Dequeue() returns A -> [B]","end:Front is now B"]}
    ],
    game:{icon:"🚶",title:"Line Manager",desc:"Master FIFO logic",badges:["🚶 FIFO Fanatic","📥 Enqueuer","📤 Dequeuer"],challenges:[{icon:"📝",title:"Identify FIFO",desc:"List 3 real world FIFO examples",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Ticket System",badge:"Support Tech",desc:"Build an O(1) Queue using an object and pointers to avoid Array.shift().",tags:["Data Structures","Queue"],steps:[{title:"Init",desc:"Use an object to store data, and head/tail counters"},{"title:"Enqueue",desc:"Add to tail, increment tail"},{"title:"Dequeue",desc:"Return head item, delete it, increment head"}],code:`class FastQueue {\n  constructor() {\n    this.items = {};\n    this.head = 0;\n    this.tail = 0;\n  }\n  enqueue(val) {\n    this.items[this.tail] = val;\n    this.tail++;\n  }\n  dequeue() {\n    if (this.head === this.tail) return null;\n    let item = this.items[this.head];\n    delete this.items[this.head];\n    this.head++;\n    return item;\n  }\n}`}
  },
"""

start_marker = "};\n\nlet userXP"
inject_idx = content.find(start_marker)

if inject_idx != -1:
    new_content = content[:inject_idx] + ",\n" + rich_content + content[inject_idx:]
    with open(html_path, "w") as f:
        f.write(new_content)
    print("Successfully generated T27-T31 rich content!")
else:
    print("Could not find injection point.")
