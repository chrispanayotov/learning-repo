// You receive a 2D matrix of numbers as an array
// Each element of the input array is an array of numbers
// Write a JS function to find the biggest number

function findBiggestNum(matrix) {
    
    // Sets biggestNum to -Infinity, 
    // so it can be compared with the next biggest number in the matrix
    let biggestNum = Math.max();

    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {
            if (matrix[i][j] > biggestNum) {
                biggestNum = matrix[i][j];
            }
        }
    }
    return biggestNum;
}

let matrixArray = [
    [3, 5, 17, 12, 91, 5],
    [-1, 7, 4, 33, 6, 22],
    [1, 8, 99, 3, 10, 43]
];

console.log(findBiggestNum(matrixArray)); // returns 99