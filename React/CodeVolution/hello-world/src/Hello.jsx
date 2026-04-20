import React from "react";

export const Hello = () =>{

    return(
        <div id="container">
            <h1>Hello Fucker</h1>
        </div>
    );
};


export const HellWithoutJSX = () => {

    // return React.createElement("div", {id: "container"}, "Hello Fucker");


    //return React.createElement("div", {id: "container"}, "<h1>Hello Fucker</h1>");
    //return React.createElement("div", {id: "container"}, "<h1>Hello Fucker</h1>");
    return React.createElement("div", {id: "container"}, 
        React.createElement("h1", null, "Fuck You")
    );
};