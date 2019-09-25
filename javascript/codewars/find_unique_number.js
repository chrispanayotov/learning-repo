// Find the unique number in an array of integers

function findUniq(arr) {
    let countedNums = {};

    // Creates an Object with the counted numbers from input array
    for (let i = 0; i < arr.length; i++) {
        let num = arr[i];
        countedNums[num] = countedNums[num] ? countedNums[num] + 1 : 1;
    }

    // Function finds the value that is 1 (unique item) in the counted array 
    // and gets the key
    function getKeyByValue(object, value) {
        return Object.keys(object).find(key => object[key] === value);
    }

    // Calls getKeyByValue with 1 in order to find the unique item
    return Number(getKeyByValue(countedNums, 1));
}

console.log(findUniq([ 0, 0, 0.55, 0, 0 ])); // returns => 0.55