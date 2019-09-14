// Write a program that allocates array of N integers, initializes each element 
// by its index multiplied by 5 and the prints the obtained array on the console.

const n = +get();
let resultArray = [];
let i = 0;

while (i < n) {
    resultArray[i] = i * 5;
    print(resultArray[i++]);
}