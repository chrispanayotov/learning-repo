// Write a JS function that orders a given array of strings, by length 
// in ascending order as primary criteria, and by alphabetical value in ascending order 
// as second criteria. The comparison should be case-insensitive.

// The input comes as an array of strings.

function sortArray(arr) {
    arr.sort(function(a, b) {
        return a.length - b.length || a.localeCompare(b);
    })
    for (let word of arr) {
        console.log(word);
    }
}

sortArray(['alpha', 'beta', 'gamma']); // => returns beta alpha gamma