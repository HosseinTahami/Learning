// Operators in JavaScript
// a.Arithmetic |   b.Assignment    |   c.Comparison
// d.Logical    |   d. Bitwise      |   


// a.Arithmetic Operator

let x, y;
x = 10;
y = 20;

// console.log(x + y);
// console.log(x - y);
// console.log(x * y);
// console.log(x ** y);
// console.log(x / y);
// console.log(x % y);

// Increment & Decrement
console.log("x:", x);       // 10
console.log("++x:", ++x);   // 11, First increase then print
console.log("x:", x);       // 11

console.log("x++:", x++);   // 11, First print then increase
console.log("x:", x);       // 12

// b. Assignment Operator

let variable = 10;
variable += 1;
variable *= 3;
variable = variable + 5;


// c. Comparison Operators 


// Relational Operators
console.log(variable > 0);
console.log(variable >= 4);
console.log(variable < 9);
console.log(variable <= 3);


// Equality Operators  "==="
console.log(variable === 1);
console.log(variable !== 90);

// == Lose Equality: ==  VS. Strict Equality Operator: ===

// Strict Equality: Type + Value 

// Lose Equality: Value
// If the types are different convert 
// the right side type to the left side type
console.log('1' == 1);  // --> convert 1, which is number to String
console.log(true == 1); // --> convert 1, which is number to Boolean


// Ternary Operator
let points = 110;
let type = points > 100 ? 'Winner' : 'Looser';


// Logical Operators
// AND (&&), OR (||)
console.log(true && false);
console.log(false || true);

let isOkay = false; 
let isNotOkay = !isOkay;

// Falsy Values
// undefined, null, 0, false, '', NaN (Not a Number)
// Anything that is not falsy is Truthy !

// Short Circuiting
// false || false || 3 || NaN || undefined
// The moment it finds a truthy value, it will return True
// without checking other values

let userColor = undefined;
let defaultColor = 'blue';
let currentColor = userColor || defaultColor;
console.log(currentColor);

// Bitwise Computer
// Bitwise OR (|)
// 1 = 00000001
// 2 = 00000010

console.log(1 | 2); // 00000011 = 3

// Read, Write, Execute
// 00000100
// 00000010
// 00000001

const readPermission = 4;
const writePermission = 2;
const executePermission = 1;

let myPermission = readPermission || writePermission;

let message = 
    (myPermission & executePermission) ? 'yes' : 'no';

console.log(message);