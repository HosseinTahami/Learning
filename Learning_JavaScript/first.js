function Person(name, age, gender){
    this.name = name;
    this.age = age;
    this.gender = gender;

}

var P1 = new Person("Hossein", "22", "Male");
console.log(P1.age);

function Car(name, price){
    this.name = name;
    this.price = price;
    this.final_price = function(discount){
        this.price = this.price * (100-discount)/100;
        console.log(this.price)
    }
}

var C1 = new Car("BMW", 100000);
C1.final_price(10);