import { useState } from "react";

export const SimpleCounter = () => {

    const [count, setCount] = useState(0);
    console.log("Render phase: Component rendering with count =", count);


    const CountFunc = () => {
        console.log("Before setCount, count is:  ", count);
        setCount(count+1);
        console.log("Still in trigger phase, After setCount + 1, count is: ", count);
        setCount(count+19);
        console.log("Still in trigger phase, After setCount + 19, count is: ", count);
        setCount(count+10);
        console.log("Still in trigger phase, After setCount + 10, count is: ", count);
        setCount(count+12);
        console.log("Still in trigger phase, After setCount + 12, count is: ", count);
    }

    return (
        <div>
            <h2>Count: {count}</h2>
            <button onClick={CountFunc}>
                <b>+</b>
            </button>
        </div>
    )
}