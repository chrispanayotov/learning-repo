let arr = '1, 2, 3, 2, 5, 2';
let target = 2;

arr = arr.split(',').map(Number);

for (let i = 1; i < arr.length; i += 1) {
    if (arr[i] === target && arr[i- 1] != target && arr[i+1] != target && i != arr.length - 1) {
            arr[i] = Math.max(arr[i-1], arr[i+1])
        }
}

console.log(`[${arr.join(', ')}]`);