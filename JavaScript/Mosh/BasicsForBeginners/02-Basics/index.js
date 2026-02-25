// Comments

// Camel variable Name
let firstName = 'Hossein';
console.log(firstName);


// const for Constants
const interestRate = 0.3;
//interestRate = 1;
console.log(interestRate);

// Primitive (Value Types) & Reference Type

// 1- Primitive Types
let age = 30;                   // Number
let familyName = 'Tahami';      // String
let isApproved = true;          // Boolean
let middleName = undefined;     // undefined
let selectedColor = null;       // null

// Static Language & Dynamic Language
// Java is Dynamic

let herName = "Sonic";
console.log(typeof(herName)); // string

herName = 1;
console.log(typeof(herName)); // number

herName = false;
console.log(typeof(herName)); // boolean

herName = 21.4;
console.log(typeof(herName)); // number

herName = undefined;
console.log(typeof(herName)); // undefined

herName = null;
console.log(typeof(herName)); // object 

// 2- Reference Types
// a.Object, b.Array, c.Functions

// a.Object
let person = {

    firstName: "Hossein",
    age: 33,
    height: 190,
    weight: 90,
};

console.log("Person Object: ",person);
console.log("Age:", person.age);
console.log("First Name:", person.firstName);

person.firstName = "Seyed Hossein";
console.log(person);


person["firstName"] = "Hossein Tahami"
console.log(person);

// b.Array
let selectedColors = ['Red', 'Blue'];
console.log(selectedColors);
console.log(
    "SelectedColors[0]:", selectedColors[0],
);
console.log(
    "SelectedColors[1]:", selectedColors[1]
);

// Array is Dynamic and the length of it can change
selectedColors[2] = 'green';
console.log(selectedColors);

console.log("Length: ",selectedColors.length);

// c.Functions

// Performing a Task
function greet(firstName, lastName) {
    console.log("Hello" ,firstName, lastName , "via Alfonso Lamarmora, 80");
}

greet('Hossein', 'Tahami');

// Calculate Value
// Square the number
function square(num){
    return num * num;
}

let value = square(4);
console.log(value);