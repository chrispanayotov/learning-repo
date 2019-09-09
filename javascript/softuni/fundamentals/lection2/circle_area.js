function circleArea(radius) {
    let result = Math.PI * radius * radius;
    console.log(result);

    return result.toFixed(2);
}

console.log(circleArea(5))