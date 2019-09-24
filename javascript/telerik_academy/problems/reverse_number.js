// Write a program that reverses the digits of a given decimal number.

const input = 123.45;

let x = input.toString();

let y = x.split('').reverse().join('');

console.log(Number(y));