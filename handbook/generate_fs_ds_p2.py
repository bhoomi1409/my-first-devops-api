import re

html_path = "/Users/bhoomim/devops CI:CD/handbook/fullstack_ai_handbook.html"
with open(html_path, "r") as f:
    content = f.read()

rich_content = r"""
  t32: {
    tag:'Phase 1 · Data Structures', num:32,
    title:'Circular Queue',
    desc:'A Queue that wraps around on itself to optimize fixed-size memory.',
    theory:`<div class="card"><h3>🍩 The Ring Buffer</h3><p>A standard queue implemented via a fixed-size array wastes space. If you enqueue and dequeue elements, the 'head' pointer moves forward, leaving empty, unusable space at the start of the array. A <strong>Circular Queue (Ring Buffer)</strong> solves this by wrapping the 'tail' pointer back to the beginning of the array if there is space.</p><h4>How it works</h4><p>Instead of <code>tail = tail + 1</code>, you use the modulo operator: <code>tail = (tail + 1) % size</code>. This guarantees the pointer never exceeds the array bounds and naturally wraps around to 0.</p></div>`,
    mcqs:[
      {q:"What problem does a Circular Queue solve compared to a standard fixed-size Array Queue?",opts:["A. It solves memory leaks","B. It reuses empty spaces at the front of the array caused by previous dequeues, preventing memory waste","C. It sorts the queue","D. It encrypts the queue"],ans:1,exp:"By wrapping the tail pointer back to index 0, it behaves like an infinite loop within a fixed memory block."},
      {q:"What mathematical operator is essential for implementing a Ring Buffer / Circular Queue?",opts:["A. Addition (+)","B. Multiplication (*)","C. Modulo (%)","D. Division (/)"],ans:2,exp:"Modulo forces a number to wrap around (e.g., if size is 5, then 5 % 5 = 0, wrapping the pointer back to start)."},
      {q:"What is a common real-world use case for a Ring Buffer?",opts:["A. Sorting large databases","B. Streaming audio/video buffers, where old data is constantly overwritten by new data once processed","C. Hashing passwords","D. Storing files on a hard drive"],ans:1,exp:"Audio hardware often uses ring buffers so the CPU can dump audio data in, and the soundcard can read it out continuously."},
      {q:"If the Head pointer catches up and equals the Tail pointer in a Circular Queue, what does it mean?",opts:["A. The queue is full (or entirely empty, depending on implementation/flags)","B. The program crashed","C. The queue is sorted","D. The array is infinite"],ans:0,exp:"Usually, you keep a 'size' or 'count' variable to differentiate between completely full and completely empty."},
      {q:"What is the Time Complexity for Enqueue and Dequeue in a Circular Queue?",opts:["A. O(1)","B. O(log N)","C. O(N)","D. O(N^2)"],ans:0,exp:"Because you are just moving two pointers (head and tail) and writing to an array index, it is instant O(1)."}
    ],
    flows:[
      {title:"Pointer Wrap Around",items:["start:Array Size 3. Tail is at Index 2","proc:Enqueue(D)","proc:Calculate: (2 + 1) % 3 = 0","end:Tail wraps to Index 0"]}
    ],
    game:{icon:"🍩",title:"Ringmaster",desc:"Master circular arrays",badges:["🍩 Bufferer","♻️ Recycler","🧮 Modulo Master"],challenges:[{icon:"📝",title:"Modulo Math",desc:"Calculate (4+1)%5",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Audio Buffer",badge:"Audio Engineer",desc:"Implement a simple fixed-size Ring Buffer.",tags:["Data Structures","Queue"],steps:[{title:"Init",desc:"Create array of size 3, set head=0, tail=0"},{"title:"Enqueue",desc:"Add item, update tail with modulo"},{"title:"Test Wrap",desc:"Add 4 items and see the first overwritten"}],code:`class RingBuffer {\n  constructor(size) {\n    this.q = new Array(size);\n    this.size = size;\n    this.head = 0;\n    this.tail = 0;\n  }\n  enqueue(val) {\n    this.q[this.tail] = val;\n    this.tail = (this.tail + 1) % this.size;\n  }\n}\n\nlet buf = new RingBuffer(3);\nbuf.enqueue("A"); buf.enqueue("B"); buf.enqueue("C");\nbuf.enqueue("D"); // Overwrites "A"!`}
  },
  t33: {
    tag:'Phase 1 · Data Structures', num:33,
    title:'Deque',
    desc:'Double-Ended Queue allowing insertion and removal from both ends.',
    theory:`<div class="card"><h3>↔️ The Best of Both Worlds</h3><p>A <strong>Deque</strong> (pronounced "deck") is a Double-Ended Queue. It allows you to add or remove elements from <strong>both the front and the back</strong> in <code>O(1)</code> time. It essentially combines a Stack and a Queue into one data structure.</p><h4>Under the Hood</h4><p>A Deque is usually implemented using a <strong>Doubly Linked List</strong> or a specialized dynamic array. If you only use one side, it acts exactly like a Stack. If you push on one side and pop on the other, it acts like a Queue.</p></div>`,
    mcqs:[
      {q:"What does Deque stand for?",opts:["A. Data Execution Queue","B. Double-Ended Queue","C. Direct Entry Queue","D. Dynamic Equality"],ans:1,exp:"It allows operations at both the Head and the Tail."},
      {q:"What are the Time Complexities of adding/removing from either end of a Deque?",opts:["A. O(1)","B. O(log N)","C. O(N)","D. O(N^2)"],ans:0,exp:"Because it maintains pointers to both the front and back, operations on the ends are instant."},
      {q:"Which standard data structure does a Deque mimic if you only ever add/remove from the Front?",opts:["A. Queue","B. Stack","C. Tree","D. Graph"],ans:1,exp:"LIFO (Last In First Out) behavior = Stack."},
      {q:"Which standard data structure does a Deque mimic if you add to the Back and remove from the Front?",opts:["A. Queue","B. Stack","C. Array","D. Set"],ans:0,exp:"FIFO (First In First Out) behavior = Queue."},
      {q:"Why is a Doubly Linked List the most common underlying implementation for a Deque?",opts:["A. Because it's required by Java","B. Because it has pointers to both the Next and Previous nodes, making removal from the tail O(1)","C. Because it sorts automatically","D. It uses less memory"],ans:1,exp:"A Singly linked list can easily add/remove at the head, but removing from the tail is O(N) because you can't step backwards to update the new tail pointer."}
    ],
    flows:[
      {title:"Deque Flexibility",items:["start:Empty Deque []","proc:addFront(1) -> [1]","proc:addBack(2) -> [1, 2]","proc:removeBack() -> [1]","end:removeFront() -> []"]}
    ],
    game:{icon:"↔️",title:"Deck Hand",desc:"Master double-ended queues",badges:["↔️ Double Ender","🥞 Stack Mimic","🚶 Queue Mimic"],challenges:[{icon:"📝",title:"Stack Mimic",desc:"Use a Deque as a Stack",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Browser History",badge:"Navigator",desc:"Use a Deque to manage Forward and Back browser history.",tags:["Algorithms","Deque"],steps:[{title:"Init",desc:"Create Deque (use JS array for simplicity)"},{"title:"Visit Page",desc:"Add to front of deque"},{"title:"Back/Forward",desc:"Pop from one end, push to another"}],code:`// Conceptual Array-based Deque\nclass HistoryDeque {\n  constructor() { this.pages = []; }\n  visit(url) { \n    this.pages.unshift(url); // addFront\n  }\n  goBack() {\n    let old = this.pages.shift(); // removeFront\n    this.pages.push(old); // addBack\n  }\n}`}
  },
  t34: {
    tag:'Phase 1 · Data Structures', num:34,
    title:'HashMap',
    desc:'A key-value store providing O(1) average lookup times.',
    theory:`<div class="card"><h3>🗺️ The Ultimate Lookup Table</h3><p>A <strong>HashMap</strong> (Dictionary in Python, Object/Map in JS) stores data in <strong>Key-Value pairs</strong> (e.g., "username" -> "Bhoomi"). It provides incredibly fast <code>O(1)</code> lookups, insertions, and deletions.</p><h4>How does it achieve O(1) without contiguous memory?</h4><ol><li>You provide a Key (e.g., "apple").</li><li>A <strong>Hash Function</strong> scrambles the word "apple" into a specific integer index (e.g., 42).</li><li>The Value is stored in an underlying Array at index 42.</li><li>When you ask for "apple" later, it hashes it again to 42, instantly jumping to the data!</li></ol><div class="box b-ro"><h5>⚠️ Hash Collisions</h5><p>Sometimes, two different keys hash to the same exact index. This is a <strong>Collision</strong>. HashMaps resolve this by storing a Linked List at that index, chaining the collided values together.</p></div></div>`,
    mcqs:[
      {q:"What is the average Time Complexity for lookup, insertion, and deletion in a HashMap?",opts:["A. O(1)","B. O(log N)","C. O(N)","D. O(N^2)"],ans:0,exp:"Hash functions provide direct array index access, making operations constant time."},
      {q:"What does a Hash Function do?",opts:["A. Encrypts passwords securely","B. Converts a given Key (like a String) into an Integer index for the underlying array","C. Sorts the values","D. Deletes old data"],ans:1,exp:"The magic of the HashMap is transforming any Key into an Array Index."},
      {q:"What is a Hash Collision?",opts:["A. When the HashMap runs out of memory","B. When two DIFFERENT keys are converted into the SAME integer index by the hash function","C. When the program crashes","D. When you delete a key twice"],ans:1,exp:"Hash functions are imperfect. 'dog' and 'god' might both hash to index 5."},
      {q:"How is a Hash Collision typically resolved (Separate Chaining)?",opts:["A. The second key overwrites the first","B. The HashMap crashes","C. The index stores a Linked List of all key-value pairs that collided there","D. It stores it in the Cloud"],ans:2,exp:"If you look up a collided key, it jumps to the index, then linearly traverses the small Linked List to find the exact match."},
      {q:"Why wouldn't you use a HashMap for everything?",opts:["A. They are slow","B. They don't maintain insertion or sorted order, and use more memory overhead than arrays","C. They can't store strings","D. They require an internet connection"],ans:1,exp:"If you need order or sorting, use an Array or a Tree. HashMaps are purely for fast, unordered lookups."}
    ],
    flows:[
      {title:"HashMap Lookup Flow",items:["start:map.get('user1')","proc:Hash('user1') -> Index 7","proc:Jump to Array[7]","dec:Collision?","proc:(No) Return Value","end:(Yes) Traverse List to find 'user1'"]}
    ],
    game:{icon:"🗺️",title:"Hash Slinger",desc:"Master O(1) lookups",badges:["🗺️ Mapper","🔑 Key Master","💥 Collision Resolver"],challenges:[{icon:"📝",title:"Identify Hash",desc:"Explain how a hash function works",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Frequency Counter",badge:"Data Analyst",desc:"Use a HashMap to count the occurrences of characters in a string in O(N) time.",tags:["Algorithms","HashMap"],steps:[{title:"Init Map",desc:"Create an empty object {}"},{"title:"Loop String",desc:"Iterate over each char"},{"title:"Count",desc:"If char exists in map, +1. Else set to 1"}],code:`function countChars(str) {\n  let map = {};\n  for (let char of str) {\n    if (map[char]) map[char]++;\n    else map[char] = 1;\n  }\n  return map;\n}\nconsole.log(countChars("hello")); // {h:1, e:1, l:2, o:1}`}
  },
  t35: {
    tag:'Phase 1 · Data Structures', num:35,
    title:'HashSet',
    desc:'A collection of unique elements, powered by a HashMap.',
    theory:`<div class="card"><h3>🎯 The Filter of Uniqueness</h3><p>A <strong>HashSet</strong> (or just <code>Set</code> in JS/Python) is exactly like a HashMap, but it <em>only stores Keys, not Values</em>. Its primary superpower is guaranteeing that <strong>every item in the set is 100% unique</strong>.</p><h4>Why use it?</h4><ul><li><strong>Deduplication:</strong> Easiest way to remove duplicates from an Array.</li><li><strong>O(1) Presence Check:</strong> Need to know if "User_123" has already voted? <code>set.has("User_123")</code> is instant. Doing <code>array.includes("User_123")</code> is slow O(N).</li></ul><div class="cb"><span class="cm">// JavaScript Set Example</span>
<span class="ck">let</span> <span class="cv">votedUsers</span> = <span class="ck">new</span> Set();
votedUsers.add(<span class="cs">"Bhoomi"</span>);
votedUsers.add(<span class="cs">"Bhoomi"</span>); <span class="cm">// Ignored! Already exists.</span>

console.log(votedUsers.has(<span class="cs">"Bhoomi"</span>)); <span class="cm">// true (O(1) time)</span></div></div>`,
    mcqs:[
      {q:"What is the defining characteristic of a HashSet?",opts:["A. It keeps elements perfectly sorted","B. It guarantees all elements inside it are unique (no duplicates)","C. It encrypts data","D. It only stores numbers"],ans:1,exp:"Sets represent mathematical sets: collections of distinct objects."},
      {q:"Under the hood, how is a HashSet usually implemented?",opts:["A. As a Linked List","B. As a HashMap where the Values are just dummy data (e.g. 'true') and the elements are the Keys","C. As a Tree","D. As a 2D Array"],ans:1,exp:"Because it uses a HashMap's hash function, it inherits the O(1) lookup speeds."},
      {q:"What is the Time Complexity of checking if an item exists in a HashSet (set.has(item))?",opts:["A. O(1)","B. O(log N)","C. O(N)","D. O(N^2)"],ans:0,exp:"Just like a HashMap, it hashes the item and jumps straight to the index."},
      {q:"What is the fastest way to remove all duplicate values from a massive Array?",opts:["A. Nested for-loops (O(N^2))","B. Pass the Array into a HashSet, then convert it back to an Array (O(N))","C. Sort the array first","D. Use regex"],ans:1,exp:"Sets automatically swallow duplicates. `[...new Set(array)]` is the standard JS deduplication trick."},
      {q:"Like HashMaps, what do HashSets lack?",opts:["A. Speed","B. Ordered/Indexed traversal (You can't do set[5])","C. Uniqueness","D. Memory efficiency"],ans:1,exp:"HashSets scatter data randomly based on hash functions, so they have no inherent order."}
    ],
    flows:[
      {title:"Set Deduplication",items:["start:Array [1, 2, 2, 3]","proc:new Set(Array)","proc:Adds 1","proc:Adds 2","proc:Ignores second 2","end:Set contains {1, 2, 3}"]}
    ],
    game:{icon:"🎯",title:"The Deduplicator",desc:"Master unique collections",badges:["🎯 Unique Sniper","🗑️ Dupe Deleter","⚡ O(1) Checker"],challenges:[{icon:"📝",title:"Dedupe",desc:"Remove dupes from [1,1,2,2]",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Instant Validation",badge:"Bouncer",desc:"Use a Set to instantly check if an IP is banned.",tags:["Algorithms","Sets"],steps:[{title:"Ban List",desc:"Create a Set of banned IPs"},{"title:"O(1) Check",desc:"Write function using set.has() to allow/deny"}],code:`let bannedIPs = new Set(["192.168.1.1", "10.0.0.5"]);\n\nfunction checkAccess(ip) {\n  if (bannedIPs.has(ip)) {\n    console.log("Access Denied");\n  } else {\n    console.log("Welcome!");\n  }\n}\ncheckAccess("10.0.0.5"); // Denied!`}
  },
  t36: {
    tag:'Phase 1 · Data Structures', num:36,
    title:'TreeMap',
    desc:'A key-value Map that automatically keeps its keys sorted.',
    theory:`<div class="card"><h3>🌲 The Sorted Map</h3><p>While a HashMap is incredibly fast <code>O(1)</code>, it destroys the order of your data. If you need a key-value store that <strong>always remains sorted by key</strong>, you use a <strong>TreeMap</strong> (often built using a Red-Black Tree).</p><h4>Trade-offs</h4><ul><li><strong>HashMap:</strong> <code>O(1)</code> lookup/insert. Unordered.</li><li><strong>TreeMap:</strong> <code>O(log N)</code> lookup/insert. Always perfectly sorted.</li></ul><div class="box b-cy"><h5>Use Case</h5><p>Imagine a live leaderboard for a game. You want to store PlayerScore -> PlayerName. You need to constantly fetch the "Top 5 players". A TreeMap keeps the scores sorted automatically as they are inserted, so fetching the top 5 is trivial.</p></div></div>`,
    mcqs:[
      {q:"What is the primary feature of a TreeMap over a standard HashMap?",opts:["A. It is faster","B. It automatically maintains its keys in a sorted order","C. It uses less memory","D. It only stores strings"],ans:1,exp:"The 'Tree' part ensures data is stored in a sorted, navigable hierarchy."},
      {q:"Under the hood, what data structure powers a TreeMap?",opts:["A. An Array","B. A Hash Function","C. A self-balancing Binary Search Tree (like a Red-Black Tree)","D. A Linked List"],ans:2,exp:"Self-balancing trees ensure that insertions and lookups remain O(log N) and perfectly sorted."},
      {q:"What is the Time Complexity for inserting a new key into a TreeMap?",opts:["A. O(1)","B. O(log N)","C. O(N)","D. O(N^2)"],ans:1,exp:"The tree must traverse down its branches to find the correct sorted spot, which takes logarithmic time."},
      {q:"If you need to iterate through your keys in alphabetical order, which should you use?",opts:["A. HashMap","B. TreeMap","C. HashSet","D. Queue"],ans:1,exp:"A HashMap guarantees no order. A TreeMap guarantees sorted order."},
      {q:"Does JavaScript have a native TreeMap class?",opts:["A. Yes","B. No, JS only has 'Map' (which remembers insertion order, but does NOT auto-sort by key value)","C. Yes, via Node.js","D. Yes, 'SortedMap'"],ans:1,exp:"In JS, if you need a TreeMap, you usually have to write one or import a library. Java and C++ have them natively."}
    ],
    flows:[
      {title:"TreeMap Insertion",items:["start:Insert(Key: 50)","dec:Root is 40. 50 > 40?","proc:(Yes) Go Right","dec:Next is 60. 50 < 60?","proc:(Yes) Go Left","end:Insert 50 as child"]}
    ],
    game:{icon:"🌲",title:"Tree Hugger",desc:"Master sorted maps",badges:["🌲 Sorter","⚖️ Balancer","📈 LogN Ranger"],challenges:[{icon:"📝",title:"Compare",desc:"Contrast HashMap vs TreeMap speed",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Live Leaderboard (Conceptual)",badge:"Scorekeeper",desc:"Understand why a TreeMap is perfect for sorted data.",tags:["Concepts","Trees"],steps:[{title:"Concept",desc:"Insert scores 100, 50, 200 into a tree"},{"title:"Auto-Sort",desc:"Tree aligns to 50 -> 100 -> 200"},{"title:"Query",desc:"Extract highest instantly by going to far right node"}],code:`// JS lacks TreeMap, but conceptually:\n// treeMap.put(100, "Bhoomi")\n// treeMap.put(50, "Alice")\n// treeMap.put(200, "Bob")\n\n// console.log(treeMap.keys()); \n// Output: [50, 100, 200] (Always sorted!)`}
  },
"""

start_marker = "};\n\nlet userXP"
inject_idx = content.find(start_marker)

if inject_idx != -1:
    new_content = content[:inject_idx] + ",\n" + rich_content + content[inject_idx:]
    with open(html_path, "w") as f:
        f.write(new_content)
    print("Successfully generated T32-T36 rich content!")
else:
    print("Could not find injection point.")
