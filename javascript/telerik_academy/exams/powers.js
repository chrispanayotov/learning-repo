// Transform an array of numbers the following way:
// each 0 - with the absolute difference of its neighbouring numbers
// all other even numbers - with the maximum of its neighbouring numbers
// each 1 - with the sum of its neihgbouring numbers
// all other odd numbers - with the minimum of its neighbouring 

// The leftmost and rightmost are considered neighbours

// A K-sum of a sequence is the sum of the numbers after K transformations 
// Find the K-sum of a given sequence

function transformArray(k, arr) {
    let counter = 0;

    while (counter < k) {
        let currentTransformation = [];

        for (let i = 0; i < arr.length; i += 1) {

            let currentElement = arr[i];

            // Check if loop is on the first element and transforms it
            if (i === 0) {
                currentTransformation.push(transform(currentElement, arr.slice(-1)[0], arr[1]));

            // Else checks if loop is on the last element and transforms it
            } else if (i === arr.length - 1) {
                currentTransformation.push(transform(currentElement, arr[i - 1], arr[0]));

            // In any other case get the neighbours of current element and do transformation
            } else {
                currentTransformation.push(transform(currentElement, arr[i - 1], arr[i + 1]));
            }
        }

        arr = currentTransformation;
        counter += 1;
    }

    function transform(num, left, right) {

        if (num === 0) {
            return Math.abs(left - right);
        } else if (num % 2 === 0) {
            return Math.max(left, right);
        } else if (num === 1) {
            return left + right;
        } else {
            return Math.min(left, right);
        }

    }

    function add(a, b) {
        return a + b;
    }

    return arr.reduce(add, 0);
}

// let k = 1;
// let array = [9, 0, 2, 4, 1]; // (becomes 0 7 4 2 13) => returns 26

let k = 3;
let array = [1, 9, 1, 9, 1, 9, 1, 9, 1, 9]; // becomes 18 1 18 1 18 1 18 1 18 1 =>
// 1 36 1 36 1 36 1 36 1 36 1 36 1 36 => 72 1 72 1 72 1 72 1 72 1 => returns 365

console.log(transformArray(k, array));