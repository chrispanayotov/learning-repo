// Given an array, find the int that appears an odd number of times.
// There will always be only one integer that appears an odd number of times.

function findOdd(A) {
    let countsArray = {};
    let oddNum = 0;

    // Creates an Object with the counted numbers from input array
    for (let i = 0; i < A.length; i++) {
        let num = A[i];
        countsArray[num] = countsArray[num] ? countsArray[num] + 1 : 1;
    }

    // Loop iterates over the associative array and finds the odd int
    for (let x of Object.values(countsArray)) {
        if (x % 2 != 0) {
            oddNum = x;
        }
    }

    // Function gets key (odd int) by it's value
    function getKeyByValue(object, value) {
        return Object.keys(object).find(key => object[key] === value);
    }

    // Return the odd int casted from string to number
    return Number(getKeyByValue(countsArray, oddNum));

  }


console.log(findOdd([1,1,2,-2,5,2,4,4,-1,-2,5])); // => returns -1