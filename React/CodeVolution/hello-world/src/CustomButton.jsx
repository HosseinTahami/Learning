export const CustomButton = ({text}) => {

    // const handleClick = () => {
    //     alert("Thanks for liking!")
    // }
    // return <button onClick={handleClick}>{children}</button>;

    // return <button onClick={() => alert("Thanks for fucking...")}>{children}</button>
    // return <button onChange={() => alert("Thanks for fucking...")}>{children}</button>
    // return <button onSubmit={() => alert("Thanks for fucking...")}>{children}</button>
    // return <button onMouseEnter={() => alert("Thanks for fucking...")}>{children}</button>
    
    const handleClick = (e) => {
        // alert("Thanks for liking!")
        console.log(e.target);
        console.log(e.clientX, e.clientY);
        console.log(e.button);
    }

    return <button onClick={handleClick}>{text}</button>
}   
