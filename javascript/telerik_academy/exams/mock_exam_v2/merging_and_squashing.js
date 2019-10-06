const n = +gets();
let inputArray = [];

for (let i = 0; i < n; i++) {
    inputArray[i] = +gets();
}

let mergedNumbersArray = [];
let squashedNumbersArray = [];
 
function mergeNumbers (a, b) {
    a = a.toString(10).split('');
    b = b.toString(10).split('');
    let mergedNumber = '';

    mergedNumbersArray.push(mergedNumber += a[1] + b[0]);
}


function squashNumbers (a, b) {
    a = a.toString(10).split('').map(Number);
    b = b.toString(10).split('').map(Number);
    let squashedNumber = '';

    let c = a[1] + b[0];

    if (c > 9) {
        c = c.toString(10).split('').map(Number);
        c = c[1];
    }

    a = a.toString(10).split(',');
    b = b.toString(10).split(',');
    c = c.toString(10);

    squashedNumbersArray.push(squashedNumber += a[0] + c + b[1]);
}

for (let i = 0; i < n -1; i += 1) {
    mergeNumbers(inputArray[i], inputArray[i+1]);
    squashNumbers(inputArray[i], inputArray[i+1]);
}

print(mergedNumbersArray.join(' '));
print(squashedNumbersArray.join(' '));