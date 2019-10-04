// Write a JS function that adds and removes numbers to / from an array. 
// You will receive a command which can either be “add” or “remove”. 

function addRemoveElements(inputArray) {
    let resultArray = [];
    let counter = 0;

    for (let i = 1; i <= inputArray.length; i++) {
        if (inputArray[counter] === 'add') {
            resultArray.push(i);
        } else {
            resultArray.pop();
        }
        counter++;
    }

    if (resultArray.length === 0) {
        console.log('Empty');
    } else {
        for (let num of resultArray) {
            console.log(num);
        }
    }
}

addRemoveElements(['add', 'add', 'remove', 'add', 'add']); // returns 1, 4, 5