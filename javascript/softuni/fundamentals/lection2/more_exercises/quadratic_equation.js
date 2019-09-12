function quadEquation(a, b, c) {
    // Calculating the discriminant and roots
    let d = Math.pow(b, 2) - 4 * a * c;

    let x1 = (-b + Math.sqrt(d)) / (2 * a);
    let x2 = (-b - Math.sqrt(d)) / (2 * a);

    // If discrimant is > 0 then print both real roots in ascending order
    // If discrimant is = 0 then print the one real root
    // In any other case the equation has no real roots

    if (d > 0) {
        console.log(Math.min(x1, x2));
        console.log(Math.max(x1, x2));
    } else if (d === 0) {
        console.log(x1);
    } else {
        console.log('No');
    }
}