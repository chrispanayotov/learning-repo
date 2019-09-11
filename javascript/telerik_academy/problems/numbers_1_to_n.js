// Write a program that enters from the console a positive integer n and prints 
// all the numbers from 1 to N inclusive, on a single line, separated by a whitespace.

const n = '5';
let result = '';

for (let i = 1; i <= n; i+= 1) {
    result += i + ' ';
}

print(result.trim());