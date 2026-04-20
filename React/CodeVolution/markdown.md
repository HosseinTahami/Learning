
```zsh
npm create vite@latest
```

```zsh
npm run dev
```

## files & dirs

- package.json

    What tools and libraries is needed for the project ?

    - react
    - react-dom

```zsh
npm install 
react@latest react-dom@latest @types/react@latest @types/react-dom@latest
```

- index.html

    The only single html file we willl have, since we are making **single page applications**

    ```html
    <body>
        <div id="root"></div>
    </body>
    ```

    at run-time, REACT will take over of this div and becomes responsiple for everything inside of it.


- package-lock.json

    make sure everybody else have the same version of the dependencies as us.


- node/

    contains all the files related to our depnedencies.

- public/

    It is used for saving the static files, such as images.

- src/

    - main.jsx
        It will specifies the root componenet, which is the app component
        and the DOM element which will be controled by REACT and the DOM element is the element with the ID 'root'.

        ```
        createRoot(document.getElementByID('root')).render(
            <StrictMode>
                <App />
            </StrictMode>
        )
        ```
    
    - App.jsx
        It contains our main application componenets.


## What is a Component ?

- A componenet is a piece of the UI that has its own logic and appearance, it can be as small as a button or as large as an entire page

- A component is just a JavaScript function that returns some HTML describing what should appear on screen.

- Root (App) Component
    - Header
    - Aside
    - Main
    - Footer


## Nesting Components

```jsx
function FuckYou(){

  return <h2>Fuck You, Who Every the fuck you are.</h2>;

}

function Button(){

  return <button>Fuck</button>
}


function App() {

  return (

    <div>
      <h1>Fuck:</h1>
      <FuckYou />
      <Button />
      <br></br>
      <Button />
    </div>

  );
}
```

**NOTE**:

We can seperate the components, from the App.jsx and put  it in different files, so we can export and import them in the App.jsx, when we want to use it.


## JSX Rules

1- Every Component must return a single root element

    - Wrapped inside the functions

2- Every fucking single tag should be properly closed
    - Even the fucking ones that don't need closing tagis in HTML


3- Attribute names must be written in camelCase

    - JSX is extenstion of JS, HTML attributes will conflict with JS keywords and need different names

    - class is className, for is htmlFor, tabindex is tabIndex, ...

4- It is possible to embed JS expressions directly in the markup using curly braces.