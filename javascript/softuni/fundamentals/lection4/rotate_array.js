// Write a JS function that rotates an array. The array should be rotated 
// to the right side, meaning that the last element should become the first, upon rotation. 
// The input comes as an array of strings. The last element of the array is the
// amount of rotation you need to perform.

function rotateArray(inputArray) {
   let rotationsToDo = Number(inputArray.pop());
   let lastElement = 0;

   for (let i = 0; i < rotationsToDo; i++){
       lastElement = inputArray.pop();
       inputArray.unshift(lastElement);
   }
   console.log(inputArray.join(' '));
}

rotateArray(['1', '2', '3', '4', '2']) // => returns 3 4 1 2