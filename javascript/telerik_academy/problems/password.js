// Write a program that does the following:
// Reverses a six digit number ( 99999 < N < 1000000, 0 < K < 1000 )
// Sums the result of division and modulus of reversed number by a number K

const input = gets();

let inputArray = input.split(' ').map(Number);

let n = inputArray[0];
let k = inputArray[1];

// Converts the input integer to string and then uses map to create an array of numbers
// After that reverses the array as required
inputArray = n.toString(10).split('').map(Number).reverse();

// Converts the reversed number from array to Number, so we can do math operations on it
let reversedNumber = Number(inputArray.join(''));

let result = (reversedNumber / k) + (reversedNumber % k);

print(Math.floor(result));