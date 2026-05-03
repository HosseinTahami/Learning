import { useState } from 'react';

export const Counter = () => {

    const [count, setCount] =  useState(0); // array destructuring
    // currenValue, setterFunction = useState(initialValue)

    // let count = 0;

    const counterFunc = () => {
        setCount(count + 1);
    };

    return <button onClick={counterFunc}>Count: {count}</button>

}