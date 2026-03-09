let numbers = [1, 2, 1, 3, 4];


let result;
result = numbers.indexOf('a')

console.log(result);


result = numbers.indexOf(1)
console.log("index of 1: ", result)

result = numbers.lastIndexOf(1)
console.log("Last index Of 1: ", result);

console.log(numbers.includes(1));
console.log(numbers.includes('a'));


result = numbers.indexOf(1, 2) // Start the search from index number 2
console.log("index of 1: ", result)