import re

html_path = "/Users/bhoomim/devops CI:CD/handbook/fullstack_ai_handbook.html"
with open(html_path, "r") as f:
    content = f.read()

rich_content = r"""
  t37: {
    tag:'Phase 1 · Data Structures', num:37,
    title:'Heap',
    desc:'A specialized tree-based data structure that satisfies the heap property (Min/Max).',
    theory:`<div class="card"><h3>⛰️ The King of the Hill</h3><p>A <strong>Heap</strong> is a complete binary tree where the parent node is always <em>greater than</em> (Max-Heap) or <em>less than</em> (Min-Heap) its children.</p><h4>The Magic of Arrays</h4><p>Even though we visualize Heaps as Trees, they are almost always implemented under the hood using a flat <strong>Array</strong>! Because they are "complete" trees (filled left to right), we can use math to find parents/children instantly.</p><div class="cb"><span class="cm">// For a node at index i:</span>
<span class="ck">Left Child</span> = <span class="cs">2 * i + 1</span>
<span class="ck">Right Child</span> = <span class="cs">2 * i + 2</span>
<span class="ck">Parent</span> = <span class="cs">Math.floor((i - 1) / 2)</span></div></div>`,
    mcqs:[
      {q:"What is the defining rule of a Max-Heap?",opts:["A. The left child is always smaller than the right child","B. The parent node is always greater than or equal to its children","C. The tree must be perfectly balanced","D. It can only hold 10 items"],ans:1,exp:"This guarantees that the absolute largest element in the entire structure is always sitting at the very top (the root)."},
      {q:"Why are Heaps usually implemented as Arrays instead of Node objects with pointers?",opts:["A. Arrays are required by law","B. Because heaps are Complete Binary Trees, you can easily calculate child/parent positions using simple math (2*i + 1) without wasting memory on pointers","C. Node pointers are too fast","D. Arrays sort themselves"],ans:1,exp:"This saves massive amounts of memory and improves CPU cache locality."},
      {q:"What is the Time Complexity of finding the Maximum value in a Max-Heap?",opts:["A. O(1)","B. O(log N)","C. O(N)","D. O(N^2)"],ans:0,exp:"The max value is always at the root (index 0 of the array). It's instant."},
      {q:"What is the Time Complexity of inserting a new value into a Heap?",opts:["A. O(1)","B. O(log N)","C. O(N)","D. O(N^2)"],ans:1,exp:"You add it to the bottom, then 'bubble it up' by comparing it to its parents, which takes log N time."},
      {q:"Are the elements in a Heap perfectly sorted from smallest to largest?",opts:["A. Yes","B. No, a Heap is only 'partially sorted'. The only guarantee is the parent-child relationship. Siblings have no guaranteed order.","C. Only in Java","D. Yes, if you use a Min-Heap"],ans:1,exp:"Heaps are not for full sorting (like a BST). They are optimized purely for quickly grabbing the Min or Max element."}
    ],
    flows:[
      {title:"Heap Insertion (Bubble Up)",items:["start:Insert 100 at bottom","dec:Is 100 > Parent(50)?","proc:(Yes) Swap them","dec:Is 100 > Parent(90)?","proc:(Yes) Swap them","end:100 is now Root"]}
    ],
    game:{icon:"⛰️",title:"King of the Hill",desc:"Master heap mechanics",badges:["⛰️ Mountaineer","🫧 Bubbler","🧮 Index Math Pro"],challenges:[{icon:"📝",title:"Calculate Index",desc:"Find left child of index 3",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Heap Math",badge:"Calculator",desc:"Write functions to get child indices in an array-based heap.",tags:["Algorithms","Heap"],steps:[{title:"Left Child",desc:"Return 2 * i + 1"},{"title:"Right Child",desc:"Return 2 * i + 2"},{"title:"Parent",desc:"Return floor((i - 1) / 2)"}],code:`function getLeftChildIndex(i) { return 2 * i + 1; }\nfunction getRightChildIndex(i) { return 2 * i + 2; }\nfunction getParentIndex(i) { return Math.floor((i - 1) / 2); }\n\nconsole.log(getLeftChildIndex(2)); // 5`}
  },
  t38: {
    tag:'Phase 1 · Data Structures', num:38,
    title:'Priority Queue',
    desc:'A Queue where elements are dequeued based on priority, not arrival time.',
    theory:`<div class="card"><h3>🚨 VIP Access</h3><p>A standard Queue is FIFO (first come, first served). A <strong>Priority Queue</strong> serves elements based on their assigned priority. (e.g., An ER waiting room: a heart attack patient is treated before someone with a paper cut, regardless of who arrived first).</p><h4>The Heap Connection</h4><p>Under the hood, Priority Queues are almost always implemented using a <strong>Heap</strong>. Why? Because you always want to Dequeue the highest priority item instantly <code>O(1)</code>, and inserting new items into a Heap is very fast <code>O(log N)</code>.</p></div>`,
    mcqs:[
      {q:"How does a Priority Queue differ from a standard Queue?",opts:["A. It's slower","B. Items are dequeued based on priority level, not insertion order (FIFO)","C. It uses a Stack under the hood","D. It can only hold numbers"],ans:1,exp:"High priority elements jump to the front of the line."},
      {q:"What underlying data structure is typically used to build an efficient Priority Queue?",opts:["A. Linked List","B. Heap (Min-Heap or Max-Heap)","C. Stack","D. Standard Array"],ans:1,exp:"A Heap guarantees the highest (or lowest) priority element is always at the root, making dequeue O(log N) to rebalance, and peek O(1)."},
      {q:"If you implement a Priority Queue using a standard unsorted Array, what is the time complexity to Dequeue the highest priority item?",opts:["A. O(1)","B. O(log N)","C. O(N)","D. O(N^2)"],ans:2,exp:"You would have to scan the entire array every time to find the highest priority item, which is terribly slow O(N)."},
      {q:"What is a common real-world use case for a Priority Queue?",opts:["A. Reversing a string","B. Dijkstra's Shortest Path algorithm (always expanding the shortest known path next)","C. Storing user passwords","D. HTML parsing"],ans:1,exp:"Network routing, OS task scheduling, and pathfinding algorithms rely heavily on PQs."},
      {q:"If two elements have the EXACT SAME priority in a Priority Queue, how are they handled?",opts:["A. The program crashes","B. Usually, they are then processed based on standard FIFO order (whoever arrived first)","C. They are both deleted","D. They are merged"],ans:1,exp:"Most robust PQ implementations fall back to arrival time for tie-breakers."}
    ],
    flows:[
      {title:"Priority Queue Operations",items:["start:Enqueue(Job A, Pri: 2)","proc:Enqueue(Job B, Pri: 10)","proc:Enqueue(Job C, Pri: 5)","dec:Dequeue() Called!","proc:Returns Job B (Pri: 10)","end:Heap Rebalances"]}
    ],
    game:{icon:"🚨",title:"Triage",desc:"Master priority sorting",badges:["🚨 VIP Manager","🏥 ER Doctor"," Dijkstra Fan"],challenges:[{icon:"📝",title:"Identify PQ",desc:"List 3 Priority Queue use cases",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Basic Priority Queue",badge:"VIP Bouncer",desc:"Implement a slow Array-based PQ (for conceptual learning).",tags:["Data Structures","Queue"],steps:[{title:"Init Array",desc:"Create empty array"},{"title:"Enqueue",desc:"Push {val, priority} to array and sort it"},{"title:"Dequeue",desc:"Shift the first item off the array"}],code:`class SlowPQ {\n  constructor() { this.q = []; }\n  enqueue(val, pri) {\n    this.q.push({val, pri});\n    // Slow O(N log N) insertion!\n    this.q.sort((a,b) => b.pri - a.pri);\n  }\n  dequeue() {\n    return this.q.shift();\n  }\n}\n\nlet pq = new SlowPQ();\npq.enqueue("Papercut", 1);\npq.enqueue("Heart Attack", 10);\nconsole.log(pq.dequeue().val); // Heart Attack`}
  },
  t39: {
    tag:'Phase 1 · Data Structures', num:39,
    title:'Binary Trees',
    desc:'A hierarchical structure where each node has at most two children.',
    theory:`<div class="card"><h3>🌳 Branching Out</h3><p>Unlike Arrays and Linked Lists (which are linear), Trees are hierarchical. A <strong>Binary Tree</strong> is a tree where every node can have <em>at most two children</em> (referred to as Left and Right).</p><h4>Key Terminology</h4><ul><li><strong>Root:</strong> The very top node.</li><li><strong>Leaf:</strong> A node with no children.</li><li><strong>Depth/Height:</strong> How many levels deep the tree goes.</li></ul><h4>Traversals (DFS)</h4><ul><li><strong>Pre-order:</strong> Root -> Left -> Right (Good for copying trees).</li><li><strong>In-order:</strong> Left -> Root -> Right (Gets values in sorted order for BSTs).</li><li><strong>Post-order:</strong> Left -> Right -> Root (Good for deleting trees from bottom up).</li></ul></div>`,
    mcqs:[
      {q:"What is the maximum number of children a node can have in a Binary Tree?",opts:["A. 1","B. 2","C. 3","D. Infinite"],ans:1,exp:"Bi = two. Left child and Right child."},
      {q:"What is a 'Leaf' node?",opts:["A. The top node","B. A node that has zero children (the bottom of the branches)","C. A node that is green","D. A node with two children"],ans:1,exp:"Leaves are the endpoints of the tree."},
      {q:"Which traversal method visits the Left child, then the Root, then the Right child?",opts:["A. Pre-order","B. In-order","C. Post-order","D. Out-order"],ans:1,exp:"In-order traversal is extremely important for Binary Search Trees because it prints the values in perfectly sorted ascending order."},
      {q:"Why are Trees considered non-linear data structures?",opts:["A. Because they are slow","B. Because data branches out in multiple paths, rather than a single sequential line like an Array","C. Because they use Math","D. Because they don't use pointers"],ans:1,exp:"Linear = one path. Hierarchical = many branching paths."},
      {q:"What is a 'Perfect' Binary Tree?",opts:["A. A tree with no bugs","B. A tree where every internal node has exactly 2 children and all leaf nodes are on the exact same level","C. A tree with only one node","D. A tree that only stores the number 1"],ans:1,exp:"A perfect tree is completely filled, looking like a perfect triangle."}
    ],
    flows:[
      {title:"In-Order Traversal",items:["start:Visit Left Subtree","proc:Process Root Node Data","end:Visit Right Subtree"]}
    ],
    game:{icon:"🌳",title:"Arborist",desc:"Master tree hierarchies",badges:["🌳 Brancher","🍂 Leaf Peeper","🚶 Traverser"],challenges:[{icon:"📝",title:"Traversal",desc:"List the 3 DFS traversal orders",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Tree Node Setup",badge:"Planter",desc:"Create a basic Binary Tree Node class in JavaScript.",tags:["Data Structures","Trees"],steps:[{title:"Class Node",desc:"Create class Node"},{"title:"Constructor",desc:"Set this.val, this.left = null, this.right = null"},{"title:"Link Them",desc:"Create root, assign root.left and root.right"}],code:`class TreeNode {\n  constructor(val) {\n    this.val = val;\n    this.left = null;\n    this.right = null;\n  }\n}\n\nlet root = new TreeNode(10);\nroot.left = new TreeNode(5);\nroot.right = new TreeNode(15);\n\nconsole.log(root.left.val); // 5`}
  },
  t40: {
    tag:'Phase 1 · Data Structures', num:40,
    title:'BST',
    desc:'Binary Search Tree: A binary tree optimized for fast searching.',
    theory:`<div class="card"><h3>🔍 The Halving Machine</h3><p>A <strong>Binary Search Tree (BST)</strong> has a strict rule that makes searching incredibly fast <code>O(log N)</code>:</p><ol><li>Everything to the <strong>Left</strong> of a node is SMALLER than the node.</li><li>Everything to the <strong>Right</strong> of a node is LARGER than the node.</li></ol><h4>Why is it fast?</h4><p>If you are looking for the number 75, and the root is 50, you instantly know to ignore the entire left half of the tree! You just halved your search space in a single step (Logarithmic time).</p><div class="box b-ro"><h5>⚠️ The Unbalanced Trap</h5><p>If you insert sorted data (1, 2, 3, 4, 5) into a basic BST, every node becomes a right child. The tree devolves into a straight line (a Linked List), and search time degrades from <code>O(log N)</code> to terrible <code>O(N)</code>!</p></div></div>`,
    mcqs:[
      {q:"What is the golden rule of a Binary Search Tree (BST)?",opts:["A. Left child must be > Root, Right child must be < Root","B. Left child < Root, Right child > Root (for all nodes)","C. All nodes must be red or black","D. It can only hold 3 items"],ans:1,exp:"This strict left-smaller, right-larger rule is what allows binary search to work."},
      {q:"What is the average Time Complexity to find a value in a balanced BST?",opts:["A. O(1)","B. O(log N)","C. O(N)","D. O(N^2)"],ans:1,exp:"Each comparison allows you to eliminate half of the remaining tree, leading to logarithmic time."},
      {q:"What happens if you insert already-sorted data (1, 2, 3, 4, 5) into a naive BST?",opts:["A. It balances perfectly","B. It crashes","C. It degrades into a straight line (a Linked List), destroying the O(log N) speed and making it O(N)","D. It sorts them backward"],ans:2,exp:"This is the fatal flaw of a basic BST, which is solved by self-balancing trees like AVL or Red-Black trees."},
      {q:"Which traversal method on a BST will print the values in perfectly sorted ascending order?",opts:["A. Pre-order","B. Post-order","C. In-order","D. Breadth-First"],ans:2,exp:"In-order traversal visits Left (smallest), then Root, then Right (largest)."},
      {q:"If a BST root is 100, where would the number 45 eventually be placed?",opts:["A. Somewhere in the Right subtree","B. Somewhere in the Left subtree","C. At the root","D. It gets deleted"],ans:1,exp:"45 is less than 100, so it must go to the left."}
    ],
    flows:[
      {title:"BST Search Flow (Target: 75)",items:["start:Root is 50","dec:75 > 50?","proc:(Yes) Go Right to 80","dec:75 < 80?","proc:(Yes) Go Left to 75","end:Found 75!"]}
    ],
    game:{icon:"🔍",title:"Search Sniper",desc:"Master O(log N) searching",badges:["🔍 Binary Sniper","⚖️ Balancer","📉 Halver"],challenges:[{icon:"📝",title:"Left or Right",desc:"Decide where 60 goes if root is 50",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"BST Search Logic",badge:"Halver",desc:"Write a recursive function to find a value in a BST.",tags:["Algorithms","BST"],steps:[{title:"Base Case",desc:"If node is null, return false"},{"title:"Match",desc:"If val === node.val, return true"},{"title:"Recursive Search",desc:"If val < node.val search left, else search right"}],code:`function searchBST(node, target) {\n  if (node === null) return false;\n  if (node.val === target) return true;\n  \n  if (target < node.val) {\n    return searchBST(node.left, target);\n  } else {\n    return searchBST(node.right, target);\n  }\n}`}
  },
"""

start_marker = "};\n\nlet userXP"
inject_idx = content.find(start_marker)

if inject_idx != -1:
    new_content = content[:inject_idx] + ",\n" + rich_content + content[inject_idx:]
    with open(html_path, "w") as f:
        f.write(new_content)
    print("Successfully generated T37-T40 rich content!")
else:
    print("Could not find injection point.")
