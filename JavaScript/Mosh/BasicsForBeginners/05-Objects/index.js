// Object

const circle = {

    radius: 1,
    color: "blue",
    center: {
        x: 1,
        y: 5,
    },
    isVisible: true,

    // draw method
    draw: function () {
        console.log('draw');
    }
};


circle.draw(); // Method


// Factory Function 

function createCircle(radius, color, location ) {

    return {

    radius,
    // draw method
        draw: function () {
            console.log('draw');
        }
    };
}

const my_circle = createCircle(1);
const my_another_circle = createCircle(1);

console.log(my_circle);
console.log(my_another_circle);

// Constructor Function

function Circle(radius){
    this.radius = radius;
    this.draw = function(){
        console.log('draw');
    }
}

const super_circle = new Circle(3);



// class Circle {
//     constructor(radius) {
//         this.radius = radius;
//         this.draw = function () {
//             console.log('draw');
//         };
//     }
// }


// const, means we can't reassign it
// but we can change it.
const car = {

    size: "Big",
    accelerate: function(){},
    engine: "V8"
}

car.color = 'Blue';
car.move = function(){}

delete car.accelerate;

console.log(car);

// Every object has a constructor property, and that
// references to the function that was used to create that
// object.

const anotherCircle = new Circle(4); // Circle.call({}, 1)
const oneCircle = createCircle(2);

console.log(anotherCircle.constructor) // Function: Circle
console.log(oneCircle.constructor)     // Function: Object

// String(), Number(), Object(), Boolean() are all constructor
// but we use literals for creating new objects.

let my_object = {};  // let my_object = new Object();

let my_string = ``;  // let my_string = new String();

let my_number = 4;   // let my_number = new Number();

let bool = false;    // let bool = new Boolean(); 


 