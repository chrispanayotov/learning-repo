// const n = +gets();

let n = 27;
let primesArray = [];

// Check if numbers from 1 to N are Prime and pushes them to an array
for (let num = 1; num <= n; num += 1) {
    if (isPrime(num) === true) {
        primesArray.push(num);
    }
}

function isPrime(num) {
    if (num < 1) return false;
    if (num === 2) return true;
  
    let sqrt = Math.sqrt(num);
  
    for (let i = 2; i <= sqrt; i += 1) 
      if (num % i === 0) return false;
    return true;
}

// Function converts the prime numbers to 1s and prints the triangle
function makeTriangle(height) {
    let output = '';

    for (let row = 0; row <= height; row += 1) {

        for (let i = 1; i <= primesArray[row]; i += 1) {

            if (primesArray.includes(i)) {
                output += '1';
            } else {
                output += '0';
            }

        }
        console.log(output);
        output = '';
    }
}

makeTriangle(primesArray.length);