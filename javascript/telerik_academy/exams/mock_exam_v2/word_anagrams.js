let targetWord = gets();
let n = +gets();

let inputArray = [];

for (let i = 0; i < n; i++) {
    inputArray[i] = gets();
}


function isAnagram(word, words) {
    let targetWordAsciiScore = 0;
    let currentWordAsciiScore = 0;

    for (let char of word) {
        targetWordAsciiScore += char.charCodeAt(0);
    }

    for (let w of words) {
        for (let letter of w) {
            currentWordAsciiScore += letter.charCodeAt(0);
        }

        if (currentWordAsciiScore === targetWordAsciiScore) {
            print('Yes');
        } else {
            print('No');
        }
        currentWordAsciiScore = 0;
    }
}


isAnagram(targetWord, inputArray);