let n = 1234567890; // returns 10
let digits, i;

function countDigits(n) {
    for (i = 1; n > 0.5; n /= 10, i++) { digits = i; }
    return digits;
}

console.log(countDigits(n));