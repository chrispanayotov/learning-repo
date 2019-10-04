// You are given a matrix of elements
// Find the number of equal neighbors

function findEqualNeighbours(matrix) {
    let neighbors = 0;

    for (let row = 0; row < matrix.length-1; row++) {
        for (let col = 0; col < matrix[row].length; col++) {
            if (matrix[row][col] === matrix[row + 1][col] || matrix[row][col] === matrix[row][col +1]) {
                neighbors++;
            }
        }
    }
    
    return neighbors;
}

let matrixArray = [
    [2, 2, 5, 7, 4],
    [4, 0, 5, 3, 4],
    [2, 5, 5, 4, 2]
];

console.log(findEqualNeighbours(matrixArray));