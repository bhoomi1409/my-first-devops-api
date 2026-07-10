import re

html_path = "/Users/bhoomim/devops CI:CD/handbook/fullstack_ai_handbook.html"
with open(html_path, "r") as f:
    content = f.read()

rich_content = """
  t4: {
    tag:'Phase 1 · Core Foundations', num:4,
    title:'Loops',
    desc:'Executing a block of code multiple times to automate repetitive tasks.',
    theory:`<div class="card"><h3>🔄 The Power of Iteration</h3><p>Loops allow you to run the same code repeatedly without copy-pasting it. This is essential for iterating over data, like a list of users or a string of text.</p><h4>Types of Loops</h4><ul><li><strong>For Loop:</strong> Runs a specific number of times. Best when you know exactly how many iterations you need.</li><li><strong>While Loop:</strong> Runs as long as a condition remains true. Best when you don't know exactly when to stop (e.g., waiting for user input).</li></ul><div class="cb"><span class="cm">// For Loop</span>
<span class="ck">for</span> (<span class="ck">let</span> i = <span class="cs">0</span>; i < <span class="cs">5</span>; i++) {
    console.log(<span class="cs">"Iteration: "</span> + i);
}

<span class="cm">// While Loop</span>
<span class="ck">let</span> <span class="cv">isGameOver</span> = <span class="cs">false</span>;
<span class="ck">while</span> (!isGameOver) {
    <span class="cm">// Keep playing...</span>
}</div></div>`,
    mcqs:[
      {q:"When is it best to use a 'for' loop instead of a 'while' loop?",opts:["A. When you don't know when the loop should end","B. When you know exactly how many times you want to iterate (e.g., over an array of 10 items)","C. When you are writing in Java","D. When you want an infinite loop"],ans:1,exp:"For loops are designed for definitive iteration with a set start and end."},
      {q:"What are the three parts of a standard 'for' loop declaration (for X; Y; Z)?",opts:["A. Initialization, Condition, Increment/Decrement","B. Variable, Operator, Type","C. Start, Middle, End","D. Condition, Increment, Return"],ans:0,exp:"e.g., for(let i=0; i<10; i++)"},
      {q:"What is an 'infinite loop'?",opts:["A. A loop that runs exactly 1000 times","B. A loop where the exit condition is never met, causing the program to freeze or crash","C. A feature of AWS","D. A loop that runs backwards"],ans:1,exp:"Infinite loops are usually bugs where the state doesn't change enough to satisfy the exit condition."},
      {q:"What does the 'break' statement do inside a loop?",opts:["A. It pauses the loop for 1 second","B. It immediately exits the entire loop, regardless of the condition","C. It skips the current iteration and moves to the next one","D. It throws an error"],ans:1,exp:"Break completely escapes the loop."},
      {q:"What does the 'continue' statement do inside a loop?",opts:["A. It exits the program","B. It skips the rest of the current iteration and jumps to the next iteration","C. It pauses the loop","D. It resumes an infinite loop"],ans:1,exp:"Continue skips the current cycle but keeps the loop running."}
    ],
    flows:[
      {title:"While Loop Flow",items:["start:Loop Start","dec:Is Condition True?","proc:(No) Exit Loop","proc:(Yes) Execute Body","proc:Update State","end:Go back to Condition"]}
    ],
    game:{icon:"🔄",title:"Loop Legend",desc:"Master iteration",badges:["🔄 Iterator","🛑 Break Master","⏭️ Continuer"],challenges:[{icon:"📝",title:"Write a For Loop",desc:"Write a loop that prints 1 to 10",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Array Iteration",badge:"Looper",desc:"Use a for loop to sum an array of numbers.",tags:["JavaScript","Loops"],steps:[{title:"Create Array",desc:"Define an array of numbers"},{title:"Initialize Sum",desc:"Create a sum variable at 0"},{title:"Loop",desc:"Iterate through the array, adding each to sum"}],code:`let numbers = [10, 20, 30, 40, 50];\nlet total = 0;\n\nfor (let i = 0; i < numbers.length; i++) {\n  total += numbers[i];\n}\n\nconsole.log("Total is: " + total);`}
  },
  t5: {
    tag:'Phase 1 · Core Foundations', num:5,
    title:'Conditionals',
    desc:'Decision-making in code using if, else if, else, and switch statements.',
    theory:`<div class="card"><h3>🔀 Branching Logic</h3><p>Conditionals allow your code to make decisions. Without them, programs would run in a single straight line from top to bottom every time.</p><h4>If / Else If / Else</h4><p>The program evaluates boolean expressions top-to-bottom. It executes the block for the <strong>first</strong> true condition and skips the rest.</p><div class="cb"><span class="ck">let</span> <span class="cv">temp</span> = <span class="cs">75</span>;
<span class="ck">if</span> (temp > <span class="cs">90</span>) {
    console.log(<span class="cs">"It's hot!"</span>);
} <span class="ck">else if</span> (temp > <span class="cs">60</span>) {
    console.log(<span class="cs">"It's nice."</span>);
} <span class="ck">else</span> {
    console.log(<span class="cs">"It's cold."</span>);
}</div><h4>Switch Statements</h4><p>Useful when checking a single variable against many specific values (e.g., checking user roles: 'admin', 'editor', 'viewer').</p></div>`,
    mcqs:[
      {q:"What happens in an if/else if chain if multiple conditions are true?",opts:["A. All true blocks execute","B. Only the FIRST true block executes, the rest are skipped","C. The LAST true block executes","D. The program crashes"],ans:1,exp:"The evaluation stops as soon as it finds the first true condition."},
      {q:"When is an 'else' block executed?",opts:["A. Always","B. Only if ALL preceding 'if' and 'else if' conditions evaluate to false","C. Only if the first 'if' is true","D. Never"],ans:1,exp:"The else block acts as a catch-all default."},
      {q:"Why might you use a 'switch' statement instead of 'if/else if'?",opts:["A. It's more secure","B. It handles loops better","C. It can be cleaner/more readable when checking a single variable against many specific exact values","D. It runs asynchronously"],ans:2,exp:"Switches are great for enums or state checking (e.g., 'loading', 'success', 'error')."},
      {q:"What happens if you forget a 'break' in a switch statement (in JS/C++)?",opts:["A. The program throws an error","B. Execution 'falls through' to the next case, running its code even if it doesn't match","C. It loops infinitely","D. It skips to the end"],ans:1,exp:"Fall-through is a common bug (or sometimes intentional pattern) in switch statements."},
      {q:"What is a Ternary operator (e.g., condition ? true_val : false_val)?",opts:["A. A loop","B. A database query","C. A shorthand, one-line if/else statement used for assigning values","D. A type of variable"],ans:2,exp:"Ternaries are clean ways to assign a value based on a condition inline."}
    ],
    flows:[
      {title:"If/Else Flow",items:["start:Condition 1","dec:True?","proc:(Yes) Run Block 1","proc:(No) Condition 2","dec:True?","proc:(Yes) Run Block 2","proc:(No) Run Else Block","end:Done"]}
    ],
    game:{icon:"🔀",title:"Decision Maker",desc:"Master code branching",badges:["🔀 Brancher","🔌 Switcher","❓ Ternary Master"],challenges:[{icon:"📝",title:"Write If/Else",desc:"Write code to check if a number is even",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"FizzBuzz Logic",badge:"Interviewer",desc:"Implement the classic FizzBuzz interview problem.",tags:["JavaScript","Conditionals"],steps:[{title:"Loop",desc:"Loop from 1 to 15"},{title:"Condition 1",desc:"If divisible by 3 AND 5, print FizzBuzz"},{title:"Condition 2",desc:"If divisible by 3, print Fizz"},{title:"Condition 3",desc:"If divisible by 5, print Buzz"},{title:"Default",desc:"Else, print the number"}],code:`for (let i = 1; i <= 15; i++) {\n  if (i % 3 === 0 && i % 5 === 0) {\n    console.log("FizzBuzz");\n  } else if (i % 3 === 0) {\n    console.log("Fizz");\n  } else if (i % 5 === 0) {\n    console.log("Buzz");\n  } else {\n    console.log(i);\n  }\n}`}
  },
  t6: {
    tag:'Phase 1 · Core Foundations', num:6,
    title:'Functions',
    desc:'Reusable blocks of code that take inputs, perform logic, and return an output.',
    theory:`<div class="card"><h3>🏭 The Code Factory</h3><p>Functions are the core building blocks of modular programming. You define them once, and call them many times with different arguments.</p><h4>Key Terms</h4><ul><li><strong>Parameters:</strong> Variables listed in the function definition (the "holes" waiting to be filled).</li><li><strong>Arguments:</strong> The actual data you pass in when calling the function.</li><li><strong>Return:</strong> The value the function spits back out to the caller.</li></ul><div class="cb"><span class="cm">// Declaration</span>
<span class="ck">function</span> <span class="cv">calculateArea</span>(width, height) {
    <span class="ck">return</span> width * height;
}

<span class="cm">// Execution</span>
<span class="ck">let</span> <span class="cv">area1</span> = calculateArea(<span class="cs">10</span>, <span class="cs">5</span>); <span class="cm">// Returns 50</span>
<span class="ck">let</span> <span class="cv">area2</span> = calculateArea(<span class="cs">3</span>, <span class="cs">3</span>);  <span class="cm">// Returns 9</span></div></div>`,
    mcqs:[
      {q:"What is the difference between a parameter and an argument?",opts:["A. They are the same","B. Parameters are the variables in the definition; Arguments are the actual values passed during the call","C. Arguments are in the definition; Parameters are passed","D. Parameters are for loops"],ans:1,exp:"Parameters act as placeholders in the function signature."},
      {q:"What happens immediately after a 'return' statement executes in a function?",opts:["A. The function keeps running","B. The function halts execution and sends the value back to the caller","C. An error is thrown","D. The loop breaks"],ans:1,exp:"'return' acts as an immediate exit point for the function."},
      {q:"What is a 'side effect' in a function?",opts:["A. When the function crashes","B. When a function modifies a variable outside its local scope, such as updating a global variable or DOM element","C. Returning a value","D. A syntax error"],ans:1,exp:"Pure functions have no side effects (they only depend on inputs and return outputs). Impure functions modify external state."},
      {q:"What does DRY stand for in programming?",opts:["A. Do Repeat Yourself","B. Don't Repeat Yourself (accomplished by wrapping repetitive code in functions)","C. Data Retrieval Yarn","D. Direct Return Yield"],ans:1,exp:"Functions are the primary tool for keeping code DRY."},
      {q:"If a JS function has no return statement, what does it return by default?",opts:["A. 0","B. null","C. undefined","D. It throws an error"],ans:2,exp:"Functions implicitly return undefined if no explicit return is provided."}
    ],
    flows:[
      {title:"Function Call Stack",items:["start:Main Code Runs","proc:Call funcA()","proc:funcA Runs","proc:Call funcB()","proc:funcB Returns","proc:funcA Returns","end:Main Code Continues"]}
    ],
    game:{icon:"🏭",title:"Factory Foreman",desc:"Master function creation",badges:["🏭 Modulator","📥 Argument Passer","📤 Returner"],challenges:[{icon:"📝",title:"Write a Function",desc:"Write a function that multiples by 2",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Math Utility Library",badge:"Librarian",desc:"Create a set of reusable math functions.",tags:["JavaScript","Functions"],steps:[{title:"Add/Sub",desc:"Create add() and subtract() functions"},{title:"Multiply/Div",desc:"Create multiply() and divide() functions"},{title:"Call them",desc:"Test them by logging results"}],code:`function add(a, b) { return a + b; }\nfunction subtract(a, b) { return a - b; }\n\nconsole.log(add(10, 5));      // 15\nconsole.log(subtract(10, 5)); // 5`}
  },
"""

start_marker = "  t4:"
start_idx = content.find(start_marker)

# Since t4 doesn't exist yet, we inject it right after t3
if start_idx == -1:
    inject_marker = "  t4: {" # Wait, we need to inject after the end of t3.
    # Let's just find "};\n\nlet userXP" and inject before it
    inject_marker = "};\n\nlet userXP"
    inject_idx = content.find(inject_marker)
    
    if inject_idx != -1:
        # Add a comma if needed, but in our previous script we didn't add a trailing comma to t3.
        # So we need to do string manipulation carefully.
        # Actually, let's just find the last '}' before inject_marker and replace it with '},'
        
        # A simpler way: we know t3 ends with `  },\n` or similar in the previous script.
        # Let's just insert rich_content before `};\n\nlet userXP`
        new_content = content[:inject_idx] + ",\n" + rich_content + content[inject_idx:]
        with open(html_path, "w") as f:
            f.write(new_content)
        print("Successfully generated T4-T6 rich content!")
    else:
        print("Could not find injection point.")
