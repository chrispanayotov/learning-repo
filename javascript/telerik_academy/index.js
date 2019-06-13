// Object literal
let person = {
    name: 'Chris',
    age: 28
};
// Dot Notation
person.name = 'NotChris';

// Bracket Notation
let selection = 'name';
person[selection] = 'Mary';

// Array literal
let selectedColors = ['red', 'blue'];
selectedColors.push('green');
console.log(selectedColors.length);

// Basic function
function greet(name, lastName) {
    console.log('Hello, ' + name + ' ' + lastName + '!');
}
greet('John', 'Smith');

// Calculating function
function square(number) {
    return number * number;
}

console.log(square(5))