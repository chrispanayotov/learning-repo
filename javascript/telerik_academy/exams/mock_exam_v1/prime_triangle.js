// const n = +gets();

let n = 27;
let primesArray = [];


const isPrime = n => {
    if (n < 0 || n === 0)
        return false;
    
    for (let i = 2; i < n; i += 1) {
        if (n % i === 0) {
            return false;
        }
    }
    return true;
}


// Check if numbers from 1 to N are Prime and pushes them to an array
for (let num = 1; num <= n; num += 1) {
    if (isPrime(num)) {
        primesArray.push(num);
    }
}


// Function converts the prime numbers to 1s and prints the triangle
const makeTriangle = (height) => {
    let createTriangle = '';

    for (let row = 0; row <= height; row += 1) {

        for (let i = 1; i <= primesArray[row]; i += 1) {

            if (primesArray.includes(i)) {
                createTriangle += '1';
            } else {
                createTriangle += '0';
            }

        }
        console.log(createTriangle);
        createTriangle = '';
    }
}

makeTriangle(primesArray.length);