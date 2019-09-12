function oddNumsFilter(n) {
    let oddNums = [];

    for (let i = 0; i <= n; i++) {
        if (i % 2 !== 0) {
            oddNums.push(i);
        }
    }

    for (let num of oddNums) {
        console.log(num);
    }
}