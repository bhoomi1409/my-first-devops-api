import re

html_path = "/Users/bhoomim/devops CI:CD/handbook/fullstack_ai_handbook.html"
with open(html_path, "r") as f:
    content = f.read()

rich_content = r"""
  t54: {
    tag:'Phase 1 · Algorithms', num:54,
    title:'Backtracking',
    desc:'An algorithmic technique for finding all (or some) solutions to some computational problems by incrementally building candidates to the solutions, and abandoning a candidate as soon as it determines that the candidate cannot possibly be completed to a valid solution.',
    theory:`<div class="card"><h3>🔙 The Undo Button</h3><p><strong>Backtracking</strong> is an advanced form of DFS (Depth-First Search) used to solve constraint-satisfaction problems like Sudoku, N-Queens, or finding all permutations of a string.</p><h4>How it works</h4><p>You make a choice, dive deeper (recurse) to see if that choice leads to a solution. If it doesn't, you <strong>undo the choice</strong> (backtrack) and try the next option. It's essentially a highly optimized brute-force search that abandons invalid paths early (pruning).</p></div>`,
    mcqs:[
      {q:"What is the core mechanic of Backtracking?",opts:["A. Sorting an array","B. Recursively trying a path, and if it fails, undoing the last choice (popping state) and trying a different path","C. Always picking the locally optimal choice","D. Using a HashMap"],ans:1,exp:"You 'backtrack' your steps when you hit a dead end."},
      {q:"Which of these problems is a classic candidate for Backtracking?",opts:["A. Finding the max number in an array","B. Solving a Sudoku puzzle","C. Sorting a database","D. Binary Search"],ans:1,exp:"In Sudoku, you place a number. If it leads to an invalid board later, you erase it and try a different number."},
      {q:"What is 'Pruning' in the context of Backtracking?",opts:["A. Deleting the source code","B. Identifying that a current partial solution is invalid and abandoning it immediately, saving massive amounts of computation time","C. Sorting the variables","D. A type of Tree"],ans:1,exp:"Without pruning, backtracking is just O(N!) pure brute force. Pruning makes it viable."},
      {q:"What underlying mechanism allows Backtracking to 'remember' its previous state to undo choices?",opts:["A. The Hard Drive","B. The Call Stack (via Recursion)","C. A Queue","D. A Trie"],ans:1,exp:"When a recursive function returns (pops), the local variables from the previous state are restored automatically."},
      {q:"Backtracking is often used to find all ______ of a string or array.",opts:["A. Lengths","B. Permutations / Combinations","C. Hashes","D. Types"],ans:1,exp:"To find all combinations, you must methodically build them up, backtracking to swap elements."}
    ],
    flows:[
      {title:"Sudoku Backtracking",items:["start:Place '1' in Cell","proc:Recurse to next Cell","dec:Valid placement?","proc:(No) Backtrack: Erase '1'","proc:Place '2' in Cell","end:Recurse again"]}
    ],
    game:{icon:"🔙",title:"The Undoer",desc:"Master recursive brute force",badges:["🔙 Backtracker","✂️ Pruner","🎲 Permutator"],challenges:[{icon:"📝",title:"Identify Pruning",desc:"Explain why pruning is necessary",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Permutations",badge:"Combiner",desc:"Find all permutations of an array [1,2].",tags:["Algorithms","Backtracking"],steps:[{title:"Base Case",desc:"If path length === array length, save path"},{"title:"Loop",desc:"Iterate through choices"},{"title:"Choose/Explore/Undo",desc:"Add to path, recurse, remove from path (undo)"}],code:`function permute(nums) {\n  let result = [];\n  function backtrack(path, used) {\n    if (path.length === nums.length) { result.push([...path]); return; }\n    for (let i = 0; i < nums.length; i++) {\n      if (used[i]) continue;\n      path.push(nums[i]); used[i] = true; // Choose\n      backtrack(path, used);              // Explore\n      path.pop(); used[i] = false;        // Undo\n    }\n  }\n  backtrack([], {});\n  return result;\n}`}
  },
  t55: {
    tag:'Phase 1 · Algorithms', num:55,
    title:'Divide and Conquer',
    desc:'An algorithm design paradigm that recursively breaks down a problem into two or more sub-problems of the same type.',
    theory:`<div class="card"><h3>🪓 Break It Down</h3><p><strong>Divide and Conquer</strong> works by breaking a massive, impossible problem into small, manageable chunks, solving those chunks, and then stitching the answers back together.</p><h4>The Three Steps</h4><ol><li><strong>Divide:</strong> Break the problem into smaller subproblems.</li><li><strong>Conquer:</strong> Solve the subproblems recursively (Base case: when the problem is small enough to solve directly).</li><li><strong>Combine:</strong> Merge the solutions of the subproblems into the final solution.</li></ol><div class="box b-vi"><h5>Classic Example: Merge Sort</h5><p>Sorting 1,000,000 items is hard. Sorting 1 item is easy (it's already sorted!). Merge Sort divides the million items in half repeatedly until it has 1,000,000 single items. Then it merges them back together in order.</p></div></div>`,
    mcqs:[
      {q:"What are the three core steps of Divide and Conquer?",opts:["A. Stop, Drop, and Roll","B. Divide, Conquer, Combine","C. Push, Pop, Peek","D. Sort, Search, Hash"],ans:1,exp:"You divide the data, solve the tiny pieces, and combine the results."},
      {q:"Which famous sorting algorithms utilize Divide and Conquer?",opts:["A. Bubble Sort and Insertion Sort","B. Merge Sort and Quick Sort","C. Selection Sort","D. Bogo Sort"],ans:1,exp:"Merge sort divides by half. Quick sort divides by a pivot."},
      {q:"How is Divide and Conquer different from Dynamic Programming?",opts:["A. They are identical","B. DP specifically handles 'Overlapping Subproblems' by caching them. D&C subproblems are usually disjoint (independent), so they don't need caching.","C. D&C uses less memory","D. DP uses loops, D&C uses arrays"],ans:1,exp:"In Merge Sort, sorting the left half has zero overlap with sorting the right half, so caching (DP) doesn't help."},
      {q:"What programming feature is heavily relied upon to implement the 'Conquer' step?",opts:["A. Callbacks","B. Recursion","C. Promises","D. Global Variables"],ans:1,exp:"The algorithm recursively calls itself on the smaller halves until it hits the base case."},
      {q:"Binary Search is often considered a simple form of Divide and Conquer. Why?",opts:["A. Because it divides the search space in half at each step","B. Because it uses two arrays","C. Because it sorts the array","D. Because it combines data"],ans:0,exp:"It 'divides' the array by half, though it technically only 'conquers' one side (Decrease and Conquer)."}
    ],
    flows:[
      {title:"D&C Flow",items:["start:Problem of size N","proc:Divide to N/2 and N/2","proc:Conquer (Solve) both halves recursively","end:Combine the two solutions"]}
    ],
    game:{icon:"🪓",title:"The Divider",desc:"Master recursive splitting",badges:["🪓 Splitter","⚔️ Conqueror","🤝 Combiner"],challenges:[{icon:"📝",title:"DP vs D&C",desc:"Explain the difference",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Merge Sort Combiner",badge:"Stitcher",desc:"Write the 'Combine' step of Merge Sort.",tags:["Algorithms","D&C"],steps:[{title:"Two Arrays",desc:"Accept two SORTED arrays"},{"title:"Two Pointers",desc:"Use i and j to track positions in both arrays"},{"title:"Merge",desc:"Compare arr1[i] and arr2[j], push smaller to result"}],code:`function merge(left, right) {\n  let res = [], i = 0, j = 0;\n  while (i < left.length && j < right.length) {\n    if (left[i] < right[j]) res.push(left[i++]);\n    else res.push(right[j++]);\n  }\n  // Push remaining elements\n  return [...res, ...left.slice(i), ...right.slice(j)];\n}`}
  },
  t56: {
    tag:'Phase 1 · Algorithms', num:56,
    title:'Graph Algorithms',
    desc:'Algorithms specifically designed to solve problems related to graph theory (networks, paths, connections).',
    theory:`<div class="card"><h3>🗺️ Navigating the Network</h3><p>Because Graphs represent complex relationships (like maps, social networks, or computer networks), they require specialized algorithms to answer questions like: "Are these two nodes connected?" or "What is the fastest way from A to B?"</p><h4>Core Graph Algos</h4><ul><li><strong>Traversal (DFS/BFS):</strong> Visiting every node in the network.</li><li><strong>Shortest Path:</strong> Dijkstra's, Bellman-Ford, Floyd-Warshall.</li><li><strong>Minimum Spanning Tree:</strong> Kruskal's, Prim's (Finding the cheapest way to connect ALL nodes without cycles, e.g., laying fiber optic cable).</li><li><strong>Topological Sort:</strong> Ordering nodes based on dependencies (e.g., Course prerequisites).</li></ul></div>`,
    mcqs:[
      {q:"What is a Minimum Spanning Tree (MST)?",opts:["A. A tree with the fewest number of leaves","B. A subset of graph edges that connects all vertices together, without any cycles, and with the minimum possible total edge weight","C. A tree used for sorting","D. A binary search tree"],ans:1,exp:"MSTs are used for network design (like laying electrical grids cheaply)."},
      {q:"Which algorithm is used to find the Minimum Spanning Tree?",opts:["A. Quick Sort","B. Kruskal's or Prim's Algorithm","C. Dijkstra's","D. Binary Search"],ans:1,exp:"Kruskal's uses a Greedy approach and Union-Find to avoid creating cycles while picking the cheapest edges."},
      {q:"What does it mean if a Graph is 'Bipartite'?",opts:["A. It has two parts that are identical","B. Its vertices can be divided into two disjoint sets such that every edge connects a vertex in one set to a vertex in the other","C. It has two roots","D. It is sorted twice"],ans:1,exp:"Useful for matching problems (e.g., matching job seekers to job openings)."},
      {q:"How do you detect a Cycle in a Directed Graph?",opts:["A. Use a HashMap","B. Use DFS and keep track of the current 'recursion stack' to see if you revisit a node currently being explored","C. Sort the graph","D. Use Binary Search"],ans:1,exp:"If you hit a node that is currently 'in progress' on the call stack, you have looped back on yourself!"},
      {q:"What is the primary difference between a Graph and a Tree?",opts:["A. Trees are green","B. Trees are strictly hierarchical and cannot contain cycles. Graphs can have arbitrary connections and cycles.","C. Graphs don't use nodes","D. Trees are for Java only"],ans:1,exp:"A Tree is just a Directed Acyclic Graph (DAG) with one root."}
    ],
    flows:[
      {title:"Graph Algorithm Selection",items:["start:Problem Type?","dec:Shortest Path?","proc:-> Dijkstra (if positive weights)","dec:Connect Everything Cheaply?","proc:-> Kruskal's (MST)","dec:Dependency Ordering?","end:-> Topological Sort"]}
    ],
    game:{icon:"🗺️",title:"The Navigator",desc:"Master graph theory",badges:["🗺️ Cartographer","🌳 MST Builder","🔄 Cycle Breaker"],challenges:[{icon:"📝",title:"Graph vs Tree",desc:"Define the difference",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Cycle Detection (Conceptual)",badge:"Detector",desc:"Understand how DFS detects cycles.",tags:["Algorithms","Graphs"],steps:[{title:"State Tracking",desc:"Nodes need 3 states: Unvisited, Visiting, Visited"},{"title:"DFS Visit",desc:"Mark node as 'Visiting'"},{"title:"Check Neighbors",desc:"If neighbor is 'Visiting', cycle found! Else, mark 'Visited' when done"}],code:`// Conceptual DFS Cycle Check\nlet state = {}; // 0=Unvisited, 1=Visiting, 2=Visited\n\nfunction hasCycle(node, graph) {\n  if (state[node] === 1) return true; // Cycle!\n  if (state[node] === 2) return false;\n  \n  state[node] = 1; // Mark Visiting\n  for (let neighbor of graph[node]) {\n    if (hasCycle(neighbor, graph)) return true;\n  }\n  state[node] = 2; // Mark Visited\n  return false;\n}`}
  },
  t57: {
    tag:'Phase 1 · Algorithms', num:57,
    title:'Dijkstra',
    desc:'The famous algorithm for finding the shortest paths between nodes in a graph.',
    theory:`<div class="card"><h3>🚗 GPS Routing Engine</h3><p><strong>Dijkstra's Algorithm</strong> (pronounced DIKE-stra) finds the absolute shortest path from a starting node to all other nodes in a <em>Weighted Graph</em> (where edges have distance/cost).</p><h4>How it works (The Greedy Approach)</h4><ol><li>Keep a table of the shortest known distance to every node (initially Infinity).</li><li>Start at node A (distance 0).</li><li>Look at A's neighbors. Update their distances in the table if the new path is shorter.</li><li>Pick the unvisited node with the <strong>smallest known distance</strong> and repeat.</li></ol><div class="box b-ro"><h5>⚠️ The Weakness</h5><p>Dijkstra completely fails if the graph has <strong>Negative Weights</strong> (e.g. an edge that gives you -5 cost). It assumes that adding an edge will always increase the total cost. If you have negative weights, you must use the <em>Bellman-Ford</em> algorithm.</p></div></div>`,
    mcqs:[
      {q:"What is the primary purpose of Dijkstra's Algorithm?",opts:["A. Sorting an array","B. Finding the shortest path from a starting node to all other nodes in a graph with non-negative edge weights","C. Finding a cycle","D. Traversing a Binary Tree"],ans:1,exp:"It is the foundation of routing protocols and GPS software."},
      {q:"What Data Structure is crucial for optimizing Dijkstra's Algorithm from O(V^2) to O(E log V)?",opts:["A. A Priority Queue (Min-Heap)","B. A Stack","C. A standard Array","D. A Trie"],ans:0,exp:"The algorithm constantly needs to find the 'unvisited node with the smallest distance'. A Min-Heap provides this instantly."},
      {q:"What happens if a graph contains negative edge weights?",opts:["A. Dijkstra's runs faster","B. Dijkstra's Algorithm may yield incorrect results or get stuck in an infinite loop","C. The OS crashes","D. It ignores them"],ans:1,exp:"Dijkstra acts greedily, assuming once a node is 'processed', its shortest path is permanently locked in. Negative weights violate this assumption."},
      {q:"In Dijkstra's, what is the initial 'shortest known distance' for all nodes (except the starting node)?",opts:["A. 0","B. Infinity","C. -1","D. 100"],ans:1,exp:"You assume the worst (Infinity) until you discover a valid path that updates it to a smaller number."},
      {q:"Is Dijkstra's a Greedy Algorithm or Dynamic Programming?",opts:["A. Dynamic Programming","B. Greedy Algorithm","C. Divide and Conquer","D. Backtracking"],ans:1,exp:"It makes the locally optimal choice at each step (picking the closest unvisited node)."}
    ],
    flows:[
      {title:"Dijkstra Flow",items:["start:Init all dists to Infinity. Start=0","proc:Pop node with Min Dist from PQ","proc:Check neighbors","dec:New path < known path?","proc:(Yes) Update dist, Push to PQ","end:Repeat until PQ empty"]}
    ],
    game:{icon:"🚗",title:"The GPS",desc:"Master shortest paths",badges:["🚗 Router","📉 Min-Heap Master","⚠️ Positive Weight Purist"],challenges:[{icon:"📝",title:"Negative Trap",desc:"Explain why negative weights break it",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Distance Table",badge:"Tracker",desc:"Setup the tracking table for Dijkstra.",tags:["Algorithms","Graphs"],steps:[{title:"Init Map",desc:"Create distances = {}"},{"title:"Loop Nodes",desc:"Set all distances to Infinity"},{"title:"Start Node",desc:"Set distances[startNode] = 0"}],code:`function initDijkstra(nodes, startNode) {\n  let distances = {};\n  for (let node of nodes) {\n    distances[node] = Infinity;\n  }\n  distances[startNode] = 0;\n  return distances;\n}\n\nconsole.log(initDijkstra(['A', 'B', 'C'], 'A')); \n// {A: 0, B: Infinity, C: Infinity}`}
  },
  t58: {
    tag:'Phase 1 · Algorithms', num:58,
    title:'Floyd Warshall',
    desc:'An algorithm for finding shortest paths in a directed weighted graph with positive or negative edge weights.',
    theory:`<div class="card"><h3>🌐 All-Pairs Shortest Path</h3><p>While Dijkstra finds the shortest path from <em>one</em> starting node to all others, <strong>Floyd-Warshall</strong> finds the shortest path from <strong>EVERY node to EVERY OTHER node</strong> at the same time!</p><h4>How it works (Dynamic Programming)</h4><p>It uses a 2D Array (Matrix) and relies on three nested loops <code>O(V^3)</code>. For every pair of nodes (i, j), it asks: <em>"Is the path from i to j shorter if I go through a middle node k?"</em></p><div class="box b-em"><h5>Handling Negatives</h5><p>Unlike Dijkstra, Floyd-Warshall handles negative edge weights perfectly. It can even detect <strong>Negative Cycles</strong> (a loop that gives you infinite negative cost) by checking if the diagonal of the matrix (distance from a node to itself) ever drops below 0!</p></div></div>`,
    mcqs:[
      {q:"What is the primary use case of the Floyd-Warshall algorithm?",opts:["A. Single-source shortest path","B. All-pairs shortest path (finding shortest paths between ALL pairs of vertices)","C. Sorting an array","D. Reversing a Linked List"],ans:1,exp:"It computes a complete distance matrix for the entire graph."},
      {q:"What is the Time Complexity of Floyd-Warshall?",opts:["A. O(N)","B. O(V^2)","C. O(V^3) (where V is number of vertices)","D. O(log N)"],ans:2,exp:"It uses three nested loops (i, j, k), making it very slow for massive graphs, but perfect for dense, small graphs."},
      {q:"Can Floyd-Warshall handle negative edge weights?",opts:["A. No","B. Yes, unlike Dijkstra's, it correctly computes shortest paths even with negative weights","C. Only in Java","D. Only if the weights are integers"],ans:1,exp:"This is one of its major advantages over Dijkstra's."},
      {q:"How does Floyd-Warshall detect a 'Negative Cycle'?",opts:["A. It crashes","B. If the distance from any node to ITSELF becomes less than zero, a negative cycle exists","C. It uses a HashMap","D. It returns null"],ans:1,exp:"Normally, distance to self is 0. If it drops to -1, it means there's a loop that continuously reduces the cost."},
      {q:"Floyd-Warshall is an example of which algorithmic paradigm?",opts:["A. Greedy Algorithm","B. Dynamic Programming","C. Divide and Conquer","D. Backtracking"],ans:1,exp:"It iteratively builds up the shortest paths by caching the best known distances in a matrix."}
    ],
    flows:[
      {title:"Floyd-Warshall Logic",items:["start:For every middle node K","proc:For every start node I","proc:For every end node J","dec:dist[I][K] + dist[K][J] < dist[I][J]?","end:(Yes) Update dist[I][J]"]}
    ],
    game:{icon:"🌐",title:"The Matrix",desc:"Master all-pairs routing",badges:["🌐 All-Pair Pro","🧊 O(V^3) Tank","🛑 Negative Cycle Detector"],challenges:[{icon:"📝",title:"Time Complexity",desc:"Explain why it is O(V^3)",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"The Core Loop",badge:"Loop Master",desc:"Write the 3 nested loops of Floyd-Warshall.",tags:["Algorithms","DP"],steps:[{title:"Loop K",desc:"Iterate middle nodes"},{"title:"Loop I & J",desc:"Iterate start and end nodes"},{"title:"Update",desc:"Math.min(current, path via K)"}],code:`function floydWarshall(dist, V) {\n  for (let k = 0; k < V; k++) {\n    for (let i = 0; i < V; i++) {\n      for (let j = 0; j < V; j++) {\n        if (dist[i][k] + dist[k][j] < dist[i][j]) {\n          dist[i][j] = dist[i][k] + dist[k][j];\n        }\n      }\n    }\n  }\n  return dist;\n}`}
  },
  t59: {
    tag:'Phase 1 · Algorithms', num:59,
    title:'Topological Sort',
    desc:'A linear ordering of vertices such that for every directed edge U->V, vertex U comes before V in the ordering.',
    theory:`<div class="card"><h3>📋 Resolving Dependencies</h3><p><strong>Topological Sort</strong> is used specifically on Directed Acyclic Graphs (DAGs). It orders nodes so that all "dependencies" are listed before the things that depend on them.</p><h4>Real World Example</h4><p>College courses! You can't take <em>Advanced Robotics</em> until you take <em>Calculus</em> and <em>Physics</em>. If you model this as a graph, Topological Sort gives you the exact order you should take your classes in.</p><div class="box b-am"><h5>⚠️ The Cycle Problem</h5><p>Topological Sort is IMPOSSIBLE if the graph has a cycle (A requires B, B requires C, C requires A). You are deadlocked. Therefore, it only works on DAGs.</p></div></div>`,
    mcqs:[
      {q:"What type of graph is required to perform a Topological Sort?",opts:["A. Undirected Graph","B. Directed Acyclic Graph (DAG)","C. Binary Tree","D. Cyclic Graph"],ans:1,exp:"It must be Directed (so dependencies have a direction) and Acyclic (no impossible circular loops)."},
      {q:"What is the most common real-world application of Topological Sort?",opts:["A. Sorting numbers alphabetically","B. Task scheduling and resolving dependencies (e.g., NPM package installs, build systems like Make/Webpack)","C. Finding shortest paths","D. Image processing"],ans:1,exp:"Webpack uses topological sort to figure out which JS files to bundle first based on your 'import' statements."},
      {q:"How is Topological Sort usually implemented?",opts:["A. Using a modified DFS or Kahn's Algorithm (BFS based)","B. Using Bubble Sort","C. Using Quick Sort","D. Using Dijkstra's"],ans:0,exp:"In DFS, you recursively visit children, and when a node has no unvisited children left, you push it to a Stack. Reversing the Stack gives the sort."},
      {q:"What happens if you try to perform a Topological Sort on a graph that contains a cycle?",opts:["A. It succeeds","B. It fails, because a valid linear dependency order is impossible (Deadlock)","C. It reverses the graph","D. It skips the cycle"],ans:1,exp:"If Job A requires Job B, and Job B requires Job A, neither can ever start."},
      {q:"Is there only one valid Topological Sort for a given graph?",opts:["A. Yes, always","B. No, there can be many valid topological orderings if some nodes don't depend on each other","C. Only in Java","D. Yes, if the graph is weighted"],ans:1,exp:"If Math and English have no prerequisites, you can take either one first. Both orderings are valid."}
    ],
    flows:[
      {title:"Dependency Flow",items:["start:Graph: A->C, B->C","dec:Who has 0 dependencies?","proc:A and B (Can do either)","proc:Finish A, Finish B","end:Dependencies met. Finish C."]}
    ],
    game:{icon:"📋",title:"The Scheduler",desc:"Master dependency resolution",badges:["📋 Scheduler","🎓 Prerequisite Pro","🛑 Deadlock Detector"],challenges:[{icon:"📝",title:"Identify DAG",desc:"Explain what a DAG is",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"In-Degree Counter",badge:"Kahn",desc:"Step 1 of Kahn's Algorithm: Count dependencies.",tags:["Algorithms","Graphs"],steps:[{title:"Init Array",desc:"Create inDegree array filled with 0s"},{"title:"Count",desc:"For every edge u -> v, increment inDegree[v]"},{"title:"Result",desc:"Nodes with 0 in-degree are safe to start!"}],code:`function countDependencies(numCourses, prerequisites) {\n  let inDegree = new Array(numCourses).fill(0);\n  for (let [course, prereq] of prerequisites) {\n    inDegree[course]++; // This course has a dependency\n  }\n  return inDegree; // Any 0 is ready to take!\n}`}
  },
"""

start_marker = "};\n\nlet userXP"
inject_idx = content.find(start_marker)

if inject_idx != -1:
    new_content = content[:inject_idx] + ",\n" + rich_content + content[inject_idx:]
    with open(html_path, "w") as f:
        f.write(new_content)
    print("Successfully generated T54-T59 rich content!")
else:
    print("Could not find injection point.")
