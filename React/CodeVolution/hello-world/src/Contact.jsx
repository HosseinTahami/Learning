import { ActionButton } from "./ActionButton";

export const Contact = () => {

    const handleMessage = () => {
        alert("Sending your fuckin message...")
    }
    return (
        <div>
            <h2>Fuck us</h2>
            <ActionButton text="Contact Us" onClick={handleMessage}/>
        </div>
    );
}