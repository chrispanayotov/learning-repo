// Write a program that finds and prints the biggest prime number which is <= N.

const n = +gets();
let biggestPrime = 0;

// Algorithm starts counting backwards from N, 
// saves the biggest prime number in variable and breaks from loop.
// Solved like this to minimize operations and save time
for (let counter = n; counter <= n; counter--) {

    let notPrime = false;
    for (let i = 2; i <= counter; i++) {
        if (counter % i ===0 && i !== counter) {
            notPrime = true;
        }
    }
    if (notPrime === false) {
        biggestPrime = counter;
        break;
    }
}

print(biggestPrime);