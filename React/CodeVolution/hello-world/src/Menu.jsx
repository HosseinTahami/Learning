import { MenuItem } from './MenuItem';

export const Menu = () => {

    const handleOrder = (itemName, itemPrice) => {
        alert(`You ordered ${itemName} for ${itemPrice} `)
    };

    return (
        <div>
            <h2>Our Menu</h2>
            <MenuItem name="Sucide Kit" price={33} onOrder={handleOrder}/>
            <MenuItem name="Nothing" price={33} onOrder={handleOrder}/>
            <MenuItem name="Everything" price={33} onOrder={handleOrder}/>
        </div>
    )
}