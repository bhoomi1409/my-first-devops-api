import re

html_path = "/Users/bhoomim/devops CI:CD/handbook/fullstack_ai_handbook.html"
with open(html_path, "r") as f:
    content = f.read()

rich_content = r"""
  t50: {
    tag:'Phase 1 · Algorithms', num:50,
    title:'Dynamic Programming',
    desc:'Solving complex problems by breaking them down into simpler overlapping subproblems and caching the results.',
    theory:`<div class="card"><h3>🧠 Remembering the Past</h3><p><strong>Dynamic Programming (DP)</strong> is an optimization technique. If you have a recursive algorithm that keeps calculating the exact same thing over and over again (overlapping subproblems), DP says: <em>"Calculate it once, save it, and just look it up next time."</em></p><h4>Two DP Approaches</h4><ol><li><strong>Top-Down (Memoization):</strong> Keep your recursive function, but add a HashMap (cache). Check the cache before computing.</li><li><strong>Bottom-Up (Tabulation):</strong> Ditch recursion entirely. Start at the base case and use a loop to build an array of solutions up to your target.</li></ol></div>`,
    mcqs:[
      {q:"What are the two requirements for a problem to be solvable with Dynamic Programming?",opts:["A. It must use Strings and Arrays","B. Overlapping Subproblems (doing the exact same calculation repeatedly) and Optimal Substructure (the overall optimal solution is built from optimal sub-solutions)","C. It must be linear and sorted","D. It must use a database"],ans:1,exp:"Fibonacci is the classic example. fib(5) calculates fib(3) multiple times."},
      {q:"What is 'Memoization'?",opts:["A. A Top-Down approach where you cache the results of recursive function calls in a HashMap/Array to avoid recomputing them","B. Memorizing syntax","C. Writing documentation","D. A Bottom-Up loop"],ans:0,exp:"Memoization trades a little bit of memory (O(N) Space) to turn O(2^N) exponential time into O(N) linear time!"},
      {q:"What is 'Tabulation'?",opts:["A. A Top-Down recursive approach","B. A Bottom-Up approach where you use an iterative loop to fill a table (array) starting from the base cases up to the target","C. Creating tabs in a browser","D. A Database table"],ans:1,exp:"Tabulation avoids the Call Stack entirely, preventing Stack Overflow errors on deep problems."},
      {q:"Without DP, what is the Time Complexity of a naive recursive Fibonacci function?",opts:["A. O(1)","B. O(N)","C. O(N log N)","D. O(2^N) Exponential"],ans:3,exp:"It branches into two calls, which branch into four, then eight... It will freeze your computer at fib(50)."},
      {q:"With DP (Memoization), what is the Time Complexity of that same Fibonacci function?",opts:["A. O(1)","B. O(N) Linear","C. O(N log N)","D. O(2^N)"],ans:1,exp:"Because every unique number is only calculated ONCE and then cached, it just takes N steps!"}
    ],
    flows:[
      {title:"Memoized Fibonacci",items:["start:fib(5) called","dec:Is 5 in cache?","proc:(No) Calculate fib(4) + fib(3)","proc:Store result in cache[5]","end:Return result"]}
    ],
    game:{icon:"🧠",title:"The Memoizer",desc:"Master dynamic programming",badges:["🧠 Cache Master","📝 Tabulator","📉 Exponential Slayer"],challenges:[{icon:"📝",title:"Top vs Bottom",desc:"Explain Memoization vs Tabulation",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Fibonacci with DP",badge:"Optimizer",desc:"Transform an O(2^N) algorithm into an O(N) algorithm.",tags:["Algorithms","DP"],steps:[{title:"Init Cache",desc:"Pass an object/map into the recursive function"},{"title:"Check Cache",desc:"If memo[n] exists, return it immediately"},{"title:"Calculate & Store",desc:"memo[n] = fib(n-1) + fib(n-2)"}],code:`function fib(n, memo = {}) {\n  if (n in memo) return memo[n]; // Instant return\n  if (n <= 1) return n;\n  \n  memo[n] = fib(n-1, memo) + fib(n-2, memo);\n  return memo[n];\n}\n\nconsole.log(fib(50)); // Completes instantly instead of freezing!`}
  },
  t51: {
    tag:'Phase 1 · Algorithms', num:51,
    title:'Greedy Algorithms',
    desc:'Making the locally optimal choice at each step with the hope of finding a global optimum.',
    theory:`<div class="card"><h3>🤑 Take the Best Now</h3><p>A <strong>Greedy Algorithm</strong> doesn't look at the big picture or plan for the future. At every single step, it simply picks the option that looks best <em>right now</em>.</p><h4>When does it work?</h4><p>It works perfectly for problems like finding the shortest path (Dijkstra) or giving change using the fewest coins (if using US currency). You just keep taking the biggest coin possible.</p><div class="box b-ro"><h5>⚠️ The Trap</h5><p>Greedy algorithms can fail spectacularly on certain problems (like the Knapsack problem or giving change with weird currency). Sometimes, taking the "best" choice now forces you into a terrible situation later. In those cases, you must use Dynamic Programming to explore all paths.</p></div></div>`,
    mcqs:[
      {q:"What defines a Greedy Algorithm?",opts:["A. It explores every possible path","B. It makes the locally optimal choice at each step without looking ahead","C. It uses a lot of memory","D. It takes the longest path"],ans:1,exp:"It 'greedily' grabs the best immediate option."},
      {q:"Does a Greedy Algorithm always guarantee the absolute best (globally optimal) solution?",opts:["A. Yes, always","B. No, it can sometimes get stuck in a 'local maximum' and fail to find the true best solution","C. Yes, if you use a while loop","D. No, it never works"],ans:1,exp:"If a greedy algorithm takes the $10 bill now, it might miss the $100 bill hidden down the other path."},
      {q:"Which famous algorithm uses a Greedy approach to find the shortest path in a graph?",opts:["A. Merge Sort","B. Dijkstra's Algorithm","C. Binary Search","D. DFS"],ans:1,exp:"Dijkstra always processes the node that is currently closest (cheapest) to the start."},
      {q:"If you need to make 30 cents in change using standard US coins (25, 10, 5, 1), how does a greedy algorithm do it?",opts:["A. Takes 1 quarter, then 1 nickel","B. Takes 3 dimes","C. Takes 30 pennies","D. Fails"],ans:0,exp:"It greedly grabs the biggest coin possible (25), leaving 5. Then it grabs the biggest possible (5). This happens to be the optimal solution!"},
      {q:"What happens if you have weird coins (25, 20, 10, 1) and need 40 cents?",opts:["A. Greedy takes 20 + 20 (Optimal)","B. Greedy takes 25, then 10, then 5 pennies (6 coins) - failing to find the optimal 2-coin solution","C. Greedy crashes","D. It works perfectly"],ans:1,exp:"This proves why Greedy fails on certain datasets, requiring Dynamic Programming instead."}
    ],
    flows:[
      {title:"Greedy Coin Change (40c)",items:["start:Need 40. Coins: 25,10,1","proc:Grab 25 (15 left)","proc:Grab 10 (5 left)","end:Grab five 1s. Total: 7 coins. (Optimal was 20+20)"]}
    ],
    game:{icon:"🤑",title:"The Glutton",desc:"Master greedy logic",badges:["🤑 Immediate Gratification","🪙 Coin Changer","📉 Local Maximum"],challenges:[{icon:"📝",title:"When it fails",desc:"Explain a scenario where Greedy fails",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Greedy Change Maker",badge:"Cashier",desc:"Implement a greedy algorithm to dispense coins.",tags:["Algorithms","Greedy"],steps:[{title:"Coins Array",desc:"[25, 10, 5, 1]"},{"title:"Loop",desc:"Iterate through coins"},{"title:"Math",desc:"While amount >= coin, subtract coin and push to result"}],code:`function makeChange(amount) {\n  let coins = [25, 10, 5, 1];\n  let result = [];\n  \n  for (let c of coins) {\n    while (amount >= c) {\n      result.push(c);\n      amount -= c;\n    }\n  }\n  return result;\n}\nconsole.log(makeChange(41)); // [25, 10, 5, 1]`}
  },
  t52: {
    tag:'Phase 1 · Algorithms', num:52,
    title:'Sliding Window',
    desc:'An optimization technique for iterating over contiguous subarrays or substrings.',
    theory:`<div class="card"><h3>🪟 The Moving Frame</h3><p>The <strong>Sliding Window</strong> technique is used to solve problems involving a contiguous sequence of elements (like finding the longest substring or the maximum sum of 3 consecutive numbers).</p><h4>Why use it?</h4><p>The naive approach is a nested loop <code>O(N^2)</code> that recalculates the entire subarray every time. Sliding Window uses two pointers to create a "window". You simply add the new element entering the window, and subtract the old element leaving the window. This drops the Time Complexity to <code>O(N)</code>!</p></div>`,
    mcqs:[
      {q:"What is the primary visual analogy for the Sliding Window technique?",opts:["A. A window sliding down a building","B. A fixed or flexible frame sliding across an array, adding new items on the right and removing old ones on the left","C. Opening a new window in the browser","D. Throwing data out a window"],ans:1,exp:"You maintain a running state (like a sum) within the window's boundaries."},
      {q:"What kind of problems is Sliding Window best suited for?",opts:["A. Sorting an array","B. Searching a tree","C. Problems involving contiguous subarrays or substrings (e.g., 'max sum of 3 consecutive items')","D. Database queries"],ans:2,exp:"The keyword is usually 'contiguous' or 'consecutive'."},
      {q:"How does Sliding Window improve Time Complexity?",opts:["A. From O(N) to O(1)","B. From O(N^2) (nested loops) to O(N) by reusing the calculations from the previous window position","C. It doesn't improve time","D. By using multiple CPUs"],ans:1,exp:"Instead of summing 3 items every time, you just subtract the item that fell out the back, and add the item that came in the front."},
      {q:"Can the window size change?",opts:["A. No, it must be fixed","B. Yes, 'Dynamic Sliding Windows' expand and contract based on a condition (like finding the longest substring without repeating characters)","C. Only in Java","D. Only if it's smaller than 10"],ans:1,exp:"Dynamic windows use two pointers (left and right) that move independently."},
      {q:"Which of these is NOT a good fit for Sliding Window?",opts:["A. Longest substring with K distinct characters","B. Maximum sum subarray of size K","C. Finding if an array contains a specific number","D. Minimum size subarray sum >= target"],ans:2,exp:"Finding a specific number is just a standard Search problem. Sliding Window is for sequences."}
    ],
    flows:[
      {title:"Fixed Window Flow (Sum of 3)",items:["start:[1, 2, 3, 4]","proc:Window 1: [1,2,3] Sum = 6","proc:Slide Right ->","end:Subtract 1, Add 4. Sum = 9."]}
    ],
    game:{icon:"🪟",title:"Window Washer",desc:"Master contiguous arrays",badges:["🪟 Slider","📉 O(N) Optimizer","🐛 Caterpillar"],challenges:[{icon:"📝",title:"Identify It",desc:"List 2 Sliding Window keywords",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Max Subarray Sum",badge:"Optimizer",desc:"Find the max sum of K consecutive elements in O(N).",tags:["Algorithms","Sliding Window"],steps:[{title:"Initial Window",desc:"Sum the first K elements"},{"title:"Slide",desc:"Loop from K to end of array"},{"title:"Update Sum",desc:"sum = sum - arr[i-k] + arr[i]"}],code:`function maxSum(arr, k) {\n  let maxSum = 0, tempSum = 0;\n  for(let i=0; i<k; i++) tempSum += arr[i]; // First window\n  maxSum = tempSum;\n  \n  for(let i=k; i<arr.length; i++) {\n    // Slide: subtract outgoing, add incoming\n    tempSum = tempSum - arr[i-k] + arr[i];\n    maxSum = Math.max(maxSum, tempSum);\n  }\n  return maxSum;\n}`}
  },
  t53: {
    tag:'Phase 1 · Algorithms', num:53,
    title:'Two Pointers',
    desc:'Using two independent index pointers to iterate through data efficiently.',
    theory:`<div class="card"><h3>👉👈 Meeting in the Middle</h3><p>The <strong>Two Pointers</strong> technique involves using two variables (usually representing indices) to traverse an array or string. It is often used to optimize <code>O(N^2)</code> solutions down to <code>O(N)</code>.</p><h4>Common Patterns</h4><ol><li><strong>Start and End:</strong> One pointer at index 0, one at the last index. They move inward towards each other. (e.g., Reversing an array, checking Palindromes, or finding a target sum in a <em>sorted</em> array).</li><li><strong>Fast and Slow (Tortoise & Hare):</strong> Both start at 0, but one moves faster (e.g., jumps 2 steps) than the other. (e.g., Finding the middle of a Linked List, or detecting a cycle).</li></ol></div>`,
    mcqs:[
      {q:"What is a 'pointer' in the context of the Two Pointers technique in JavaScript/Python?",opts:["A. A memory address variable","B. Just a simple integer variable holding an array index (e.g. let left = 0)","C. A mouse cursor","D. A boolean flag"],ans:1,exp:"While C++ uses literal memory pointers, in high-level languages we just use index integers."},
      {q:"If you want to reverse an array in-place in O(N) time and O(1) space, how do you use Two Pointers?",opts:["A. Start both at 0 and move right","B. Start 'left' at 0 and 'right' at the end. Swap their values, then move them inward (left++, right--) until they cross.","C. It's impossible","D. Start both at the end"],ans:1,exp:"This is the classic O(1) space reversal algorithm."},
      {q:"When using Two Pointers to find a pair of numbers that add up to a Target, what MUST be true about the array?",opts:["A. It must be empty","B. It must be sorted","C. It must have negative numbers","D. It must be an array of strings"],ans:1,exp:"If sorted, you can do: if sum is too big, move Right pointer left. If too small, move Left pointer right."},
      {q:"What is the 'Fast and Slow' (Tortoise and Hare) pointer pattern typically used for?",opts:["A. Sorting an array","B. Detecting cycles/loops in a Linked List (if the fast pointer laps and catches the slow pointer, there's a loop)","C. Hashing strings","D. Rendering HTML"],ans:1,exp:"Floyd's Cycle-Finding Algorithm uses a fast pointer (moves 2 steps) and a slow pointer (moves 1 step)."},
      {q:"Why is Two Pointers better than a nested loop?",opts:["A. It looks cooler","B. It reduces Time Complexity from O(N^2) to O(N) by traversing the array only once or twice","C. It uses more memory","D. It compiles faster"],ans:1,exp:"By strategically moving pointers, you avoid checking every possible combination."}
    ],
    flows:[
      {title:"Two Sum (Sorted Array)",items:["start:[1, 3, 5, 8, 10]. Target 8.","proc:L(1) + R(10) = 11. (Too big)","proc:Move R left.","dec:L(1) + R(8) = 9. (Too big)","proc:Move R left.","end:L(3) + R(5) = 8. Found!"]}
    ],
    game:{icon:"👉",title:"The Pointer",desc:"Master index manipulation",badges:["👉👈 Inward Mover","🐢 Tortoise & Hare","📉 O(N) Optimizer"],challenges:[{icon:"📝",title:"Identify Pattern",desc:"When to use Fast/Slow?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Two Sum (Sorted)",badge:"Matchmaker",desc:"Find two numbers that add up to a target in O(N).",tags:["Algorithms","Two Pointers"],steps:[{title:"Init Pointers",desc:"left = 0, right = arr.length - 1"},{"title:"Loop",desc:"while (left < right)"},{"title:"Logic",desc:"If sum === target return. If sum > target right--. If sum < target left++"}],code:`function twoSumSorted(arr, target) {\n  let left = 0, right = arr.length - 1;\n  while (left < right) {\n    let sum = arr[left] + arr[right];\n    if (sum === target) return [arr[left], arr[right]];\n    if (sum > target) right--;\n    else left++;\n  }\n  return null;\n}`}
  },
"""

start_marker = "};\n\nlet userXP"
inject_idx = content.find(start_marker)

if inject_idx != -1:
    new_content = content[:inject_idx] + ",\n" + rich_content + content[inject_idx:]
    with open(html_path, "w") as f:
        f.write(new_content)
    print("Successfully generated T50-T53 rich content!")
else:
    print("Could not find injection point.")
