// You receive a 2D matrix of numbers as an array
// Each element of the input array is an array of numbers
// Find sum at the main and at the secondary diagonals

function sumDiagonals(matrix) {
    let sumLeftDiagonal = 0;
    let sumRightDiagonal = 0;
    let y = matrix[0].length - 1;

    for (let i = 0; i < matrix.length; i++) {
        sumLeftDiagonal += matrix[i][i];
        sumRightDiagonal += matrix[i][y];
        y--;
    }

    return Array(sumLeftDiagonal, sumRightDiagonal);
}

let matrixArray = [
    [3, 5, 17],
    [-1, 7, 14],
    [1, -8, 89]
];

console.log(sumDiagonals(matrixArray));