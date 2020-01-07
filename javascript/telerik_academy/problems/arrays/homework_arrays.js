const arr = [2, 1, 3, 4, 6, 0, 0, 5, 7, 8, 10];

// Create a new copy of the array - DONE
const copyArr = arr.slice();

// Reverse the array - DONE
const reverseArr = arr.reverse();

// Find if the number ```10``` is in the array in an array of integers 
// and return ```true``` or ```false``` - DONE
const includesNum = arr.includes(10);   // true

// Find the first element greater than ```6``` in an array of integers and return it - DONE
const greaterThanSix = copyArr.find(function(item, index, arr) {
    return item > 6;
});

// Remove duplicates from an array of integers - DONE
function removeDuplicates(array) {
    let duplicatesRemoved = Array.from(new Set(array));
    
    return duplicatesRemoved;
}

// Flatten an array of integers 
const multyArr = [1, 2, [3, 4, [5, 6]]];

function flatDeep(arr, d = 1) {
    return d > 0 ? arr.reduce((acc, val) => acc.concat(Array.isArray(val) 
    ? flatDeep(val, d - 1) : val), []) : arr.slice();
};

// Write a function to find the **most occurring element** in an array of integers - DONE
const occArr = [1, 2, 1, 4, 2, 4, 2, 3, 3, 5, 6, 7, 3, 2];

 function mostOccuringElement(array) {
     let occurrencesObj = {};
     let mostOccEle = 0;
     
     // Sort the array so it'll be easier to count the numbers
     array.sort();
     //  [ 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5, 6, 7 ]
     
     // Scans the array and adds key(Number)/value(Occurence) to occurrencesObject
     for (let i = 0; i < array.length; i += 1) {
        let currentEle = array[i];
        let counter = 0;

        for (let j = 0; j <= array.length; j += 1) {

            if (currentEle === array[j]) {
                counter += 1;
            } else  if (counter > 0) {
                occurrencesObj[array[i]] = counter;
                break;
            }
        }
    }        

    // Get the number with the highest occurence
    for (let key in occurrencesObj) {
        if (occurrencesObj[key] > mostOccEle) {
            mostOccEle = occurrencesObj[key]
        }
    }

    return occurrencesObj[mostOccEle];
}

// Create a **4x4 multidimensional array** and fill it with the letters from ```a``` to  ```p``` - DONE
function createMatrix(rows, cols) {
    let matrix = [];
    let letter = 97;

    for (let row = 0; row < rows; row += 1) {
        matrix[row] = [];

        for (let col = 0; col < cols; col += 1) {
            matrix[row][col] = String.fromCharCode(letter);
            letter += 1
        }
    }

    return matrix;
}

function getMainDiagonal(matrix) {
    for (let i = 0; i < matrix.length; i += 1) {
        console.log(matrix[i][i]);
    }
}

function getSecondaryDiagonal(matrix) {
    let length = matrix.length - 1;
    for (let i = 0; i < matrix.length; i += 1) {
        console.log(matrix[i][length-i]);
    }
}

const matrix = createMatrix(4, 4);
console.log(getSecondaryDiagonal(matrix));
