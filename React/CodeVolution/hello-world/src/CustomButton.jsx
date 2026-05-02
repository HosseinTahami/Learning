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
        console.log("Clicked Element: ", e.target);
        console.log("Clicked Coordinates: ", e.clientX, e.clientY);
        console.log("Which Button: ", e.button);
    }

    return <button onClick={handleClick}>{text}</button>
}   


// Every Event Handler, recivers an Event Object