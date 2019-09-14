// Write a program that finds the length of the maximal sequence of 
// equal elements in an array of N integers.

const n = +gets();
let inputArray = [];

// Get input from console and fill in array
for (let i = 0; i < n; i++) {
    inputArray[i] = +gets();
}

let longestSequence = 1;
let counter = 1;
let currentElement = inputArray[0];


for (let i = 1; i < n; i++) {
     // If the numbers are a match increase counter
    if (inputArray[i] == currentElement) {
        counter++;
        
        // When a new longest sequence has been found update the longestSequence variable
        if (counter > longestSequence) {
            longestSequence = counter;
        }
    } else {
        currentElement = inputArray[i];
        counter = 1;
    }
}

print(longestSequence);