import { UserInfo } from "./UserInfo"

// export const UserCard = ( { name, age, city, email } ) => {

//     return (
//         <div>
//             <h2> User Details </h2>
//             <UserInfo name={name} age={age} city={city} email={email} />
//         </div>
//     )
// }


// export const UserCared =  (probs) => {

//     return (
//         <div>
//             <h2>User Details</h2>
//             <UserInfo {...props} />
//         </div>

//     );
// };




export const UserCared =  (id, ...rest) => {

    return (
        <div>
            <h2>User {id} Details</h2>
            <UserInfo {...rest} />
        </div>

    );
};
