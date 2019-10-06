let n = 185; // Outputs - 41
let resultArray = [];

nums = n.toString(10).split('').map(Number);

let x = nums[0] * nums[1] * nums[2];
let y = nums[0] + nums[1] * nums[2];
let z = nums[0] + nums[1] + nums[2];
let w = nums[0] * nums[1] + nums[2];

resultArray.push(x, y, z, w);

console.log(Math.max.apply(null, resultArray));