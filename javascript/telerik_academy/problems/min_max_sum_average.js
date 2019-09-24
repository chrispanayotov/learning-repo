// Write a program that reads from the console a sequence of N real numbers and 
// returns the minimal, the maximal number, the sum and the average of all numbers 
// (displayed with 2 digits after the decimal point).

const n = +gets();
let inputArray = [];

for (let i = 0; i < n; i++) {
    inputArray[i] = +gets();
}

Array.min = function (inputArray) {
    return Math.min.apply(Math, inputArray);
}

Array.max = function (inputArray) {
    return Math.max.apply(Math, inputArray);
}

let min = Array.min(inputArray);
let max = Array.max(inputArray);
let sum = inputArray.reduce((a, b) => a + b, 0);
let avg = sum / inputArray.length;

console.log(`min=${min.toFixed(2)}`);
console.log(`max=${max.toFixed(2)}`);
console.log(`sum=${sum.toFixed(2)}`);
console.log(`avg=${avg.toFixed(2)}`);

