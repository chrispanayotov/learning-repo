// Need to find a way to rank numbers that are equal

const n  = 4;
let inputArray = [9, 1, 1, 1];

// Makes a copy of the original Array, so we can save the order of the input
let inputArrayCopy = Array.from(inputArray);

// Sort in descending order so we can rank the numbers
inputArray.sort((a, b) => b - a);

let associativeArray = new Object();
let counter = 1;
let result = ''

for (let i = 0; i < n; i++) {
    associativeArray[inputArray[i]] = counter;
    counter++;
}

for (let num of inputArrayCopy) {
    result += associativeArray[num] + ' ';
}

console.log(result.trim());