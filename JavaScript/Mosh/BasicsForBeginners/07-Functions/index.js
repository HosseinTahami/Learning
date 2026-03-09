// Function Declaration

walk();

function walk(){
    console.log('Walk');
}

// Function Expression
let run = function () {

    console.log("Run");
};

let move = run;

run();
move();

// Hoisting: With Function Declaration, use the function before
//           itself, but this is not possible in function expression.

function sum (a, b){
    console.log(arguments);
    return a + b;
}

console.log(sum(1));
console.log(sum(1, 3));
console.log(sum(2, 5, 6));


function advance_sum(){

    let total = 0;
    for (let val of arguments)
        total+=val;

    console.log(total);
}

advance_sum(3, 5, 62, 43, 2, 3);


function super_sum(...args){
    let total = 0;
    for (let val of args)
        total += val;

    console.log(total);
}

super_sum(4, 5, 6, 52, 9, 80, 4)


function final_price(discount, ...price){

    total = price.reduce( (a, b) => a + b);
    return total * (1 - discount);
}


console.log(final_price(0.2, 2, 5, 2, 4, 5));