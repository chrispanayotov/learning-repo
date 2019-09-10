let fruits = [
    'banana',
    'apple',
    'kiwi',
    'cherry',
    'lemon',
    'grapes',
    'peach',
];

let vegetables = [
    'tomato',
    'cucumber',
    'pepper',
    'onion',
    'garlic',
    'parsley',
];

function fruitOrVeggie(item) {
    if (fruits.indexOf(item) > -1) {
        return 'fruit';
    } else if (vegetables.indexOf(item) > -1) {
        return 'vegetable';
    }
    return 'unknown';
}

// Switch Case solution

function food(item) {
    switch (item) {
        case 'banana':
        case 'apple':
        case 'kiwi':
        case 'cherry':
        case 'lemon':
        case 'grapes':
        case 'peach':
            console.log('fruit'); break;
        case 'tomato':
        case 'cucumber':
        case 'pepper':
        case 'onion':
        case 'parsley':
        case 'garlic':
            console.log('vegetable'); break;
        default:
            console.log('unknown');
    }
}