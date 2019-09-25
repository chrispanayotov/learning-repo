// Write a function that accepts an array of 10 integers (between 0 and 9),
// that returns a string of those numbers in the form of a phone number.

function createPhoneNumber(numbers){
    let firstDigits = numbers.splice(0, 3).join('');
    let secondDigits = numbers.splice(0, 3).join('');
    let lastDigits = numbers.splice(0, 4).join('');

    return '(' + `${firstDigits}` + ')' + ' ' + `${secondDigits}` + '-' + `${lastDigits}`;    
}

console.log(createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) // => returns "(123) 456-7890"


// Other coder's solutions

function createPhoneNumber(numbers){
    var format = "(xxx) xxx-xxxx";
    
    for(var i = 0; i < numbers.length; i++)
    {
      format = format.replace('x', numbers[i]);
    }
    
    return format;
}