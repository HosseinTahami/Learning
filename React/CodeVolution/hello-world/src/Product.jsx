// export const Product = (props) => {


//     return (

//         <div>
//             <h3>{props.title}</h3>
//             <p>Price: ${props.price}</p>
//             <p>In Stock: {props.inStock ? "Yes" : "No"}</p>
//             <p>Category: {props.categories.join(", ")} </p>
//         </div>
//     )
// }


export const Product = ({title, price, inStock, categories}) => {


    return (

        <div>
            <h3>{title}</h3>
            <p>Price: ${price}</p>
            <p>In Stock: {inStock ? "Yes" : "No"}</p>
            <p>Category: {categories.join(", ")} </p>
        </div>
    )
}