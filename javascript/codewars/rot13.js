// ROT13 is a simple letter substitution cipher that replaces a letter with the 
// letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

// Create a function that takes a string and returns the string ciphered with Rot13. 
// If there are numbers or special characters included in the string, they should 
// be returned as they are. Only letters from the latin/english alphabet should 
// be shifted, like in the original Rot13 "implementation".

function rot13(message) {
    let encryptedMessageArray = [];

    // Functions checks if a char is a letter
    let isLetter = function(str) {
        return str.length === 1 && str.match(/[a-z]/i);
    }
    // Main for-loop, which loops over every character in message string
    for (let char of message) {
        
        // If block checks if char is a letter and lower-case using Ascii values
        if (char === char.toLowerCase() && isLetter(char)) {

            // If letter is lower than half of alphabet, directly add 13 to it
            if (char.charCodeAt(0) > 96 && char.charCodeAt(0) < 110) {
                let encryptedLetterLower = char.charCodeAt(0) + 13;
                encryptedMessageArray.push(String.fromCharCode(encryptedLetterLower));

            // Replaces the letter with the 13th letter after it in the alphabet
            } else {
                let x = 123 - char.charCodeAt(0);
                let y = Math.abs(13 - x);
                let resultLower = y + 97;
                encryptedMessageArray.push(String.fromCharCode(resultLower));
            }

        // Same thing as above, but for upper-case letters
        } else if (char === char.toUpperCase() && isLetter(char)) {
            if (char.charCodeAt(0) > 64 && char.charCodeAt(0) < 78) {
                let encryptedLetterUpper = char.charCodeAt(0) + 13;
                encryptedMessageArray.push(String.fromCharCode(encryptedLetterUpper));

            } else {
                let z = 91 - char.charCodeAt(0);
                let w = Math.abs(13 - z);
                let resultUpper = w + 65;
                encryptedMessageArray.push(String.fromCharCode(resultUpper));
            }

        // If it is not a letter, checks if character is a space and pushes it
        } else if (/\s/.test(char)) {
            encryptedMessageArray.push(char);

        // In any other case push the symbol to array
        } else {
            encryptedMessageArray.push(char);
        }
    } 
    return encryptedMessageArray.join('');
}

console.log(rot13('Test')); // => returns Grfg;