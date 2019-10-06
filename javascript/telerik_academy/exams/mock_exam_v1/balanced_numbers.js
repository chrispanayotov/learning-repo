let balancedNumbers = [];
let isNumBalanced = true;

function add(a, b) {
    return a + b;
}

while (isNumBalanced === true) {
    const n = +gets();
    let inputArray = [];
    inputArray[0] = n;

    for (let num of inputArray) {
        num = num.toString(10).replace(/\D/g, '0').split('').map(Number);
    
        if (num[0] + num[2] === num[1]) {
            balancedNumbers.push(num.join(''));
            isNumBalanced = true;
        } else {
            isNumBalanced = false;
        }
    }
}

balancedNumbers = balancedNumbers.map(Number).reduce(add, 0);

print(balancedNumbers);