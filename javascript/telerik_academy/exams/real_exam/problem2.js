let englishString = 'test';
let spanishString = 'el examen';

// returns ph pxamen

function solve (english, spanish) {
    let alienMessageArray = [];
    let alphabetObject = {};
    let alphabetArray = 'abcdefghijklmnopqrstuvwxyz'.split('');
    let incrementer = 0;
    english = english.split('');
    spanish = spanish.split('');

    let longestString = Math.max(english.length, spanish.length);

    // Create an object letter being the key and number being the value
    // 'a': 0,
    // 'b': 1 .. and so on
    for (let i = 97; i < 123; i += 1) {
        alphabetObject[String.fromCharCode(i)] = incrementer;
        incrementer += 1;
    }

    for (let i = 0; i < longestString; i += 1) {
        let result =  Math.abs(alphabetObject[english[i]] - alphabetObject[spanish[i]]);

        if (english[i] === " " || spanish[i] === " ") {
            alienMessageArray.push(" ");
            continue;
        }
        
        // If a letter from either languages is undefined, 
        // it means the string is over, so append the letter from the opposite language
        if (!alphabetObject[english[i]]) {
            result = alphabetObject[spanish[i]];
        } else if (!alphabetObject[spanish[i]]) {
            result = alphabetObject[english[i]];
        }
        //Converts the number result to a letter and push to array
        alienMessageArray.push(alphabetArray[result]);
    }
    console.log(alienMessageArray.join(''));
}

solve(englishString, spanishString);