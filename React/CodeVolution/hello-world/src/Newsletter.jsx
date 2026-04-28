import { ActionButton } from "./ActionButton"

export const Newsletter = () => {

    const handleSubscription = ()=>{
        alert("Subscrbing...");
    }

    return (
        <div>
            <h2>Subscribe to Newsletter</h2>
            <ActionButton text="subscribe" onClick={handleSubscription}/>
        </div>
    )
}