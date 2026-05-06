import { useState } from "react";

export const SimpleCounter = () => {

    const [count, setCount] = useState(0);

    const CountFunc = () => {
        console.log("Count: ", count);
        setCount(count+1);
        console.log("Count: ", count);
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