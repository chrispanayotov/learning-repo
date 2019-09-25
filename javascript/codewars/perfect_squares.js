// Given an integral number, determine if it's a square number

let isSquare = function(n){
    return n >= 0 && Math.sqrt(n) % 1 === 0;
}

// isSquare(-1) returns  false
// isSquare(0) returns   true
// isSquare(3) returns   false
// isSquare(4) returns   true
// isSquare(25) returns  true  
// isSquare(26) returns  false