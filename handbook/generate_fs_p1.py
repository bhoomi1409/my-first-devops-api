import re

html_path = "/Users/bhoomim/devops CI:CD/handbook/fullstack_ai_handbook.html"
with open(html_path, "r") as f:
    content = f.read()

rich_content = """
const RICH_TOPICS = {
  t1: {
    tag:'Phase 1 · Core Foundations', num:1,
    title:'Variables',
    desc:'The fundamental building blocks of programming used to store, retrieve, and manipulate data.',
    theory:`<div class="card"><h3>📦 What is a Variable?</h3><p>Think of a variable as a labeled box in your computer's memory. You put data (like a number or a word) into the box, and you use the label to find that data later.</p><h4>Variable Declaration & Assignment</h4><ul><li><strong>Declaration:</strong> Reserving the memory space and naming it.</li><li><strong>Assignment:</strong> Storing a specific value into that space.</li></ul><div class="cb"><span class="cm">// JavaScript Example</span>
<span class="ck">let</span> <span class="cv">playerName</span> = <span class="cs">"Bhoomi"</span>;  <span class="cm">// String</span>
<span class="ck">let</span> <span class="cv">score</span> = <span class="cs">150</span>;          <span class="cm">// Number</span>
<span class="ck">const</span> <span class="cv">MAX_LEVEL</span> = <span class="cs">50</span>;     <span class="cm">// Constant (cannot change)</span></div><h4>Variables in Memory</h4><p>Under the hood, the variable name <code>score</code> is mapped to a specific hexadecimal memory address (e.g., <code>0x7FF09A</code>). The CPU reads/writes to this address.</p></div>`,
    mcqs:[
      {q:"What is the primary purpose of a variable?",opts:["A. To run loops","B. To store and retrieve data in memory","C. To connect to the internet","D. To style a webpage"],ans:1,exp:"Variables act as named storage locations in memory."},
      {q:"What does the 'const' keyword do in JavaScript?",opts:["A. Makes the variable public","B. Prevents the variable from being reassigned","C. Deletes the variable","D. Changes the variable to a string"],ans:1,exp:"Constants (const) cannot be reassigned after their initial declaration."},
      {q:"Which of the following is a valid variable naming convention in most languages?",opts:["A. 1stPlayer","B. first player","C. firstPlayer","D. first-player"],ans:2,exp:"camelCase (firstPlayer) is standard. Variable names cannot contain spaces or start with numbers."},
      {q:"What happens under the hood when you declare a variable?",opts:["A. The CPU gets faster","B. The OS allocates a specific memory address and maps the variable name to it","C. A new file is created on the hard drive","D. Nothing happens until you print it"],ans:1,exp:"Variables map human-readable names to physical memory addresses."},
      {q:"What is 'initialization'?",opts:["A. Deleting a variable","B. Declaring a variable and assigning it a value for the very first time","C. Using a variable in a math equation","D. Writing a function"],ans:1,exp:"Initialization is the first assignment of a value to a newly declared variable."}
    ],
    flows:[
      {title:"Variable Lifecycle",items:["start:Declare (let x)","proc:Allocate Memory","proc:Assign Value (x = 5)","proc:Write to Memory","end:Read/Use Variable"]}
    ],
    game:{icon:"📦",title:"Variable Vanguard",desc:"Master data storage",badges:["📦 Storer","🏷️ Labeler","⚡ Memory Mapper"],challenges:[{icon:"📝",title:"Declare It",desc:"Write code to declare 3 variables",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Score Tracker",badge:"Tracker",desc:"Use variables to build a simple score tracking logic block.",tags:["JavaScript","Variables"],steps:[{title:"Declare",desc:"Create variables for score and player name"},{title:"Update",desc:"Increase score by 100"},{title:"Output",desc:"Print the final score message"}],code:`let playerName = "Hero";\nlet currentScore = 0;\n\n// Player defeats an enemy\ncurrentScore = currentScore + 100;\n\nconsole.log(playerName + " has " + currentScore + " points!");`}
  },
  t2: {
    tag:'Phase 1 · Core Foundations', num:2,
    title:'Data Types',
    desc:'How programming languages categorize and understand different kinds of information.',
    theory:`<div class="card"><h3>🗂️ Primitives vs References</h3><p>Data types tell the compiler/interpreter how to handle the data in a variable (e.g., you can multiply numbers, but not strings).</p><h4>Primitive Types (Stored directly in Stack)</h4><ul><li><strong>Integer/Number:</strong> Whole numbers (10) or floats (3.14)</li><li><strong>String:</strong> Text ("Hello World")</li><li><strong>Boolean:</strong> True or False</li><li><strong>Null / Undefined:</strong> Intentional absence of value vs uninitialized</li></ul><h4>Reference Types (Stored in Heap, pointer in Stack)</h4><ul><li><strong>Arrays/Lists:</strong> Ordered collections [1, 2, 3]</li><li><strong>Objects/Dictionaries:</strong> Key-value pairs {name: "Bhoomi"}</li></ul><div class="box b-ro"><h5>⚠️ Static vs Dynamic Typing</h5><p>In <strong>statically typed</strong> languages (Java, C++), a variable's type is checked at compile-time and cannot change. In <strong>dynamically typed</strong> languages (Python, JS), a variable can hold a string, then later hold a number.</p></div></div>`,
    mcqs:[
      {q:"Which of these is a Primitive data type?",opts:["A. Array","B. Boolean","C. Object","D. Class"],ans:1,exp:"Booleans (true/false) are simple primitives. Arrays and Objects are reference types."},
      {q:"In a statically typed language like Java, what happens if you assign a string to an integer variable?",opts:["A. It converts it automatically","B. The compiler throws a type error","C. It stores the length of the string","D. It ignores it"],ans:1,exp:"Statically typed languages enforce strict type checking at compile time."},
      {q:"What is the difference between Null and Undefined in JS?",opts:["A. They are the same","B. Null is an intentional absence of value; Undefined means a variable was declared but not assigned","C. Undefined is for numbers, Null is for strings","D. Null causes a crash"],ans:1,exp:"Null is explicitly set by the programmer. Undefined is the default uninitialized state."},
      {q:"Where are Reference types (like large Objects) stored in memory?",opts:["A. The Stack","B. The CPU Cache","C. The Heap","D. The Hard Drive"],ans:2,exp:"Large, dynamic objects are stored in the Heap, while a pointer to them is kept on the Stack."},
      {q:"What happens when you add a String and a Number in JavaScript (e.g., '5' + 3)?",opts:["A. It equals 8","B. It throws an error","C. Type coercion occurs, resulting in the string '53'","D. It crashes"],ans:2,exp:"JS dynamically coerces the number into a string and concatenates them."}
    ],
    flows:[
      {title:"Type Checking Flow",items:["start:Assign x = 5","dec:Static or Dynamic?","proc:(Static) Check Type Rules","proc:(Dynamic) Update Type Tag at Runtime","end:Store Value"]}
    ],
    game:{icon:"🗂️",title:"Type Titan",desc:"Master data categorization",badges:["🔢 Number Cruncher","🔤 String Weaver","⚖️ Boolean Boss"],challenges:[{icon:"📝",title:"Identify Types",desc:"List the type of 5 different values",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Data Type Formatter",badge:"Formatter",desc:"Write a function that handles different data types differently.",tags:["JavaScript","Data Types"],steps:[{title:"Input Check",desc:"Use typeof to check the input"},{title:"String handling",desc:"If string, convert to uppercase"},{title:"Number handling",desc:"If number, multiply by 10"}],code:`function formatData(input) {\n  if (typeof input === "string") {\n    return input.toUpperCase();\n  } else if (typeof input === "number") {\n    return input * 10;\n  }\n  return null;\n}\n\nconsole.log(formatData("hello")); // HELLO\nconsole.log(formatData(5));     // 50`}
  },
  t3: {
    tag:'Phase 1 · Core Foundations', num:3,
    title:'Operators',
    desc:'Symbols that tell the compiler or interpreter to perform specific mathematical, relational or logical operations.',
    theory:`<div class="card"><h3>🧮 Types of Operators</h3><p>Operators manipulate variables and values to produce new results.</p><h4>1. Arithmetic</h4><ul><li>Addition (+), Subtraction (-), Multiplication (*), Division (/)</li><li><strong>Modulo (%):</strong> Returns the remainder (e.g., 10 % 3 = 1). Crucial for checking even/odd numbers.</li></ul><h4>2. Relational (Comparison)</h4><ul><li>Equal (==), Strict Equal (===), Not Equal (!=)</li><li>Greater than (>), Less than or equal (<=)</li></ul><h4>3. Logical</h4><ul><li><strong>AND (&&):</strong> True only if BOTH sides are true.</li><li><strong>OR (||):</strong> True if AT LEAST ONE side is true.</li><li><strong>NOT (!):</strong> Inverts the boolean (e.g., !true = false).</li></ul><div class="cb"><span class="cm">// Example</span>
<span class="ck">let</span> <span class="cv">isAdult</span> = age >= <span class="cs">18</span>;
<span class="ck">let</span> <span class="cv">hasTicket</span> = <span class="cs">true</span>;
<span class="ck">let</span> <span class="cv">canEnter</span> = isAdult && hasTicket;</div></div>`,
    mcqs:[
      {q:"What does the Modulo (%) operator do?",opts:["A. Calculates percentages","B. Returns the remainder of a division","C. Multiplies two numbers","D. Converts to a string"],ans:1,exp:"10 % 3 equals 1, because 10 divided by 3 is 9, with a remainder of 1."},
      {q:"What is the difference between == and === in JavaScript?",opts:["A. == is faster","B. === checks both value AND data type, preventing weird type coercion","C. == is for strings, === is for numbers","D. They are identical"],ans:1,exp:"'5' == 5 is true. '5' === 5 is false because the types (String vs Number) don't match."},
      {q:"If A is true and B is false, what is the result of (A && B)?",opts:["A. true","B. false","C. undefined","D. error"],ans:1,exp:"The AND (&&) operator requires BOTH sides to be true."},
      {q:"If A is true and B is false, what is the result of (A || B)?",opts:["A. true","B. false","C. undefined","D. error"],ans:0,exp:"The OR (||) operator requires at least ONE side to be true."},
      {q:"What does the NOT (!) operator do?",opts:["A. Deletes a variable","B. Inverts a boolean (true becomes false)","C. Makes a number negative","D. Halts the program"],ans:1,exp:"!true evaluates to false, and !false evaluates to true."}
    ],
    flows:[
      {title:"Logical Evaluation (AND)",items:["start:Evaluate Left Side","dec:Is Left True?","proc:(No) Short-circuit Return False","proc:(Yes) Evaluate Right Side","end:Return Right Side Result"]}
    ],
    game:{icon:"🧮",title:"Operator Overlord",desc:"Master logical and math operations",badges:["➕ Adder","⚖️ Comparator","🧠 Logician"],challenges:[{icon:"🧮",title:"Modulo Math",desc:"Calculate 17 % 5",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Access Control Gateway",badge:"Gatekeeper",desc:"Use relational and logical operators to determine if a user can access a system.",tags:["JavaScript","Logic"],steps:[{title:"Variables",desc:"Set age, hasID, isBanned"},{title:"Condition",desc:"Use && and ! to evaluate access"},{title:"Output",desc:"Log true or false"}],code:`let age = 20;\nlet hasID = true;\nlet isBanned = false;\n\n// Must be 18+, have ID, and NOT be banned\nlet canAccess = (age >= 18) && hasID && !isBanned;\n\nconsole.log("Access Granted: " + canAccess);`}
  },
"""

start_marker = "const RICH_TOPICS = {"
start_idx = content.find(start_marker)

# Replace the generic t1 and inject t1-t3
if start_idx != -1:
    # Find the closing brace of RICH_TOPICS (we'll just replace the whole block)
    end_marker = "};\n\nlet userXP"
    end_idx = content.find(end_marker)
    
    if end_idx != -1:
        new_content = content[:start_idx] + rich_content + content[end_idx:]
        with open(html_path, "w") as f:
            f.write(new_content)
        print("Successfully generated T1-T3 rich content!")
    else:
        print("Could not find end of RICH_TOPICS.")
else:
    print("Could not find start of RICH_TOPICS.")
