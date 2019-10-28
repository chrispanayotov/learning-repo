// Write a JS function that checks if a given matrix of numbers is magical. 
// A matrix is magical if the sums of the cells of every row and every column are equal. 
// The input comes as an array of arrays, containing numbers (number 2D matrix). 

// The input numbers will always be positive.


function magicChecker (arr) {
    return checkMagic(arr) &&
           checkMagic(rotate(arr));
  
    function rotate(array) {
        return array[0].map((x, i) => array.map(x => x[i]))
    }
   
    function checkMagic(arr) {
        arr = arr.map(x => x.reduce((a, b) => a + b));
 
        return Array.from(new Set(arr)).length === 1;
    }
}

console.log(magicChecker([
    [4, 5, 6],
    [6, 5, 4],
    [5, 5, 5]
])); // => returns true