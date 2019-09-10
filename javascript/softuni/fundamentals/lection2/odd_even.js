function oddOrEven(num) {
    if (num % 2 === 0 && num % 1 === 0) {
        console.log('even');
    } else if (num % 2 !== 0 && num % 1 === 0 ) {
        console.log('odd');
    } else {
        console.log('invalid');
    }
}