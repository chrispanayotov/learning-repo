// You are given a sequence of numbers representing heights. A peak is a height
// that is larger than it's direct neighbours. A valley is a sequence of 3 or more
// heights between two peaks, including the peak.

// Write a program which finds the largest sum of heights in a valley.

// Input will consist of an array with single element: the heights with space between them
// Output must consist of a single line: the largest sum

function largestSumOfHeights (arr) {
    let peaks = [];

    for (let i = 0; i < arr.length; i += 1) {

        // First and last element of input array will always be a peak
        if (i === 0 || i === arr.length -1) {
            peaks.push(i);
        
        // Every other element is compared to its neighbour and if its larger it means we found a new peak
        } else {
            if (arr[i] > arr[i - 1] && arr[i] > arr[i + 1]) {
                peaks.push(i);
            }
        }
    }

    let maxValleySum = 0;

    for (let i = 1; i < peaks.length; i += 1) {
        let startIndex = peaks[i-1];
        let endIndex = peaks[i];
        let valleySum = 0;

        for (let j = startIndex; j <= endIndex; j += 1) {
            valleySum += arr[j];
        }
        if (maxValleySum < valleySum) {
            maxValleySum = valleySum;
        }
    }

    console.log(maxValleySum);
}

// Peaks -> 5, 7, 6, 8

console.log(largestSumOfHeights([5, 1, 7, 4, 8])); // => returns 19

// largestSumOfHeights([5, 1, 7, 6, 5, 6, 4, 2, 3, 8]) // => returns 24
// Valleys - 5 1 7 (13); 7 6 5 6 (24); 6 4 2 3 8 (23);