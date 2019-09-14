// Write a program that finds the length of the maximal increasing sequence 
// in an array of N integers.

let inputArray = [7, 3, 2, 3, 5, 2, 2, 4];
let longestSequence = 1;
let count = 1;
let prev = 0;

// Prev variable starts from index 0 and compares whether the next number in the
// array is smaller. 
// If it is increase longestSequence variable by 1, else resets counter.

for (let i = 1; i < inputArray.length; i++) {
    if (inputArray[prev] < inputArray[i]) {
        count += 1;
        
        if (count > longestSequence) {
            longestSequence = count;
        }

    } else {
        count = 1;
    }
    
    prev += 1;
}

console.log(longestSequence);