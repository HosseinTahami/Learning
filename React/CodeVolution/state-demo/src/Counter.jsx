export const Counter = () => {
    let count = 0;

    const counterFunc = () => {
        counter++;
    }

    return <button onClick={counterFunc}>Count: {count}</button>

}