// The Luhn formula is widely used system for validating identification numbers.
// Using the original number, double the value of every other digit.
// Then add the values of the individual digits together 
// (if a doubled value now has two digits, add the digits individually).
// The ID number is valid if the sum is divisible by 10.

// Write a program that takes an ID number of arbitrary length and determines
// whether the number is valid under the Luhn formula. The program must process
// each character before reading the next one.

function luhnValidation(id) {
    let idArray = id.toString().split('').map(Number);
    let checkSumArray = [];
    let doubledDigits = 0;

    for (let i = 0; i < idArray.length; i++) {
        
        // Double every odd digit
        if (i % 2 != 0) {
            doubledDigits = idArray[i] * 2;

            if (doubledDigits > 9) {
                checkSumArray.push(1, doubledDigits % 10);
            } else {
                checkSumArray.push(idArray[i+1]);
            }
        } else {
            checkSumArray.push(idArray[i]);
        }
    }

    // Sum the numbers in the array
    let totalSum = checkSumArray.reduce((a, b) => a + b, 0);
    
    // Finds the check digit and adds it to the checkSumArray, so the overall sum will be 30
    // The final number needs to be divisible by 10
    if (totalSum % 10 != 0 ) {
        checkSumArray.push(10 - (totalSum % 10));
        console.log(`Checksum digit is: ${10 - (totalSum % 10)}`)
        totalSum = checkSumArray.reduce((a, b) => a + b, 0);
    }

    return totalSum;
}

console.log(luhnValidation(176248)); // => returns 30;