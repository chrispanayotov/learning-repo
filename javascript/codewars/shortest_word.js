// Simple, given a string of words, return the length of the shortest word(s).
// String will never be empty and you do not need to account for different data types.

function findShort(s) {
    let wordsArray = s.split(' ');
    let shortestWord = 999999999999999;

    for (let word of wordsArray) {
        if (word.length < shortestWord) {
            shortestWord = word.length;
        }
    }    

    return shortestWord;
}

console.log(findShort("bitcoin take over the world maybe who knows perhaps")); // returns 3