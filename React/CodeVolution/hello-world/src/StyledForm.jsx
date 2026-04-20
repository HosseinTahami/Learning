export const StyledForm = () => {

    // return (
    //     <form class="contact-from">
    //         <label for="username">UserName:</label>
    //         <input type="text" id="username" class="form-input"/>
    //         <br />
    //         <label for="email"></label>
    //         <input type="text" id="email" class="form-input" />
    //     </form>
    // )

    return (
    <form className="contact-from">
        <label htmlFor="username">UserName:</label>
        <input type="text" id="username" className ="form-input"/>
        <br />
        <label htmlFor="email">Email:</label>
        <input type="text" id="email" className="form-input" tabIndex="1" />
    </form>
)

}