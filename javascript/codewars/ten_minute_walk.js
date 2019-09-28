// You live in the city of Cartesia where all roads are laid out in a perfect grid. 
// You arrived ten minutes too early to an appointment, so you decided to 
// take the opportunity to go for a short walk. The city provides its citizens with
// a Walk Generating App on their phones -- everytime you press the button it 
// sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). 
// You always walk only a single block in a direction and you know it takes you 
// one minute to traverse one city block, so create a function that will return true 
// if the walk the app gives you will take you exactly ten minutes 
// (you don't want to be early or late!) and will, of course, 
// return you to your starting point. Return false otherwise.

// Note: you will always receive a valid array containing a random assortment of 
// direction letters ('n', 's', 'e', or 'w' only). It will never give you an 
// empty array (that's not a walk, that's standing still!).

function isValidWalk(walk) {
    let walkDuration = 0;
    let currentPosition = {'n': 0, 'w': 0};

    for (let direction of walk) {

        if (direction === 'n') {
            currentPosition['n'] += 1;
        } else if (direction === 's') {
            currentPosition['n'] -= 1;
        }

        if (direction === 'w') {
            currentPosition['w'] += 1;
        } else if (direction === 'e') {
            currentPosition['w'] -= 1;
        }
        
        walkDuration++;
    }
    
    return (currentPosition['n'] === 0 && currentPosition['w'] === 0 && walkDuration === 10);
}

// Should return false, because walk duration is > 10 minutes;
console.log(isValidWalk(['w','e','w','e','w','e','w','e','w','e','w','e'])); 

isValidWalk(['n','s','n','s','n','s','n','s','n','s']) // 'should return true'
isValidWalk(['w','e','w','e','w','e','w','e','w','e','w','e']) // 'should return false'
isValidWalk(['w']) // 'should return false'
isValidWalk(['n','n','n','s','n','s','n','s','n','s']) // 'should return false'
