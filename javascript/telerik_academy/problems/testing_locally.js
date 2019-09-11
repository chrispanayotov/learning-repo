const getGets = (arr) => {
    let index = 0;

    return () => {
        const toReturn = arr[index];
        index += 1;
        return toReturn;
    };
};

// Place input in test array

const test = [
    5
];

const get = this.gets || getGets(test);
const print = this.print || console.log();

// For numbers
const n = +gets();

// For strings and arrays
const line = gets();

// Write Solution below

