// Create a function that takes a list of non-negative integers and strings 
// and returns a new list with the strings filtered out.


function filter_list(l) {
    let filteredArray = [];

    for (let char of l) {

        if (typeof(char) === 'number') {
            filteredArray.push(char);
        }

    }
    return filteredArray;
  }

filter_list([1,2,'a','b']) // => returns [1,2]
filter_list([1,'a','b',0,15]) // => returns [1,0,15]
filter_list([1,2,'aasf','1','123',123]) // => returns [1,2,123]

// Other coders solution

function filter_list(l) {
    return l.filter(function(v) {return typeof v == 'number'})
  }