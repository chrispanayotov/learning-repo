let n = gets();

function add(a, b) {
    return a + b;
}

n = n.toString(10).replace(/\D/g, '0').split('').map(Number);
n = n.reduce(add, 0);

while (n > 9) {    
    n = n.toString(10).replace(/\D/g, '0').split('').map(Number);
    n = n.reduce(add, 0);
}

print(n);