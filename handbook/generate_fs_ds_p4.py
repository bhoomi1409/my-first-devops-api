import re

html_path = "/Users/bhoomim/devops CI:CD/handbook/fullstack_ai_handbook.html"
with open(html_path, "r") as f:
    content = f.read()

rich_content = r"""
  t41: {
    tag:'Phase 1 · Data Structures', num:41,
    title:'AVL Tree',
    desc:'A self-balancing Binary Search Tree that prevents O(N) degradation.',
    theory:`<div class="card"><h3>⚖️ The Perfect Balancer</h3><p>An <strong>AVL Tree</strong> solves the fatal flaw of a standard BST (where inserting sorted data turns it into a slow O(N) linked list). It does this by aggressively ensuring the tree remains perfectly balanced after every single insertion or deletion.</p><h4>The Balance Factor</h4><p>Every node keeps track of a "Balance Factor": the height of its Left subtree minus the height of its Right subtree. If this factor ever becomes greater than 1 or less than -1, the tree immediately performs a <strong>Rotation</strong> (Left Rotation or Right Rotation) to fix itself.</p></div>`,
    mcqs:[
      {q:"What specific problem does an AVL Tree solve?",opts:["A. It solves memory leaks","B. It prevents a Binary Search Tree from becoming unbalanced (which would ruin its O(log N) search speed)","C. It sorts arrays faster","D. It encrypts the data"],ans:1,exp:"By self-balancing, it guarantees that Search, Insert, and Delete remain O(log N) in the worst-case scenario."},
      {q:"How does an AVL Tree maintain its balance?",opts:["A. By deleting random nodes","B. By calculating a Balance Factor and performing Left or Right 'Rotations' when the tree gets too heavy on one side","C. By using a HashMap","D. By storing data in an Array"],ans:1,exp:"Rotations act like a seesaw, lifting the heavy side up to become the new root of that subtree."},
      {q:"What is the strictest acceptable Balance Factor (Left Height - Right Height) for a node in an AVL tree?",opts:["A. 0","B. -1, 0, or 1","C. Any number","D. -5 to 5"],ans:1,exp:"If the difference hits 2 or -2, a rotation is immediately triggered."},
      {q:"Why might you choose a Red-Black Tree over an AVL Tree in a real-world database?",opts:["A. Red-Black trees are faster at searching","B. AVL Trees are SO strictly balanced that they spend too much CPU time performing rotations during insertions. Red-Black trees are slightly less strict, making insertions faster.","C. AVL Trees use strings","D. Red-Black trees use less memory"],ans:1,exp:"AVL is better for read-heavy systems (perfectly balanced). Red-Black is better for write-heavy systems (fewer rotations)."},
      {q:"What is the Time Complexity for searching an AVL Tree?",opts:["A. O(1)","B. O(log N) worst-case","C. O(N)","D. O(N^2)"],ans:1,exp:"Because it is guaranteed to be balanced, search will never degrade to O(N)."}
    ],
    flows:[
      {title:"Right Rotation (LL Heavy)",items:["start:Insert 1 into (3 -> 2)","proc:Tree is 3->2->1 (Line)","dec:Balance Factor of 3 is 2!","proc:Rotate Right around 2","end:2 becomes root, 1 is left, 3 is right"]}
    ],
    game:{icon:"⚖️",title:"The Balancer",desc:"Master self-balancing trees",badges:["⚖️ Rotator","📉 O(logN) Savior","📐 Factor Calculator"],challenges:[{icon:"📝",title:"Balance Factor",desc:"Calculate BF of a node",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Balance Factor Logic",badge:"Math Whiz",desc:"Write a function to calculate a node's balance factor.",tags:["Algorithms","Trees"],steps:[{title:"Height Func",desc:"Create a helper to get node height"},{"title:"Factor Func",desc:"Return height(left) - height(right)"}],code:`function getHeight(node) {\n  if (!node) return 0;\n  return Math.max(getHeight(node.left), getHeight(node.right)) + 1;\n}\n\nfunction getBalanceFactor(node) {\n  if (!node) return 0;\n  return getHeight(node.left) - getHeight(node.right);\n}`}
  },
  t42: {
    tag:'Phase 1 · Data Structures', num:42,
    title:'Trie',
    desc:'A Prefix Tree used for ultra-fast string and autocomplete searching.',
    theory:`<div class="card"><h3>⌨️ The Autocomplete Engine</h3><p>A <strong>Trie</strong> (pronounced "try", from re<em>trie</em>val) is a specialized tree designed specifically for storing and searching Strings. Instead of storing a whole word in a single node, <strong>each node stores a single character</strong>.</p><h4>How it works</h4><p>If you store "CAT" and "CAR", they share the 'C' node and the 'A' node, then branch off at 'T' and 'R'. This makes searching for words or prefixes incredibly fast: <code>O(L)</code> where L is the length of the word!</p><div class="cb"><span class="cm">// Time Complexity vs HashMap</span>
<span class="cm">// HashMap string lookup: O(1) to find exact word. (Cannot do prefix search)</span>
<span class="cm">// Trie string lookup: O(L) to find exact word AND can instantly find all words starting with "CA".</span></div></div>`,
    mcqs:[
      {q:"What is the primary use case for a Trie?",opts:["A. Sorting numbers","B. Autocomplete, spell checkers, and IP routing (prefix matching)","C. Managing queues","D. Image processing"],ans:1,exp:"Tries excel at finding all strings that share a common prefix (e.g. typing 'ca' into Google)."},
      {q:"In a Trie, what does each Node typically store?",opts:["A. A full sentence","B. A single character (or a hashmap of characters pointing to children) and a boolean 'isEndOfWord' flag","C. An integer","D. A linked list"],ans:1,exp:"The path from the root down to an 'isEndOfWord' node spells out the string."},
      {q:"What is the Time Complexity of searching for a word of length L in a Trie?",opts:["A. O(1)","B. O(L)","C. O(N) where N is all words in the dictionary","D. O(log N)"],ans:1,exp:"You just follow the L characters down the tree. It doesn't matter if the Trie contains 10 words or 10 million words; it always takes O(L) time!"},
      {q:"If 'CAR' and 'CAT' are in a Trie, how many nodes are created in total for them?",opts:["A. 6","B. 4 (Root -> C -> A -> branch to R and T)","C. 2","D. 1"],ans:1,exp:"They share the 'C' and 'A' nodes, saving memory compared to storing them separately."},
      {q:"Why might you NOT use a Trie?",opts:["A. They are too slow","B. They can be very memory intensive (high Space Complexity) because each node requires pointers to all possible children (e.g. 26 letters of alphabet)","C. They only work in Java","D. They can't store strings"],ans:1,exp:"Tries trade massive amounts of memory for incredible prefix-search speed."}
    ],
    flows:[
      {title:"Trie Prefix Search ('CA')",items:["start:Start at Root","proc:Find child 'C'","proc:Find child 'A'","dec:Return all children of 'A'?","end:Returns 'CAR' and 'CAT'"]}
    ],
    game:{icon:"⌨️",title:"Auto-Completer",desc:"Master prefix trees",badges:["⌨️ Typist","🌲 Prefix Ranger","🔤 Speller"],challenges:[{icon:"📝",title:"Memory Calc",desc:"Explain why Tries use so much RAM",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Basic Trie Node",badge:"Linguist",desc:"Set up the structure for a Trie Node.",tags:["Data Structures","Trie"],steps:[{title:"Class Node",desc:"Create TrieNode class"},{"title:"Children",desc:"Add this.children = {} (a hashmap)"},{"title:"End Flag",desc:"Add this.isEndOfWord = false"}],code:`class TrieNode {\n  constructor() {\n    this.children = {}; // Map char to TrieNode\n    this.isEndOfWord = false;\n  }\n}\n\nlet root = new TrieNode();\nroot.children['a'] = new TrieNode();\nroot.children['a'].isEndOfWord = true; // Represents "a"`}
  },
  t43: {
    tag:'Phase 1 · Data Structures', num:43,
    title:'Graph',
    desc:'A network of interconnected nodes, perfect for representing real-world relationships.',
    theory:`<div class="card"><h3>🕸️ The Web of Data</h3><p>A <strong>Graph</strong> is a collection of Nodes (called <strong>Vertices</strong>) connected by lines (called <strong>Edges</strong>). Unlike Trees, Graphs have no strict hierarchy or "root" node. They can contain loops and cycles.</p><h4>Types of Graphs</h4><ul><li><strong>Directed vs Undirected:</strong> Directed edges are one-way streets (Twitter follower). Undirected edges are two-way (Facebook friend).</li><li><strong>Weighted vs Unweighted:</strong> Weighted edges have a cost/distance associated with them (Google Maps travel time between cities).</li></ul><div class="box b-vi"><h5>How to represent them in code?</h5><p><strong>Adjacency List:</strong> A HashMap where the key is the Node, and the value is an Array of its neighbors. (Best for sparse graphs like social networks).</p><p><strong>Adjacency Matrix:</strong> A 2D Array where grid[i][j] = 1 if they are connected. (Best for dense graphs).</p></div></div>`,
    mcqs:[
      {q:"What is the difference between a Tree and a Graph?",opts:["A. Trees have leaves, Graphs don't","B. A Tree is actually just a highly restricted type of Graph (Directed, Acyclic, with a single Root)","C. Graphs are linear, Trees are not","D. They are completely unrelated"],ans:1,exp:"All trees are graphs, but not all graphs are trees (because graphs can have cycles/loops)."},
      {q:"Which Graph representation uses a 2D Array and is O(V^2) for space complexity?",opts:["A. Adjacency List","B. Adjacency Matrix","C. Edge List","D. Node Map"],ans:1,exp:"Adjacency Matrices are terrible for memory if the graph is huge and sparse (mostly 0s), but they allow O(1) edge lookups."},
      {q:"What is a Weighted Graph?",opts:["A. A graph that takes up lots of memory","B. A graph where the edges (connections) have an associated cost, distance, or weight (e.g. 5 miles)","C. A graph with thick lines","D. A graph with no cycles"],ans:1,exp:"Algorithms like Dijkstra's Shortest Path require weighted graphs to calculate the 'cheapest' route."},
      {q:"Which graph traversal algorithm uses a Queue to explore neighbors level-by-level?",opts:["A. DFS (Depth First Search)","B. BFS (Breadth First Search)","C. Binary Search","D. Quick Sort"],ans:1,exp:"BFS explores wide before deep, making it perfect for finding the shortest path in an unweighted graph."},
      {q:"What represents a 'Directed' edge?",opts:["A. A line without arrows","B. An arrow pointing from one node to another, indicating a one-way relationship","C. A dotted line","D. A heavy line"],ans:1,exp:"If A points to B, you can travel A->B, but not B->A."}
    ],
    flows:[
      {title:"Adjacency List Setup",items:["start:Node A connects to B and C","proc:Map['A'] = ['B', 'C']","proc:Node B connects to A","proc:Map['B'] = ['A']","end:Graph Represented!"]}
    ],
    game:{icon:"🕸️",title:"Networker",desc:"Master interconnected data",badges:["🕸️ Web Weaver","🗺️ Mapper","🛣️ Router"],challenges:[{icon:"📝",title:"List vs Matrix",desc:"Explain when to use an Adjacency List",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Social Network Graph",badge:"Zuck",desc:"Build an Adjacency List to represent friendships.",tags:["Data Structures","Graphs"],steps:[{title:"Init Map",desc:"Create class with this.adjList = {}"},{"title:"Add Node",desc:"Method to add a user to the map"},{"title:"Add Edge",desc:"Method to push friend into user's array"}],code:`class Graph {\n  constructor() { this.adjList = {}; }\n  addVertex(v) {\n    if (!this.adjList[v]) this.adjList[v] = [];\n  }\n  addEdge(v1, v2) {\n    this.adjList[v1].push(v2);\n    this.adjList[v2].push(v1); // Undirected\n  }\n}\n\nlet g = new Graph();\ng.addVertex("Bhoomi"); g.addVertex("Alice");\ng.addEdge("Bhoomi", "Alice");`}
  },
  t44: {
    tag:'Phase 1 · Data Structures', num:44,
    title:'Union Find',
    desc:'Also known as Disjoint Set, optimized for grouping elements and finding cycles.',
    theory:`<div class="card"><h3>🔗 The Cycle Detector</h3><p><strong>Union Find (Disjoint Set)</strong> is a highly specialized data structure used primarily to track a set of elements partitioned into a number of disjoint (non-overlapping) subsets.</p><h4>Primary Uses</h4><ul><li><strong>Finding Cycles:</strong> Quickly detecting if adding an edge to a graph will create a loop.</li><li><strong>Kruskal's Algorithm:</strong> Used to find the Minimum Spanning Tree of a graph.</li><li><strong>Network Connectivity:</strong> Answering "Is computer A connected to computer B, even through intermediaries?" in near O(1) time.</li></ul><h4>Two Main Operations</h4><p>1. <strong>Find:</strong> Determine which subset a particular element is in (usually by finding the "Root/Parent" of that subset).<br>2. <strong>Union:</strong> Join two subsets into a single subset.</p></div>`,
    mcqs:[
      {q:"What are the two primary operations of the Union Find data structure?",opts:["A. Push and Pop","B. Find and Union","C. Insert and Delete","D. Shift and Unshift"],ans:1,exp:"Find identifies the group; Union merges two groups together."},
      {q:"What is 'Path Compression' in Union Find?",opts:["A. Compressing the source code","B. An optimization that flattens the tree structure during a 'Find' operation, pointing all nodes directly to the root, making future lookups nearly O(1)","C. Deleting old nodes","D. Using a zip file"],ans:1,exp:"Path compression is the secret sauce that makes Union Find incredibly fast (Inverse Ackermann function time)."},
      {q:"What is Union Find exceptionally good at detecting in an undirected graph?",opts:["A. The shortest path","B. Cycles (Loops)","C. The maximum value","D. Sorted order"],ans:1,exp:"If you try to Union two nodes that already have the same Root/Parent, you know adding that edge creates a cycle!"},
      {q:"How is Union Find usually represented in code?",opts:["A. With a complex node class","B. Simply with an Array where array[i] stores the parent of element i","C. With a HashMap","D. With a Stack"],ans:1,exp:"An array called 'parent[]' is incredibly memory efficient and fast."},
      {q:"What is 'Union by Rank'?",opts:["A. Sorting the array","B. An optimization where you attach the smaller tree to the root of the larger tree during a Union, keeping the overall tree shallow","C. Promoting a user to Admin","D. Using military ranks"],ans:1,exp:"Combined with Path Compression, Union by Rank ensures operations run in near constant time."}
    ],
    flows:[
      {title:"Detecting a Cycle",items:["start:Add Edge (A-B)","proc:Find(A) -> Root 1. Find(B) -> Root 2","proc:Roots differ. Union them!","proc:Add Edge (B-C)","dec:Find(B) -> Root 1. Find(C) -> Root 1","end:Roots MATCH! Cycle detected!"]}
    ],
    game:{icon:"🔗",title:"The Connector",desc:"Master disjoint sets",badges:["🔗 Unionizer","🔍 Finder","🗜️ Compressor"],challenges:[{icon:"📝",title:"Path Compression",desc:"Explain path compression",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Basic Find Logic",badge:"Detective",desc:"Implement the recursive Find function with path compression.",tags:["Algorithms","Disjoint Set"],steps:[{title:"Parent Array",desc:"Assume parent = [0, 1, 1, 3]"},{"title:"Recursive Find",desc:"If parent[i] !== i, recursively call find"},{"title:"Compress",desc:"Assign the result to parent[i] before returning"}],code:`// Assuming 'parent' array is accessible\nfunction find(i) {\n  if (parent[i] === i) {\n    return i; // Root found\n  }\n  // Path Compression: Make it point directly to root\n  parent[i] = find(parent[i]); \n  return parent[i];\n}`}
  },
"""

start_marker = "};\n\nlet userXP"
inject_idx = content.find(start_marker)

if inject_idx != -1:
    new_content = content[:inject_idx] + ",\n" + rich_content + content[inject_idx:]
    with open(html_path, "w") as f:
        f.write(new_content)
    print("Successfully generated T41-T44 rich content!")
else:
    print("Could not find injection point.")
