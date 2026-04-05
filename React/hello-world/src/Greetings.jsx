export const Greetings = (props) => {

    return (
        <h2>{props.message ? props.message : "Hello"}, {props.name ? props.name : "Guest"}</h2>
    );
}

// export const Greetings = ({ message = "Hello", name = "Guest" }) => {
//     return (
//         <h2>{message}, {name}</h2>
//     );
// }