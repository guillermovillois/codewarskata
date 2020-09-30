function nextBigger(n) {
    let lista = n.toString().split('')
    // console.log(lista)
    lista.map((each) => {
        // console.log(each)
    })
    //your code here



    function allPossibleCases(arr) {
        if (arr.length == 1) {
            return arr[0];
        } else {
            var result = [];
            var allCasesOfRest = allPossibleCases(arr.slice(1));  // recur with the rest of array
            for (var i = 0; i < allCasesOfRest.length; i++) {
                for (var j = 0; j < arr[0].length; j++) {
                    result.push(arr[0][j] + allCasesOfRest[i]);
                }
            }
            return result;
        }

    }
    console.log(allPossibleCases(lista))
}


nextBigger(12)
nextBigger(513)
nextBigger(2017)
nextBigger(414)
nextBigger(144)