import re

html_path = "/Users/bhoomim/devops CI:CD/handbook/fullstack_ai_handbook.html"
with open(html_path, "r") as f:
    content = f.read()

rich_content = r"""
  t111: {
    tag:'Phase 3 · Frontend', num:111,
    title:'React Fundamentals & JSX',
    desc:'The most popular JavaScript library for building user interfaces.',
    theory:`<div class="card"><h3>⚛️ The UI Library</h3><p>Historically, developers kept HTML in one file and JS in another. <strong>React</strong> changed the game by introducing <strong>JSX</strong> (JavaScript XML). JSX allows you to write HTML <em>directly inside</em> your JavaScript code!</p><h4>Why React?</h4><ul><li><strong>Declarative:</strong> You describe what the UI <em>should</em> look like for a given state, and React figures out how to update the DOM efficiently.</li><li><strong>Component-Based:</strong> You build encapsulated, reusable buttons, forms, and cards, then compose them together to make complex UIs.</li></ul><div class="cb"><span class="cm">// This is JSX! It looks like HTML, but it's pure JS.</span>
<span class="ck">const</span> title = &lt;<span class="cv">h1</span> <span class="cv">className</span>=<span class="cs">"header"</span>&gt;Hello React!&lt;/<span class="cv">h1</span>&gt;;</div></div>`,
    mcqs:[
      {q:"What is JSX in React?",opts:["A. A new programming language","B. A syntax extension for JavaScript that looks identical to HTML, allowing you to write UI components directly inside JS files","C. A database query language","D. A CSS framework"],ans:1,exp:"JSX is compiled down to standard React.createElement() javascript calls under the hood by Babel."},
      {q:"Why do you use 'className' in JSX instead of 'class'?",opts:["A. Because it sounds better","B. Because 'class' is a reserved keyword in JavaScript (used for OOP classes). JSX is just JavaScript, so it must use 'className' to map to the HTML class attribute.","C. It's a bug in React","D. To confuse beginners"],ans:1,exp:"This is one of the few strict differences between standard HTML and JSX."},
      {q:"How do you inject a dynamic JavaScript variable into JSX HTML?",opts:["A. Use the $ symbol","B. Wrap the variable in curly braces { }","C. Use standard string concatenation (+)","D. Wrap it in quotes"],ans:1,exp:"E.g., <h1>Hello {userName}!</h1>"},
      {q:"Is React a Framework or a Library?",opts:["A. A complete Framework (like Angular)","B. A Library focused strictly on rendering User Interfaces. You have to add your own routing and state management libraries.","C. An Operating System","D. A Database"],ans:1,exp:"React is highly unopinionated. You build your own tech stack around it."},
      {q:"What must every React component return?",opts:["A. A string","B. Exactly one single root JSX element (or a Fragment <>)","C. An Array","D. A Database connection"],ans:1,exp:"You cannot return two sibling <div> tags. You must wrap them in a single parent <div> or a <> (Fragment)."}
    ],
    flows:[
      {title:"The JSX Compilation Flow",items:["start:Developer writes: <div className='x'>Hi</div>","proc:Babel Compiler intercepts it","dec:Translates to: React.createElement('div', {className:'x'}, 'Hi')","end:Browser executes the pure JS!"]}
    ],
    game:{icon:"⚛️",title:"The React Dev",desc:"Master JSX",badges:["⚛️ Component Maker","🧬 JSX Weaver","📦 Fragment User"],challenges:[{icon:"📝",title:"Reserved Words",desc:"Why use className instead of class?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"First Component",badge:"UI Builder",desc:"Write a basic React component returning JSX.",tags:["React","Frontend"],steps:[{title:"Function",desc:"function Welcome() { ... }"},{"title:"JSX",desc:"return <h1>Hello World</h1>;"},{"title:"Export",desc:"export default Welcome;"}],code:`// A standard React Functional Component\nexport default function UserCard() {\n  // Pure JavaScript logic here\n  const name = "Bhoomi";\n  const age = 25;\n\n  // Returns JSX (HTML inside JS!)\n  // Notice className and the {} for variables.\n  return (\n    <div className="card">\n      <h2>{name}</h2>\n      <p>Age: {age}</p>\n    </div>\n  );\n}`}
  },
  t112: {
    tag:'Phase 3 · Frontend', num:112,
    title:'Virtual DOM',
    desc:'The secret behind Reacts blazing fast rendering performance.',
    theory:`<div class="card"><h3>👻 The Ghost DOM</h3><p>Manipulating the real browser DOM (using <code>document.createElement</code>) is very slow and computationally expensive. If a list of 1000 items changes by 1 item, completely redrawing the real DOM is a terrible user experience.</p><h4>The React Solution</h4><p>React keeps a lightweight, Javascript copy of the DOM in memory called the <strong>Virtual DOM</strong>. When data changes, React:</p><ol><li>Creates a <em>new</em> Virtual DOM with the updates.</li><li>Compares the New Virtual DOM with the Old Virtual DOM (<strong>Diffing Algorithm / Reconciliation</strong>).</li><li>Figures out that ONLY the text of the 3rd <code>&lt;li&gt;</code> changed.</li><li>Updates ONLY that exact spot in the <em>Real DOM</em>, leaving the other 999 items untouched!</li></ol></div>`,
    mcqs:[
      {q:"What is the Virtual DOM?",opts:["A. A 3D interface","B. A lightweight Javascript representation (a copy) of the actual browser DOM kept in memory by React","C. A new HTML5 tag","D. A database cache"],ans:1,exp:"Updating Javascript objects in memory is incredibly fast. Updating the real UI is very slow."},
      {q:"What is 'Reconciliation' (Diffing) in React?",opts:["A. Reconnecting to the internet","B. The algorithm React uses to compare the updated Virtual DOM with the previous Virtual DOM to calculate the absolute minimum number of changes needed for the real DOM","C. Sorting a database","D. Deleting old code"],ans:1,exp:"This diffing process is why React is so performant."},
      {q:"If you have a list of 100 items, and you change the color of item #50, what does React do?",opts:["A. Deletes and redraws all 100 items in the Real DOM","B. Uses the Virtual DOM to detect exactly what changed, and applies a surgical CSS update ONLY to item #50 in the Real DOM","C. Refreshes the webpage","D. Crashes"],ans:1,exp:"Minimizing Real DOM updates is the core philosophy of React."},
      {q:"Why does React require you to pass a unique 'key' prop when mapping over an array to render a list (e.g., <li key={item.id}>)?",opts:["A. For security","B. Because the Diffing algorithm uses those unique keys to quickly identify exactly which items were added, removed, or reordered, avoiding complete list re-renders","C. To style the list","D. To encrypt the list"],ans:1,exp:"Never use the array 'index' as a key if the list can be reordered or deleted, as it completely breaks the diffing algorithm."},
      {q:"Does the user ever directly see the Virtual DOM?",opts:["A. Yes, in the browser console","B. No, it is purely an invisible, behind-the-scenes mathematical model React uses for calculations","C. Yes, on mobile","D. Yes, if they view source"],ans:1,exp:"The Virtual DOM is entirely abstract."}
    ],
    flows:[
      {title:"Virtual DOM Flow",items:["start:State Changes! (Score: 1 -> 2)","proc:React builds NEW Virtual DOM tree","proc:React runs Diffing Algorithm against OLD tree","dec:Notices ONLY the <span> text changed","end:React surgically updates Real DOM <span> to '2'"]}
    ],
    game:{icon:"👻",title:"The Diff Engine",desc:"Master React rendering",badges:["👻 Virtualizer","⚖️ Diff Calculator","🔑 Key Provider"],challenges:[{icon:"📝",title:"Keys",desc:"Why never use array index as a key?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"The Key Warning",badge:"List Maker",desc:"Render a list correctly in React.",tags:["React","Lists"],steps:[{title:"Data",desc:"const users = [{id: 1, name: 'A'}]"},{"title:"Map",desc:"users.map(user => ...)"},{"title:"Key",desc:"<div key={user.id}>{user.name}</div>"}],code:`export default function UserList() {\n  const users = [\n    { id: "x1", name: "Alice" },\n    { id: "y2", name: "Bob" }\n  ];\n\n  return (\n    <ul>\n      {users.map((user) => (\n        // The 'key' is CRITICAL for the Virtual DOM!\n        // Without it, if Bob is deleted, React might accidentally\n        // re-render the entire list instead of just removing Bob.\n        <li key={user.id}>{user.name}</li>\n      ))}\n    </ul>\n  );\n}`}
  },
  t113: {
    tag:'Phase 3 · Frontend', num:113,
    title:'Components & Props',
    desc:'The building blocks of React and how data flows between them.',
    theory:`<div class="card"><h3>🧱 Lego Blocks</h3><p>A React <strong>Component</strong> is just a JavaScript function that returns JSX. You build small pieces (like a <code>&lt;Button /&gt;</code>), and combine them to build big pieces (like a <code>&lt;Navbar /&gt;</code>).</p><h4>Props (Properties)</h4><p>Components need data. You pass data from a Parent component down to a Child component using <strong>Props</strong>. Props look exactly like HTML attributes.</p><p><strong>CRITICAL RULE:</strong> Props are <em>Read-Only</em>. A child component is strictly forbidden from modifying the props it receives from its parent. Data flows strictly ONE WAY (Top-Down).</p></div>`,
    mcqs:[
      {q:"What is a React Component conceptually?",opts:["A. A database table","B. An independent, reusable piece of UI, typically written as a JavaScript function that returns JSX","C. A CSS file","D. An image asset"],ans:1,exp:"Components are the fundamental building blocks of React applications."},
      {q:"What are 'Props' in React?",opts:["A. CSS animations","B. Arguments (data) passed from a Parent component down to a Child component, similar to how arguments are passed to a function","C. HTML tags","D. State variables"],ans:1,exp:"<UserProfile name='Bhoomi' /> - 'name' is a prop."},
      {q:"Can a Child component modify the Props it receives from its Parent? (e.g., props.name = 'New Name')",opts:["A. Yes, anytime","B. No, Props are strictly Read-Only (Immutable). A component must never modify its own props.","C. Only if the prop is a number","D. Yes, if you use a special keyword"],ans:1,exp:"If a child needs to change data, it must ask the Parent to change the Parent's state."},
      {q:"What is 'Prop Drilling'?",opts:["A. Drilling a hole in the UI","B. The annoying process of passing a prop through 5 layers of intermediate child components just to get it to the 6th nested component that actually needs it","C. Animating props","D. Deleting props"],ans:1,exp:"Prop drilling is a common problem in React that is solved by using Context API or Redux."},
      {q:"How do you access a prop inside a functional component?",opts:["A. Using the 'this' keyword","B. By passing 'props' as the first parameter of the function, and accessing it via props.propertyName (or by destructuring it)","C. Using document.getProp()","D. Using global variables"],ans:1,exp:"Destructuring is the modern standard: function UserCard({ name, age }) { ... }"}
    ],
    flows:[
      {title:"Top-Down Data Flow",items:["start:<App /> (Holds user='Bhoomi')","proc:Passes prop to <Navbar user={user} />","proc:<Navbar /> passes prop to <ProfileAvatar name={user} />","dec:<ProfileAvatar /> renders 'Bhoomi'","end:Data strictly flows downward!"]}
    ],
    game:{icon:"🧱",title:"The Builder",desc:"Master components",badges:["🧱 Lego Master","📦 Prop Passer","⬇️ Top-Down Thinker"],challenges:[{icon:"📝",title:"Read-Only",desc:"Why are props immutable?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Passing Props",badge:"Prop Master",desc:"Pass data from Parent to Child.",tags:["React","Props"],steps:[{title:"Parent",desc:"<Button color='red' text='Click' />"},{"title:"Child",desc:"function Button({ color, text })"},{"title:"Render",desc:"<button style={{background: color}}>{text}</button>"}],code:`// CHILD COMPONENT (Reusable)\n// We immediately Destructure the props for clean code\nfunction CustomButton({ color, label }) {\n  return (\n    <button style={{ backgroundColor: color }}>\n      {label}\n    </button>\n  );\n}\n\n// PARENT COMPONENT\nexport default function App() {\n  return (\n    <div>\n      {/* Reusing the component by passing different PROPS! */}\n      <CustomButton color="blue" label="Submit" />\n      <CustomButton color="red" label="Delete" />\n    </div>\n  );\n}`}
  },
  t114: {
    tag:'Phase 3 · Frontend', num:114,
    title:'State (useState)',
    desc:'Adding memory and interactivity to React components.',
    theory:`<div class="card"><h3>🧠 Component Memory</h3><p>Props are read-only data passed from above. But what if a component needs to change its <em>own</em> data? (e.g., A counter button that goes from 0 to 1 when clicked). That is called <strong>State</strong>.</p><h4>The useState Hook</h4><p>In modern React, we use the <code>useState</code> hook. It gives you two things:</p><ol><li>A variable containing the current state value (e.g., <code>count</code>).</li><li>A setter function to update that value (e.g., <code>setCount</code>).</li></ol><div class="box b-ro"><h5>⚠️ The React Rule of Re-rendering</h5><p>You MUST use the setter function to change state (Never do <code>count = 1</code>). When you call <code>setCount(1)</code>, React automatically triggers a <strong>Re-render</strong> of the component, updating the UI to reflect the new state!</p></div></div>`,
    mcqs:[
      {q:"What is the difference between Props and State?",opts:["A. They are identical","B. Props are read-only data passed down from a parent. State is internal, mutable memory managed completely by the component itself.","C. State is for CSS, Props are for HTML","D. Props can change, State cannot"],ans:1,exp:"Props = External config. State = Internal memory."},
      {q:"What does the useState() hook return?",opts:["A. A boolean","B. An array with exactly two elements: the current state value, and a function to update that state.","C. An object","D. A string"],ans:1,exp:"We usually destructure this immediately: const [count, setCount] = useState(0);"},
      {q:"What happens automatically when you call a state setter function (like setCount(5))?",opts:["A. The database updates","B. React schedules a Re-render of that component (and its children), updating the Real DOM to reflect the new state","C. The page hard-refreshes","D. An error is thrown"],ans:1,exp:"This is the magic of React. Data changes -> UI updates automatically."},
      {q:"Why is it a critical error to directly mutate state (e.g., count = 5) instead of using the setter function (setCount(5))?",opts:["A. It creates a memory leak","B. Because React will not know the state changed, and therefore will NOT trigger a re-render to update the UI","C. It deletes the variable","D. It causes an infinite loop"],ans:1,exp:"React relies on the setter function to trigger the reconciliation process."},
      {q:"If your new state depends on your previous state (like incrementing a counter), what is the safest way to update it?",opts:["A. setCount(count + 1)","B. Passing an updater callback function: setCount(prevCount => prevCount + 1)","C. count++","D. setCount(prev)"],ans:1,exp:"Using the callback guarantees you have the absolute most recent state, preventing race condition bugs if the user clicks very fast."}
    ],
    flows:[
      {title:"State Re-render Cycle",items:["start:Component mounts (count: 0)","proc:User clicks 'Add' Button","proc:onClick calls setCount(1)","dec:React triggers a Re-render","end:Component runs again, JSX outputs '1'"]}
    ],
    game:{icon:"🧠",title:"The Memorizer",desc:"Master component state",badges:["🧠 State Keeper","🔄 Re-renderer","🛑 Direct Mutator (Avoid)"],challenges:[{icon:"📝",title:"Updater Func",desc:"Write a prev state update",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Interactive Counter",badge:"Clicker",desc:"Build a stateful counter.",tags:["React","State"],steps:[{title:"Import",desc:"import { useState } from 'react'"},{"title:"Init Hook",desc:"const [score, setScore] = useState(0)"},{"title:"Event",desc:"onClick={() => setScore(score + 1)}"}],code:`import { useState } from 'react';\n\nexport default function Counter() {\n  // State variable (score) and its setter (setScore). Initial value is 0.\n  const [score, setScore] = useState(0);\n\n  return (\n    <div className="card">\n      <h2>Score: {score}</h2>\n      {/* Calling setScore triggers a UI update! */}\n      <button onClick={() => setScore(score + 1)}>\n        Add Point\n      </button>\n    </div>\n  );\n}`}
  },
  t115: {
    tag:'Phase 3 · Frontend', num:115,
    title:'Component Lifecycle & useEffect',
    desc:'Executing code at specific moments during a component\'s existence.',
    theory:`<div class="card"><h3>⏳ The Circle of Life</h3><p>Every React Component goes through three phases of life:</p><ol><li><strong>Mounting:</strong> It is born and inserted into the DOM.</li><li><strong>Updating:</strong> Its state or props change, causing a re-render.</li><li><strong>Unmounting:</strong> It dies and is removed from the DOM.</li></ol><h4>The useEffect Hook</h4><p>We use <code>useEffect</code> to perform "Side Effects" (fetching data, setting timers, subscribing to websockets) during these lifecycle phases. <br>The most critical part of useEffect is the <strong>Dependency Array</strong> <code>[]</code>, which controls exactly <em>when</em> the effect runs.</p></div>`,
    mcqs:[
      {q:"What is a 'Side Effect' in a React component?",opts:["A. A CSS animation","B. Operations that reach outside the functional component, like fetching data from an API, setting a timer, or manually changing the DOM","C. Changing local state","D. Passing props"],ans:1,exp:"React components should be 'pure' functions. Side effects belong inside useEffect."},
      {q:"If you use useEffect WITHOUT a dependency array at all (e.g., useEffect(() => {...})), when does it run?",opts:["A. Only once on mount","B. It runs after EVERY single render of the component (which can cause massive performance issues or infinite loops)","C. Never","D. Only on unmount"],ans:1,exp:"You almost never want to do this."},
      {q:"If you use useEffect WITH an EMPTY dependency array (e.g., useEffect(() => {...}, [])), when does it run?",opts:["A. After every render","B. Exactly ONCE, immediately after the component mounts to the screen (Perfect for initial API fetches)","C. Before rendering","D. When it unmounts"],ans:1,exp:"The empty array means 'this effect depends on nothing, so it never needs to re-run'."},
      {q:"If you provide variables in the dependency array (e.g., useEffect(() => {...}, [userId])), when does it run?",opts:["A. Only once","B. On mount, AND whenever the value of 'userId' changes between renders","C. Every 5 seconds","D. When 'userId' is deleted"],ans:1,exp:"This is incredibly powerful. If the user clicks a different profile, 'userId' changes, and the effect automatically re-fetches the new data!"},
      {q:"How do you execute 'Cleanup' code (Unmounting) in a useEffect (like clearing a timer to prevent memory leaks)?",opts:["A. Write a second useEffect","B. Return a function from inside the useEffect. React will run this returned function right before the component unmounts.","C. Use the delete keyword","D. Use clearEffect()"],ans:1,exp:"e.g., return () => clearInterval(timer);"}
    ],
    flows:[
      {title:"useEffect Dependency Rules",items:["start:useEffect( () => { fetch() } )","dec:No Array? -> Runs on EVERY render","dec:Array []? -> Runs ONCE on mount","end:Array [id]? -> Runs on mount AND when 'id' changes"]}
    ],
    game:{icon:"⏳",title:"The Lifecycle",desc:"Master useEffect",badges:["⏳ Mounter","🧼 Cleanup Crew","🔗 Dependency Expert"],challenges:[{icon:"📝",title:"Infinite Loop",desc:"How does fetch without [] cause a loop?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"API Fetch on Mount",badge:"Data Fetcher",desc:"Fetch data perfectly on component load.",tags:["React","Hooks"],steps:[{title:"State",desc:"const [data, setData] = useState(null)"},{"title:"Effect",desc:"useEffect(() => { fetch()... }, [])"},{"title:"Dependency",desc:"Ensure array is empty [] so it only fetches once!"}],code:`import { useState, useEffect } from 'react';\n\nexport default function Profile() {\n  const [user, setUser] = useState(null);\n\n  useEffect(() => {\n    // This runs exactly ONCE when the component loads\n    fetch('https://api.github.com/users/octocat')\n      .then(res => res.json())\n      .then(data => setUser(data));\n      \n    // Optional Cleanup function (runs when component unmounts)\n    return () => console.log("Profile component died!");\n  }, []); // <--- EMPTY ARRAY IS CRITICAL HERE!\n\n  if (!user) return <div>Loading...</div>;\n  return <h1>{user.name}</h1>;\n}`}
  },
"""

start_marker = "};\n\nlet userXP"
inject_idx = content.find(start_marker)

if inject_idx != -1:
    new_content = content[:inject_idx] + ",\n" + rich_content + content[inject_idx:]
    with open(html_path, "w") as f:
        f.write(new_content)
    print("Successfully generated T111-T115 rich content!")
else:
    print("Could not find injection point.")
