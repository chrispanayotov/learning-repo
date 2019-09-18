// Write a program that finds the most frequent number in an array of N elements.

let inputArray = [4, 1, 1, 4, 2, 3, 4, 4, 1, 2, 4, 9, 3];

let largestSequence = 0;
let mostFrequentNumber = 0;
let counter = 0;


for (let i = 0; i < inputArray.length; i++) {
    for (let j = 0; j < inputArray.length; j++) {
        if (inputArray[i] === inputArray[j]) {
            counter += 1;

            if (counter > largestSequence) {
                largestSequence = counter;
                mostFrequentNumber = inputArray[i];
            }
        }
    }
    counter = 0;
}

console.log(mostFrequentNumber + `(${largestSequence} times)`);