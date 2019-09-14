// Write a program that reads two integer numbers N and K and an array of N elements
// from the console. Find the maximal sum of K elements in the array.

const n = +gets();
const k = +gets();

let inputArray = [];
let resultArray = [];

for (let i = 0; i < n; i++) {
    inputArray[i] = +gets();
}

// Clones and sorts the input array in descending order
inputArray = inputArray.sort((a, b) => b - a); 

// Gets the first k elements in the sorted array and appends them to resultArray
for (let i = 0; i < k; i++) {
    resultArray.push(inputArray[i]);
}

// Sums the numbers in result array
print(resultArray.reduce((a, b) => a + b, 0));