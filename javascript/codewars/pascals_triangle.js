// Wikipedia article on Pascal's Triangle: http://en.wikipedia.org/wiki/Pascal's_triangle

// Write a function that, given a depth (n), returns a single-dimensional 
// array/list representing Pascal's Triangle from the first to the n-th level.

function pascalsTriangle(n) {
    let triangleArray = [];

    for (let i = 0; i < n; i++) {
        triangleArray[i] = new Array(i + 1);

        for (let j = 0; j < i+1; j++) {
            if (j === 0 || j === i) {
                triangleArray[i][j] = 1;
            } else {
                triangleArray[i][j] = triangleArray[i-1][j-1] + triangleArray[i-1][j];
            }
        }
    }
  
    return triangleArray.join().split(',').map(Number);
  }

pascalsTriangle(4) // => returns [1, 1, 1, 1, 2, 1, 1, 3, 3, 1]