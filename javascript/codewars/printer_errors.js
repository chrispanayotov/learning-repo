// In a factory a printer prints labels for boxes. For one kind of boxes the 
// printer has to use colors which, for the sake of simplicity, 
// are named with letters from a to m. 

// If the string consists letter above m it counts towards a printing error
// Print the number of errors and length of printing job

function printerError(s) {
    let printingJobLength = s.length;
    let errorsCount = 0;

    for (let char of s) {
        if (char.charCodeAt(0) > 109) {
            errorsCount++;
        }
    }
    
    return `${errorsCount}` + '/' + `${printingJobLength}`;
}

console.log(printerError('aaaxbbbbyyhwawiwjjjwwm')); // => returns '8/22'