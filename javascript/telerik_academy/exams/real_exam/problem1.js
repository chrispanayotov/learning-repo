let nTargets = +gets();
let gS = +gets(); // Goshos speed
let gL = +gets(); // Goshos latency
let pS = +gets(); // Peshos speed
let pL = +gets(); // Peshos latency

function solve (targets, gS, gL, pS, pL) {
    let speed;
    
    function calcGosho(gS, gL) {
        speed = targets * gS + gL + gL;
        return speed;
    }

    function calcPesho(pS, pL) {
        speed = targets * pS + pL + pL;
        return speed;
    }

    let resultGosho = calcGosho(gS, gL);
    let resultPesho = calcPesho(pS, pL);

    if (resultGosho < resultPesho) {
        print('George');
    } else if (resultPesho < resultGosho) {
        print('Peter');
    } else {
        print('Draw');
    }
}

solve(nTargets, gS, gL, pS, pL);