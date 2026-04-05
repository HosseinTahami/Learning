import { UserInfo } from "./UserInfo"

// export const UserCards = ({name, age, city, email}) => {

//     return (
//         <>
//             <h2>User Details</h2>
//             <UserInfo name={name} age={age} city={city} email={email}/>
//         </>
//     );
// }   

export const UserCards = ({id, ...rest}) => {

    return (
        <>
            <h2>User {id} Details</h2>
            <UserInfo {...rest}/>
        </>
    );
}