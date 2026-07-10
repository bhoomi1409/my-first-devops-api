import re

html_path = "/Users/bhoomim/devops CI:CD/handbook/fullstack_ai_handbook.html"
with open(html_path, "r") as f:
    content = f.read()

rich_content = r"""
  t116: {
    tag:'Phase 3 · Frontend', num:116,
    title:'Custom Hooks',
    desc:'Extracting component logic into reusable functions.',
    theory:`<div class="card"><h3>🎣 Sharing the Magic</h3><p>If you write complex logic to fetch user data in the <code>Profile</code> component, what happens if the <code>Dashboard</code> component also needs to fetch user data? You don't want to copy/paste the <code>useState</code> and <code>useEffect</code> blocks.</p><h4>Creating a Custom Hook</h4><p>A Custom Hook is just a standard JavaScript function whose name starts with <strong>"use"</strong> (e.g., <code>useFetch</code>). It can call other hooks inside it. You extract the logic out of your component into this function, and then just call <code>const data = useFetch('/api/users')</code> from any component!</p></div>`,
    mcqs:[
      {q:"What is the primary purpose of writing a Custom Hook in React?",opts:["A. To make the app look better","B. To extract and reuse complex stateful logic (useState/useEffect) across multiple different components without duplicating code","C. To connect to a database","D. To replace Redux"],ans:1,exp:"Custom hooks are the ultimate way to keep your React components clean and focused purely on UI."},
      {q:"What is the mandatory naming convention for a Custom Hook?",opts:["A. It must end with 'Hook'","B. It must start with the word 'use' (e.g., useWindowSize, useFetch)","C. It must be capitalized","D. There is no rule"],ans:1,exp:"If you don't start it with 'use', React's linter won't check it for Hook constraint violations (like ensuring it's not called inside an if-statement)."},
      {q:"Can a Custom Hook call other React hooks (like useState or useEffect) inside of it?",opts:["A. Yes, absolutely. That is the entire point.","B. No, only components can call hooks","C. Only in class components","D. Only if you pass a special prop"],ans:0,exp:"A custom hook is essentially a wrapper around standard React hooks."},
      {q:"If Component A and Component B both call the same 'useCounter' custom hook, do they share the same state?",opts:["A. Yes, changing the counter in A changes it in B","B. No, custom hooks are a mechanism to reuse stateful LOGIC, not state itself. Each call gets completely independent state.","C. It throws an error","D. They overwrite each other"],ans:1,exp:"This is a critical distinction. If you want to share the actual data/state, you need Context API or Redux, not a custom hook."},
      {q:"What does a Custom Hook typically return?",opts:["A. Always JSX","B. Whatever you want! Usually an array or an object containing the state variables and functions needed by the component.","C. A Promise","D. Nothing"],ans:1,exp:"e.g., return { data, loading, error };"}
    ],
    flows:[
      {title:"Custom Hook Flow",items:["start:Component A calls useFetch('/users')","proc:useFetch manages 'loading' and 'data' state","dec:useFetch returns data to Component A","proc:Component B calls useFetch('/posts')","end:Gets completely independent state. Code reused!"]}
    ],
    game:{icon:"🎣",title:"The Angler",desc:"Master custom hooks",badges:["🎣 Logic Extractor","📦 Hook Reuser","📏 useNamer"],challenges:[{icon:"📝",title:"Shared State",desc:"Do components share state via hooks?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"useToggle Hook",badge:"Abstractor",desc:"Create a reusable hook for toggling booleans.",tags:["React","Hooks"],steps:[{title:"Function",desc:"function useToggle(initial = false)"},{"title:"Logic",desc:"const [on, setOn] = useState(initial); const toggle = () => setOn(!on);"},{"title:"Return",desc:"return [on, toggle]"}],code:`// 1. Define the Custom Hook\nfunction useToggle(initialValue = false) {\n  const [value, setValue] = useState(initialValue);\n  const toggle = () => setValue(prev => !prev);\n  \n  // Return the state and the updater function\n  return [value, toggle];\n}\n\n// 2. Use it cleanly in any component!\nexport default function App() {\n  const [isModalOpen, toggleModal] = useToggle(false);\n  const [isDarkMode, toggleDarkMode] = useToggle(true);\n  \n  return <button onClick={toggleModal}>Open Modal</button>;\n}`}
  },
  t117: {
    tag:'Phase 3 · Frontend', num:117,
    title:'React Router',
    desc:'Navigating between different views in a Single Page Application without reloading the browser.',
    theory:`<div class="card"><h3>🗺️ The Navigator</h3><p>Traditional websites download a brand new HTML file from the server every time you click a link (which is slow). React creates <strong>Single Page Applications (SPAs)</strong>. You load one HTML file, and React just dynamically swaps the components in and out.</p><h4>React Router DOM</h4><p>To give users the <em>illusion</em> of multiple pages (and working URL paths like <code>/about</code>), we use a library called <strong>React Router</strong>. It listens to the URL in the address bar. If the URL is <code>/home</code>, it tells React to render the <code>&lt;Home /&gt;</code> component.</p></div>`,
    mcqs:[
      {q:"What is a Single Page Application (SPA)?",opts:["A. A website with only one paragraph","B. An app that loads a single HTML page and dynamically updates the DOM using Javascript as the user interacts, rather than loading new pages from the server.","C. An app without CSS","D. A mobile app"],ans:1,exp:"SPAs (like Facebook or Gmail) feel incredibly fast and app-like because the browser never flashes white or reloads."},
      {q:"What does React Router do in an SPA?",opts:["A. It connects to the database","B. It maps specific URL paths (like '/contact') to specific React Components, intercepting navigation so the browser doesn't actually refresh","C. It secures the application","D. It manages state"],ans:1,exp:"It gives the user the ability to bookmark pages and use the Back button, even though there's technically only one page."},
      {q:"In React Router, what component should you use INSTEAD of a standard HTML <a href='...'> anchor tag to navigate between pages?",opts:["A. <button>","B. <Link to='...'>","C. <nav>","D. <Route>"],ans:1,exp:"If you use a standard <a> tag, the browser will perform a hard refresh, completely destroying the React SPA experience."},
      {q:"How do you define a route that should render the 'Dashboard' component when the URL is '/dashboard'?",opts:["A. <Route path='/dashboard' element={<Dashboard />} />","B. <Link to='/dashboard' />","C. <App url='/dashboard' />","D. <Switch id='/dashboard' />"],ans:0,exp:"The Route component acts as an IF statement. If path matches URL, render the element."},
      {q:"How do you capture a dynamic ID from a URL, like '/users/55'?",opts:["A. By reading the database","B. By defining a route like path='/users/:id' and using the useParams() hook inside the component to extract '55'","C. You can't capture IDs","D. Using local storage"],ans:1,exp:"useParams is essential for dynamic routing (like viewing individual user profiles)."}
    ],
    flows:[
      {title:"SPA Navigation Flow",items:["start:User clicks <Link to='/about'>","proc:React Router intercepts click","proc:Prevents default browser refresh","dec:Updates URL bar to '/about'","end:Unmounts <Home/>, Mounts <About/> component"]}
    ],
    game:{icon:"🗺️",title:"The Navigator",desc:"Master SPA routing",badges:["🗺️ Route Mapper","🔗 Linker","🆔 Param Extractor"],challenges:[{icon:"📝",title:"Anchor Tag",desc:"Why is <a href> bad in React?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Basic Routing",badge:"Tour Guide",desc:"Set up a multi-page React app.",tags:["React","Routing"],steps:[{title:"Wrap",desc:"Wrap App in <BrowserRouter>"},{"title:"Routes",desc:"Create <Routes> container"},{"title:"Route",desc:"Add <Route path='/' element={<Home/>} />"}],code:`import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';\n\nexport default function App() {\n  return (\n    <BrowserRouter>\n      <nav>\n        {/* Use Link, NOT <a>! */}\n        <Link to="/">Home</Link>\n        <Link to="/about">About</Link>\n      </nav>\n      \n      <Routes>\n        {/* If URL matches path, render the element */}\n        <Route path="/" element={<Home />} />\n        <Route path="/about" element={<About />} />\n      </Routes>\n    </BrowserRouter>\n  );\n}`}
  },
  t118: {
    tag:'Phase 3 · Frontend', num:118,
    title:'Context API',
    desc:'Solving the Prop Drilling problem by providing global state to the component tree.',
    theory:`<div class="card"><h3>📡 The Global Broadcast</h3><p>Imagine the user logs in. The <code>App</code> component holds the <code>user</code> state. But the <code>NavbarAvatar</code> component is nested 5 levels deep. Passing the <code>user</code> prop down through 4 intermediate components that don't even need it is called <strong>Prop Drilling</strong>, and it makes code terrible.</p><h4>React Context</h4><p>The Context API allows you to broadcast data globally. You wrap your app in a <code>&lt;UserContext.Provider&gt;</code>. Then, ANY component, no matter how deep, can simply call <code>useContext(UserContext)</code> to instantly grab the data, bypassing the middleman completely.</p></div>`,
    mcqs:[
      {q:"What specific problem does the React Context API solve?",opts:["A. Slow CSS animations","B. Prop Drilling (passing props through multiple levels of components that don't need them just to reach a nested child)","C. Database connections","D. Routing errors"],ans:1,exp:"Context allows you to 'teleport' data directly to the component that needs it."},
      {q:"What is the first step to using Context?",opts:["A. Installing Redux","B. Creating the Context object using React.createContext()","C. Using the useContext hook","D. Writing an API endpoint"],ans:1,exp:"You have to create the Context object first, then export it so other files can use it."},
      {q:"How do you make the Context data available to your component tree?",opts:["A. By using local storage","B. By wrapping your component tree inside a <MyContext.Provider value={data}> tag","C. By passing it as a standard prop","D. By using a custom hook"],ans:1,exp:"Any component inside the Provider (no matter how deep) can access the 'value' prop."},
      {q:"Inside a deeply nested child component, what hook do you use to retrieve the Context data?",opts:["A. useState()","B. useContext(MyContext)","C. useEffect()","D. useGlobal()"],ans:1,exp:"useContext grabs the value from the nearest Provider above it in the tree."},
      {q:"Should you use Context for ALL of your application's state?",opts:["A. Yes, never use useState again","B. No, Context should only be used for truly global data (like User Auth, UI Themes, or Language preference). Overusing it causes unnecessary re-renders of the entire app.","C. Only in small apps","D. Yes, it's faster"],ans:1,exp:"Keep local state (like a text input value) in local useState."}
    ],
    flows:[
      {title:"The Context Teleporter",items:["start:<App> creates ThemeContext='dark'","proc:<Provider value='dark'> wraps everything","dec:<Layout> ignores it (No prop drilling)","dec:<Sidebar> ignores it","end:<Button> calls useContext -> Gets 'dark' instantly!"]}
    ],
    game:{icon:"📡",title:"The Broadcaster",desc:"Master global state",badges:["📡 Teleporter","🕳️ Drill Stopper","🎁 Provider"],challenges:[{icon:"📝",title:"Overuse",desc:"Why not put everything in Context?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Theme Context",badge:"Contextual",desc:"Create and consume a global theme context.",tags:["React","Context"],steps:[{title:"Create",desc:"export const ThemeCtx = createContext()"},{"title:"Provide",desc:"<ThemeCtx.Provider value='dark'> <App/> </ThemeCtx.Provider>"},{"title:"Consume",desc:"const theme = useContext(ThemeCtx);"}],code:`import { createContext, useContext } from 'react';\n\n// 1. Create it\nconst ThemeContext = createContext("light");\n\nexport default function App() {\n  return (\n    // 2. Provide it\n    <ThemeContext.Provider value="dark">\n      <DeepNestedComponent />\n    </ThemeContext.Provider>\n  );\n}\n\nfunction DeepNestedComponent() {\n  // 3. Consume it (No props required!)\n  const theme = useContext(ThemeContext);\n  return <div className={theme}>I am dark mode!</div>;\n}`}
  },
  t119: {
    tag:'Phase 3 · Frontend', num:119,
    title:'State Management (Redux/Zustand)',
    desc:'Advanced architectural patterns for managing massive amounts of global state.',
    theory:`<div class="card"><h3>🏛️ The Global Store</h3><p>Context API is great for small things (themes, auth). But if you are building Facebook, where hundreds of components interact with complex, rapidly changing data (chats, notifications, feeds), Context will cause massive performance issues. You need a dedicated <strong>State Management Library</strong>.</p><h4>Redux vs Zustand</h4><ul><li><strong>Redux:</strong> The industry standard. Very powerful, but requires massive amounts of "boilerplate" code (Actions, Reducers, Dispatchers, Store).</li><li><strong>Zustand:</strong> The modern favorite. It provides a global Store, but is incredibly lightweight and easy to use compared to Redux.</li></ul></div>`,
    mcqs:[
      {q:"Why might you choose a State Management library (like Redux or Zustand) over the built-in React Context API?",opts:["A. Context API is deprecated","B. Context causes massive re-renders when data changes. Libraries like Zustand/Redux allow components to subscribe to specific slices of state, preventing unnecessary re-renders in complex apps.","C. They are built into HTML5","D. They use less RAM"],ans:1,exp:"In Context, if a User's avatar changes, the entire App might re-render. In Redux, ONLY the Avatar component re-renders."},
      {q:"In Redux architecture, what is the 'Store'?",opts:["A. Where you buy plugins","B. The single, centralized Javascript object that holds the entire global state of the application","C. A database table","D. A routing configuration"],ans:1,exp:"The 'Single Source of Truth'."},
      {q:"In Redux, how do you change the state inside the Store?",opts:["A. You modify it directly (store.count = 5)","B. You CANNOT modify it directly. You must 'Dispatch' an 'Action' (an object describing what happened). A 'Reducer' function then reads the action and generates a brand new state object.","C. You use useState","D. You restart the app"],ans:1,exp:"This strict one-way data flow makes bugs incredibly easy to trace (Time-Travel Debugging)."},
      {q:"What is a major complaint developers have about Redux?",opts:["A. It is too fast","B. It requires a massive amount of 'boilerplate' code (setup) just to do simple things","C. It is written in Python","D. It only works on Mac"],ans:1,exp:"This is why Redux Toolkit (RTK) and alternatives like Zustand were created."},
      {q:"Why is Zustand becoming so popular as a Redux alternative?",opts:["A. It creates databases","B. It provides the performance benefits of a global store without the massive boilerplate of Redux; you just define a hook and use it","C. It is owned by Google","D. It replaces React"],ans:1,exp:"Zustand is German for 'State'."}
    ],
    flows:[
      {title:"Redux Unidirectional Flow",items:["start:UI Button Clicked","proc:Dispatches ACTION {type: 'ADD_TODO', payload: 'Buy Milk'}","dec:REDUCER takes Old State + Action","proc:Reducer returns NEW State Object","end:STORE updates. UI Subscriptions trigger re-render."]}
    ],
    game:{icon:"🏛️",title:"The State Manager",desc:"Master global architectures",badges:["🏛️ Store Keeper","🚀 Dispatcher","📉 Reducer"],challenges:[{icon:"📝",title:"Boilerplate",desc:"Why is Zustand trending over Redux?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"Zustand Store",badge:"Modernizer",desc:"Create a global store using Zustand.",tags:["React","State"],steps:[{title:"Import",desc:"import { create } from 'zustand'"},{"title:"Store",desc:"const useStore = create(set => ({ bears: 0, add: () => set... }))"},{"title:"Use",desc:"const bears = useStore(state => state.bears)"}],code:`import { create } from 'zustand';\n\n// 1. Create a global hook (The Store)\nconst useBearStore = create((set) => ({\n  bears: 0,\n  // Action to update state\n  increasePopulation: () => set((state) => ({ bears: state.bears + 1 })),\n  removeAllBears: () => set({ bears: 0 }),\n}));\n\n// 2. Any component can use it instantly! No Providers needed!\nfunction BearCounter() {\n  const bears = useBearStore((state) => state.bears);\n  return <h1>{bears} around here ...</h1>;\n}`}
  },
  t120: {
    tag:'Phase 3 · Frontend', num:120,
    title:'Next.js (SSR vs SSG)',
    desc:'The React framework for production, bringing server-side rendering to single-page applications.',
    theory:`<div class="card"><h3>🚀 The React Framework</h3><p>Standard React SPAs have a major flaw: <strong>SEO (Search Engine Optimization)</strong>. When a Google Bot requests a React site, it receives a blank HTML file and a massive JS file. Google bots hate executing Javascript.</p><h4>Next.js to the rescue</h4><p>Next.js is a framework built ON TOP of React that renders the components on the <strong>Server</strong> before sending them to the browser.</p><ul><li><strong>SSR (Server-Side Rendering):</strong> The server generates fresh HTML for every single request. Great for dynamic data (like a user dashboard).</li><li><strong>SSG (Static Site Generation):</strong> The server generates the HTML once during build time. Incredible performance for static data (like a Blog or Documentation).</li></ul></div>`,
    mcqs:[
      {q:"What major problem with standard React does Next.js solve?",opts:["A. It makes writing CSS easier","B. It solves SEO and initial page load speed issues by pre-rendering the React components into static HTML on the server, rather than forcing the client's browser to build the HTML via Javascript.","C. It connects to SQL","D. It removes the Virtual DOM"],ans:1,exp:"If you right-click -> View Source on a standard React app, the body is empty. On Next.js, you see full HTML content."},
      {q:"What is Server-Side Rendering (SSR)?",opts:["A. Generating the HTML on the user's phone","B. Every time a user requests a URL, the Server executes the React code, fetches the database data, builds the HTML, and sends the finished page to the user","C. Creating a database","D. Compiling CSS"],ans:1,exp:"SSR guarantees you always have the most up-to-date data, but it requires server processing power for every request."},
      {q:"What is Static Site Generation (SSG)?",opts:["A. Writing HTML by hand","B. The Server executes the React code and builds the HTML exactly ONCE during the 'build' phase before deployment. That finished HTML is then served to millions of users instantly via CDNs.","C. Generating CSS","D. Using WordPress"],ans:1,exp:"SSG is incredibly fast and cheap to host. Perfect for blogs, marketing pages, and documentation."},
      {q:"In Next.js (App Router), what defines a route/page?",opts:["A. React Router DOM","B. The File System. If you create a file at 'app/about/page.js', Next.js automatically creates the '/about' route.","C. An XML file","D. The Database"],ans:1,exp:"File-based routing removes the need for complex routing configuration files."},
      {q:"Is Next.js only for the frontend?",opts:["A. Yes, it's just React","B. No, Next.js is a Full-Stack framework. You can write backend API routes and connect directly to databases within the same Next.js project.","C. Only on Windows","D. Yes, it replaces HTML"],ans:1,exp:"You don't necessarily need a separate Spring Boot or Node.js server if you use Next.js Route Handlers."}
    ],
    flows:[
      {title:"Standard React vs SSR",items:["start:React: Client asks Server -> Gets Blank HTML -> Downloads JS -> Builds UI (Slow)","dec:Next.js (SSR): Client asks Server","proc:Server fetches DB -> Server builds React UI","end:Server sends finished HTML -> Client sees UI instantly!"]}
    ],
    game:{icon:"🚀",title:"The Frameworker",desc:"Master Next.js",badges:["🚀 SSR Engine","📄 Static Generator","📁 File Router"],challenges:[{icon:"📝",title:"The SEO Problem",desc:"Why is standard React bad for SEO?",xp:50},{icon:"⚡",title:"MCQ Master",desc:"Score 5/5 on MCQs",xp:100}]},
    project:{title:"File-Based Routing",badge:"Directory Master",desc:"Understand Next.js folder routing.",tags:["Next.js","Routing"],steps:[{title:"Folder",desc:"Create folder: app/dashboard"},{"title:"File",desc:"Create file: app/dashboard/page.js"},{"title:"Result",desc:"URL /dashboard now works automatically!"}],code:`// app/dashboard/page.js\n\n// By simply placing this file in this folder structure,\n// Next.js automatically creates a server-rendered route at "/dashboard".\n// No React-Router setup required!\n\nexport default function Dashboard() {\n  return <h1>Welcome to the Next.js Dashboard!</h1>;\n}`}
  }
"""

start_marker = "};\n\nlet userXP"
inject_idx = content.find(start_marker)

if inject_idx != -1:
    new_content = content[:inject_idx] + ",\n" + rich_content + content[inject_idx:]
    with open(html_path, "w") as f:
        f.write(new_content)
    print("Successfully generated T116-T120 rich content!")
else:
    print("Could not find injection point.")
