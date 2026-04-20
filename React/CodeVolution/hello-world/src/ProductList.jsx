

export const ProductList = () =>{

    const products = [
        {
            id: 1,
            name: "Laptop",
            price: 99
        },
        {   
            id: 2,
            name: "Phone",
            price: 4299
        },
        {
            id: 3,
            name: "Tablet",
            price: 6387
        }
    ];

    const productElements = products.
    filter((product) => { 
        return product.price > 500;
    }).map((product) => {
    return (
        <div key={product.id}>
            <h3>{product.name}</h3>
            <p>Price: $(product.price)</p>
        </div>
    );
});



    return (
        <div>
            <h2>Our Products</h2>
            {productElements}
        </div>
    );
};