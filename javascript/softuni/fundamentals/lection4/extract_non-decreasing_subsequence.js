// Write a JS function that extracts only those numbers that form a non-decreasing subsequence. 
// In other words, you start from the first element and continue to the end of the 
// given array of numbers. Any number which is LESS THAN the current biggest 
// one is ignored, alternatively if it’s equal or higher than the current biggest 
// one you set it as the current biggest one and you continue to the next number. 
// The input comes as an array of numbers.

function extractSubsequence(arr) {
    let resultArray = [];
    let currentLargestNum = Math.max(); // Set variable to -Infinity

    for (let i = 0; i < arr.length; i++) {

        if (arr[i] >= currentLargestNum) {
            resultArray.push(arr[i]);
            currentLargestNum = arr[i];
        }
        
    }
    
    for (let num of resultArray) {
        console.log(num);
    }
}

extractSubsequence([1, 3, 8, 4, 10, 12, 3, 2, 24]); // returns 1 3 8 10 12 24