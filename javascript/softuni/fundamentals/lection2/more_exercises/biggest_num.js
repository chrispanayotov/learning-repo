function maxNum(array) {
    let max = -99999999999999;

    for (let num of array) {

        if (num > max) {
            max = num;
        }
        
    }
    return max;
}