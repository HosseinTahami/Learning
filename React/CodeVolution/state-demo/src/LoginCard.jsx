import { useState } from "react";

export const LoginCard = () => {

    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const [message, setMessage] = useState("");

    const handleLogin = () => {
        setIsLoggedIn(!isLoggedIn);
    }


    const messageHandler = (e) =>{

        setMessage(e.target.value);
        
    };

    return (
    
        <>
        <button onClick={handleLogin}>{isLoggedIn ? "LogOut" : "Login"}</button>
        <div>
            <input type="text"
             placeholder="Type a message"
            value={message}
            onChange={messageHandler}/>

            <p>{message}</p>
        </div>
        </>
    );

};