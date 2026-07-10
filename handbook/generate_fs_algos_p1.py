import re

html_path = "/Users/bhoomim/devops CI:CD/handbook/fullstack_ai_handbook.html"
with open(html_path, "r") as f:
    content = f.read()

rich_content = r"""
  t45: {
    tag:'Phase 1 · Algorithms', num:45,
    title:'Sorting',
    desc:'Arranging data in a specific order (ascending or descending).',
    theory:`<div class="card"><h3>🗂️ Organizing Chaos</h3><p>Sorting algorithms organize data to make it easier to search and process later.</p><h4>Common Sorting Algorithms</h4><ul><li><strong>Bubble / Selection / Insertion Sort:</strong> The "naive" algorithms. Very easy to write, but incredibly slow for large data. Time Complexity: <code>O(N^2)</code>.</li><li><strong>Merge Sort:</strong> A "Divide and Conquer" algorithm. Splits the array in half recursively until size 1, then merges them back together in order. Time Complexity: <code>O(N log N)</code>. Space: <code>O(N)</code>.</li><li><strong>Quick Sort:</strong> Picks a "pivot" element, puts smaller items to the left, larger to the right, and repeats recursively. Time Complexity: <code>O(N log N)</code> average, but <code>O(N^2)</code> worst-case. Extremely fast in practice.</li></ul><div class="box b-vi"><h5>💡 Language Defaults</h5><p>When you call <code>array.sort()</code> in JS or Python, it usually uses <strong>Timsort</strong> (a highly optimized hybrid of Merge Sort and Insertion Sort) which runs in <code>O(N log N)</code>.</p></div></div>`,
    mcqs:[
      {q:"Why do we sort data?",opts:["A. It looks prettier","B. It makes future search operations (like Binary Search) exponentially faster","C. It saves hard drive space","D. It compresses the data"],ans:1,exp:"Sorting is an upfront investment. You spend O(N log N) time sorting so that future searches take O(log N) instead of O(N)."},
      {q:"What is the Time Complexity of Bubble Sort?",opts:["A. O(1)","B. O(log N)","C. O(N)","D. O(N^2)"],ans:3,exp:"Bubble sort uses a nested loop to compare every element against every other element, resulting in quadratic time."},
      {q:"Which sorting algorithm guarantees an O(N log N) time complexity but requires O(N) extra space/memory?",opts:["A. Quick Sort","B. Merge Sort","C. Bubble Sort","D. Selection Sort"],ans:1,exp:"Merge sort needs extra arrays to hold the halves as it merges them back together."},
      {q:"What does it mean for a sorting algorithm to be 'Stable'?",opts:["A. It doesn't crash","B. If two elements have the same value, their relative order is preserved from the original array","C. It always runs in O(1)","D. It works on strings"],ans:1,exp:"Stability is important if you sort by Name, and then sort by Age, you want people with the same Age to remain sorted by Name."},
      {q:"Quick Sort is incredibly fast, but what is its worst-case time complexity?",opts:["A. O(log N)","B. O(N)","C. O(N log N)","D. O(N^2)"],ans:3,exp:"If the array is already sorted, and you always pick the first element as the pivot, Quick Sort degrades to O(N^2)."}
    ],
    flows:[
      {title:"Merge Sort Divide",items:["start:[38, 27, 43, 3]","proc:Split: [38, 27] and [43, 3]","proc:Split: [38] [27] [43] [3]","dec:Merge: [27, 38] and [3, 43]","end:Final Merge: [3, 27, 38, 43]"]}
    ],
    game:{icon:"🗂️",title:"The Sorter",desc:"Master sorting algorithms",badges:["🗂️ Organizer","⚡ Quick Sorter","📉 LogN Hero"],challenges:[{icon:"📝",title:"Identify Stable",desc:"Explain Stable Sorting",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"JS Sort Gotcha",badge:"Debugger",desc:"Understand JS default sorting behavior.",tags:["JavaScript","Sorting"],steps:[{title:"The Trap",desc:"Sort [1, 2, 10, 20] using .sort()"},{"title:"The Result",desc:"It results in [1, 10, 2, 20] because it sorts alphabetically!"},{"title:"The Fix",desc:"Pass a comparator: .sort((a,b) => a - b)"}],code:`let nums = [1, 20, 10, 2];\n\n// Bad (Alphabetical default)\nconsole.log(nums.sort()); \n// Output: [1, 10, 2, 20]\n\n// Good (Numerical comparison)\nconsole.log(nums.sort((a, b) => a - b));\n// Output: [1, 2, 10, 20]`}
  },
  t46: {
    tag:'Phase 1 · Algorithms', num:46,
    title:'Searching',
    desc:'Finding the location or existence of a specific target within data.',
    theory:`<div class="card"><h3>🔎 Finding the Needle</h3><p>Searching is the act of looking through data to find a specific target. The efficiency of a search depends heavily on the underlying Data Structure.</p><h4>Linear Search</h4><p>Starting at the beginning and looking at every single item until you find the target. Time Complexity: <code>O(N)</code>. (Used for unsorted arrays or Linked Lists).</p><h4>Optimized Searches</h4><p>If the data is <strong>sorted</strong>, you can use Binary Search <code>O(log N)</code>. If the data is stored in a <strong>HashMap/HashSet</strong>, you can search in <code>O(1)</code> time!</p></div>`,
    mcqs:[
      {q:"What is the Time Complexity of a Linear Search?",opts:["A. O(1)","B. O(log N)","C. O(N)","D. O(N^2)"],ans:2,exp:"You must check each item one by one, so time scales linearly with the size of the data."},
      {q:"If you have an Unsorted Array, what is the best way to search it?",opts:["A. Binary Search","B. Linear Search","C. Tree Search","D. Graph Search"],ans:1,exp:"You cannot use Binary Search on unsorted data. You must use Linear Search."},
      {q:"If you need to repeatedly search an array millions of times, what should you do first?",opts:["A. Put the array in a loop","B. Sort the array once (O(N log N)), so you can use Binary Search (O(log N)) for the millions of lookups","C. Buy more RAM","D. Delete the array"],ans:1,exp:"The upfront cost of sorting pays off massively if you do many searches later."},
      {q:"Which data structure gives you O(1) search time?",opts:["A. Linked List","B. HashMap/HashSet","C. Array","D. Binary Tree"],ans:1,exp:"Hash functions allow instant jump-to-index capabilities."},
      {q:"What does JavaScript's array.indexOf() use under the hood?",opts:["A. Binary Search","B. Linear Search","C. HashMap","D. Trie"],ans:1,exp:"indexOf() scans the array from index 0 to the end, making it O(N)."}
    ],
    flows:[
      {title:"Linear Search Flow",items:["start:Array: [4, 2, 9]. Target: 9","dec:Is arr[0]==9?","proc:(No) Move to next","dec:Is arr[1]==9?","proc:(No) Move to next","dec:Is arr[2]==9?","end:(Yes) Return index 2"]}
    ],
    game:{icon:"🔎",title:"The Detective",desc:"Master data retrieval",badges:["🔎 Linear Sleuth","⚡ Constant Finder","📉 Optimal Searcher"],challenges:[{icon:"📝",title:"indexOf Time",desc:"Explain indexOf complexity",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Linear Search Impl",badge:"Sleuth",desc:"Write a basic linear search from scratch.",tags:["Algorithms","Search"],steps:[{title:"Loop",desc:"Iterate i from 0 to length-1"},{"title:"Check",desc:"If arr[i] === target, return i"},{"title:"Not Found",desc:"Return -1 at the end"}],code:`function linearSearch(arr, target) {\n  for (let i = 0; i < arr.length; i++) {\n    if (arr[i] === target) return i;\n  }\n  return -1;\n}\nconsole.log(linearSearch([5,10,15], 10)); // 1`}
  },
  t47: {
    tag:'Phase 1 · Algorithms', num:47,
    title:'Binary Search',
    desc:'A highly efficient search algorithm that halves the search space at each step.',
    theory:`<div class="card"><h3>✂️ The Halving Technique</h3><p><strong>Binary Search</strong> is the reason we sort arrays. If an array is sorted, you don't need to check every item. You check the <strong>middle</strong> item. If the middle item is too big, you know your target MUST be in the left half. You instantly throw away 50% of the data.</p><h4>Time Complexity</h4><p>Because you cut the dataset in half every step, it runs in <code>O(log N)</code> time. This means you can find a specific item in a sorted list of <strong>1 billion</strong> items in just ~30 steps!</p><div class="cb"><span class="cm">// Binary Search Pointers</span>
<span class="ck">let</span> <span class="cv">left</span> = <span class="cs">0</span>;
<span class="ck">let</span> <span class="cv">right</span> = arr.length - <span class="cs">1</span>;
<span class="cm">// Loop while left <= right...</span></div></div>`,
    mcqs:[
      {q:"What is the MANDATORY prerequisite for using Binary Search on an array?",opts:["A. It must contain only numbers","B. It must be perfectly sorted","C. It must be less than 100 items","D. It must be a prime length"],ans:1,exp:"If the data isn't sorted, checking the middle tells you absolutely nothing about where the target is."},
      {q:"What is the Time Complexity of Binary Search?",opts:["A. O(1)","B. O(log N)","C. O(N)","D. O(N^2)"],ans:1,exp:"Logarithmic time. It scales incredibly well for massive datasets."},
      {q:"In Binary Search, if your target is LESS than the middle element, what do you do?",opts:["A. Move the 'left' pointer to middle + 1","B. Move the 'right' pointer to middle - 1","C. Return false","D. Throw an error"],ans:1,exp:"You discard the right half of the array by bringing the right boundary inwards."},
      {q:"Can you perform Binary Search on a standard Singly Linked List?",opts:["A. Yes, perfectly","B. No, because you cannot jump instantly to the 'middle' element in O(1) time","C. Only if it is sorted","D. Yes, but only in Java"],ans:1,exp:"Binary search requires O(1) random access to find the midpoint, which Linked Lists do not have."},
      {q:"How many steps does it take to binary search 1,000,000 items in the worst case?",opts:["A. 1,000,000","B. 500,000","C. ~20","D. 1"],ans:2,exp:"log2(1,000,000) is roughly 20. 2^20 = ~1,048,576."}
    ],
    flows:[
      {title:"Binary Search Flow (Find 2)",items:["start:Arr: [1, 2, 3, 4, 5]","proc:Mid is 3. Target(2) < 3.","proc:Discard Right Half","proc:Arr: [1, 2]. Mid is 1.","dec:Target(2) > 1. Discard Left.","end:Arr: [2]. Found!"]}
    ],
    game:{icon:"✂️",title:"The Halver",desc:"Master O(log N) searches",badges:["✂️ Halver","📉 LogN Master","🎯 Midpoint Sniper"],challenges:[{icon:"📝",title:"Calculate Max Steps",desc:"Max steps for 4 billion items? (32)",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Binary Search Impl",badge:"LogN Sniper",desc:"Write the classic Binary Search algorithm.",tags:["Algorithms","Search"],steps:[{title:"Pointers",desc:"left = 0, right = arr.length - 1"},{"title:"Loop",desc:"while (left <= right)"},{"title:"Midpoint",desc:"mid = Math.floor((left+right)/2)"},{"title:"Check",desc:"If target < arr[mid], right = mid-1. Else left = mid+1."}],code:`function binarySearch(arr, target) {\n  let l = 0, r = arr.length - 1;\n  while (l <= r) {\n    let mid = Math.floor((l + r) / 2);\n    if (arr[mid] === target) return mid;\n    if (target < arr[mid]) r = mid - 1;\n    else l = mid + 1;\n  }\n  return -1;\n}`}
  },
  t48: {
    tag:'Phase 1 · Algorithms', num:48,
    title:'DFS',
    desc:'Depth-First Search: Exploring a tree or graph by going as deep as possible before backtracking.',
    theory:`<div class="card"><h3>🕳️ Diving Deep</h3><p><strong>Depth-First Search (DFS)</strong> is an algorithm for traversing Trees or Graphs. It explores as far down a single branch as possible until it hits a dead end (leaf), and then <strong>backtracks</strong> up to explore the next branch.</p><h4>Implementation</h4><p>DFS is naturally implemented using <strong>Recursion</strong> (which uses the Call Stack under the hood), or iteratively using your own manual <strong>Stack</strong>.</p><div class="box b-ro"><h5>Use Cases</h5><p>Solving mazes, finding paths in puzzles, checking if a path exists between two nodes, and topological sorting.</p></div></div>`,
    mcqs:[
      {q:"Which data structure is fundamentally linked to Depth-First Search (DFS)?",opts:["A. Queue","B. Stack (or the Call Stack via Recursion)","C. HashMap","D. Array"],ans:1,exp:"DFS plunges deep, and when it hits a wall, it pops the last location off the stack to backtrack."},
      {q:"What is the primary difference between DFS and BFS?",opts:["A. DFS is for arrays, BFS is for trees","B. DFS dives deep into one branch before checking siblings; BFS checks all siblings before diving deeper","C. DFS is faster","D. BFS uses recursion"],ans:1,exp:"DFS goes deep. BFS goes wide."},
      {q:"When using DFS on a Graph (unlike a Tree), what MUST you keep track of?",opts:["A. The root node","B. A 'Visited' Set or Array to prevent getting stuck in infinite loops/cycles","C. The time it takes","D. The length of the graph"],ans:1,exp:"Trees have no cycles. Graphs can have cycles (A->B->C->A). Without a visited set, DFS will loop forever."},
      {q:"What is an 'In-Order Traversal' of a Binary Tree?",opts:["A. It's a type of BFS","B. It's a specific type of DFS where you visit Left, Root, Right","C. It's a sorting algorithm","D. It doesn't exist"],ans:1,exp:"Pre-order, In-order, and Post-order are all variations of Depth-First Search."},
      {q:"If you are trying to solve a Maze (finding any path to the exit), which algorithm feels most natural?",opts:["A. BFS","B. DFS","C. Binary Search","D. Quick Sort"],ans:1,exp:"DFS mimics how a human solves a maze: pick a path, follow it to a dead end, backtrack, pick another path."}
    ],
    flows:[
      {title:"DFS Recursion (Pre-order)",items:["start:dfs(node)","dec:Is node null?","proc:(Yes) Return","proc:(No) Print node.val","proc:dfs(node.left)","end:dfs(node.right)"]}
    ],
    game:{icon:"🕳️",title:"The Diver",desc:"Master deep traversal",badges:["🕳️ Deep Diver","🥞 Stack Master","🔙 Backtracker"],challenges:[{icon:"📝",title:"Graph DFS",desc:"Explain why Graphs need a Visited set",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Tree DFS",badge:"Explorer",desc:"Write a recursive DFS to print a tree.",tags:["Algorithms","DFS"],steps:[{title:"Base Case",desc:"If node is null, return"},{"title:"Process",desc:"Console log the node's value (Pre-order)"},{"title:"Recurse",desc:"Call dfs(node.left), then dfs(node.right)"}],code:`function dfs(node) {\n  if (!node) return;\n  \n  console.log(node.val); // Pre-order visit\n  \n  dfs(node.left);\n  dfs(node.right);\n}`}
  },
  t49: {
    tag:'Phase 1 · Algorithms', num:49,
    title:'BFS',
    desc:'Breadth-First Search: Exploring a tree or graph level-by-level.',
    theory:`<div class="card"><h3>🌊 The Rippling Wave</h3><p><strong>Breadth-First Search (BFS)</strong> explores data <em>wide</em> before it goes deep. It visits all direct neighbors (level 1), then all their neighbors (level 2), rippling outward like a stone dropped in a pond.</p><h4>Implementation</h4><p>BFS is implemented using a <strong>Queue (FIFO)</strong>. You enqueue the starting node, then in a loop: Dequeue a node, process it, and Enqueue all of its children/neighbors.</p><div class="box b-cy"><h5>The Superpower: Shortest Path</h5><p>In an unweighted graph (like a maze or a social network), BFS is <strong>guaranteed to find the shortest path</strong> to the target. (e.g. Degrees of separation from Kevin Bacon).</p></div></div>`,
    mcqs:[
      {q:"Which data structure is fundamentally linked to Breadth-First Search (BFS)?",opts:["A. Stack","B. Queue (FIFO)","C. HashMap","D. Trie"],ans:1,exp:"A Queue ensures that nodes discovered first (level 1) are processed before nodes discovered later (level 2)."},
      {q:"What is the absolute best use case for BFS?",opts:["A. Finding the shortest path in an unweighted graph/grid","B. Solving a Sudoku puzzle","C. Printing a BST in sorted order","D. Sorting an array"],ans:0,exp:"Because it explores level-by-level, the first time you hit the target, it is guaranteed to be the shortest path."},
      {q:"How does BFS differ from DFS conceptually?",opts:["A. BFS uses recursion, DFS uses loops","B. BFS goes wide (level-by-level), DFS goes deep (branch-by-branch)","C. BFS is only for arrays","D. They are the same"],ans:1,exp:"BFS ripples outwards. DFS plunges downwards."},
      {q:"If you want to find out the 'Degrees of Separation' between you and Elon Musk on Twitter, what algorithm do you use?",opts:["A. Binary Search","B. DFS","C. BFS","D. Bubble Sort"],ans:2,exp:"Check your friends (1 degree). Then their friends (2 degrees). This is a level-by-level BFS."},
      {q:"When using BFS on a Graph, what must you do to prevent infinite loops?",opts:["A. Use a Stack","B. Use a 'Visited' Set so you don't enqueue the same node twice","C. Delete the graph","D. Sort it"],ans:1,exp:"Just like DFS, graphs have cycles. You must track what you have already visited."}
    ],
    flows:[
      {title:"BFS Queue Flow",items:["start:Queue: [Root]","proc:Dequeue Root. Enqueue Left, Right","proc:Queue: [Left, Right]","proc:Dequeue Left. Enqueue its children","end:Continues level by level"]}
    ],
    game:{icon:"🌊",title:"The Wave",desc:"Master wide traversal",badges:["🌊 Rippler","🚶 Queue Master","📏 Shortest Path"],challenges:[{icon:"📝",title:"BFS vs DFS",desc:"When to use BFS over DFS?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Tree Level Order",badge:"Leveler",desc:"Write a BFS to print a tree level-by-level.",tags:["Algorithms","BFS"],steps:[{title:"Init Queue",desc:"Create queue = [root]"},{"title:"While Loop",desc:"while queue.length > 0"},{"title:"Process",desc:"shift() node, print val, push() left and right children"}],code:`function bfs(root) {\n  if (!root) return;\n  let q = [root]; // Array acting as Queue\n  \n  while (q.length > 0) {\n    let node = q.shift(); // Dequeue front\n    console.log(node.val);\n    \n    if (node.left) q.push(node.left);\n    if (node.right) q.push(node.right);\n  }\n}`}
  },
"""

start_marker = "};\n\nlet userXP"
inject_idx = content.find(start_marker)

if inject_idx != -1:
    new_content = content[:inject_idx] + ",\n" + rich_content + content[inject_idx:]
    with open(html_path, "w") as f:
        f.write(new_content)
    print("Successfully generated T45-T49 rich content!")
else:
    print("Could not find injection point.")
