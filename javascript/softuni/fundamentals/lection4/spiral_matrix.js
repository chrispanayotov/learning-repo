// Write a JS function that generates a Spirally-filled matrix with numbers, with given dimensions.
// The input comes as 2 numbers that represent the dimension of the matrix. 
// The output is the matrix filled spirally starting from 1.
// You need to print every row on a new line, with the cells separated by a space. 

function createSpiralMatrix (m, n) {

    // First we create the empty matrix m x n
    let result = new Array(m).fill().map(() => new Array(n).fill(''));

    // Set the ranges that we are going to use to fill in the 2D array
    let counter = 1;
    let rowStart = 0;
    let rowEnd = m - 1;
    let colStart = 0;
    let colEnd = n - 1;
    let i, j;

    // While loop "keeps track" whether the matrix is being filled in a spiral way
    while (colStart <= colEnd && rowStart <= rowEnd) {
        // Fill in the first row of the matrix until n - 1
        for (i = colStart;  i <= colEnd; i += 1) {
            result[rowStart][i] = counter;
            counter += 1;
        }

        rowStart += 1;

        // Fill in the last column of the matrix 
        for (j = rowStart; j <= rowEnd; j += 1) {
            result[j][colEnd] = counter;
            counter += 1;
        }

        colEnd -= 1;

        // Reverse the direction and fill in the last row of the matrix
        for (i = colEnd; i >= colStart; i -= 1) {
            result[rowEnd][i] = counter;
            counter += 1;
        }

        rowEnd -= 1;

        // Fills the numbers in an upwards direction 
        for (i = rowEnd; i >= rowStart; i -= 1) {
            result[i][colStart] = counter;
            counter += 1;
        }

        colStart += 1;

    }

    for (i = 0; i < result.length; i += 1) {
        console.log(result[i].join(' '));
    }
}

createSpiralMatrix(m , n);