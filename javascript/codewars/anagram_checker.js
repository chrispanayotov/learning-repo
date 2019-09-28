function anagrams(word, words) {
    let targetWordAsciiScore = 0;
    let currentWordAsciiScore = 0;
    let anagramsArray = [];

    // Algorithm sums the Ascii score of the target word and then checks
    // whether the other words in the array have the same score
    // If they do, then it means it's an anagram and pushes the word in new array
    // which is then returned
    
    for (let char of word) {
        targetWordAsciiScore += char.charCodeAt(0);
        }

    for (let w of words) {
        for (let letter of w) {
            currentWordAsciiScore += letter.charCodeAt(0);
        }

        if (currentWordAsciiScore === targetWordAsciiScore) {
            anagramsArray.push(w);
        }

        currentWordAsciiScore = 0;
    }
    return anagramsArray;
}


console.log(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']));

// anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']