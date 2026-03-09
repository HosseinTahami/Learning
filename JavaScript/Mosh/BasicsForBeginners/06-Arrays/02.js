let numbers = [5];

// End Of Array
numbers.push(9, 0)

console.log(numbers)


// Beginning Of Array
numbers.unshift(1, 3)

console.log(numbers)


// Middle Of Array
numbers.splice(2, 0, -1, 'b') // start, deleteCount, elements 

console.log(numbers)