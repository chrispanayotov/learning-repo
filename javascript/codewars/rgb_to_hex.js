// Create a function that converts RGB decimal values to hexadecimal
// The valid decimal values for RGB are 0 - 255. Any (r,g,b) argument values that 
// fall out of that range should be rounded to the closest valid value. 

function rgb(r, g, b) {
    r = Math.max(0, Math.min(255, r));
    g = Math.max(0, Math.min(255, g));
    b = Math.max(0, Math.min(255, b));

    function componentToHex(color) {
        let hex = color.toString(16).toUpperCase();
        return hex.length == 1 ? "0" + hex : hex;
    }

    return componentToHex(r) + componentToHex(g) + componentToHex(b);
}

rgb(255, 255, 255) // returns FFFFFF
rgb(255, 255, 300) // returns FFFFFF
rgb(0,0,0) // returns 000000
rgb(148, 0, 211) // returns 9400D3
rgb(-20, 0, 0) // returns 000000