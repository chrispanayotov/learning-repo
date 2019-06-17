function distPoints (x1, y1, x2, y2) {
    let pointOne = {
        x: x1,
        y: y1
    };
    let pointTwo = {
        x: x2,
        y: y2
    };
    let distA = Math.abs(pointOne.x - pointTwo.x);
    let distB = Math.abs(pointOne.y - pointTwo.y);
    let total = Math.sqrt(Math.pow(distA, 2) + Math.pow(distB, 2));

    return total;
}