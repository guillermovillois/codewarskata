var recoverSecret = function (triplets) {
    let newStr = Array.from(new Set(triplets.join(',').split(','))).join('');
    triplets.map(triplet => {
        console.log(newStr.indexOf(triplet[0]), newStr.indexOf(triplet[1]), newStr.indexOf(triplet[2]))
        // console.log(letter0, letter1, letter2)
        // triplet.map(cada =>
        //     newStr.for

        // )
    }
    )
    console.log(newStr)
    let word = '';
    triplets.map((cada, index) => {
        if (index == 0) {
            word = cada.join('')
            console.log(word)
        } else {
            for (let i = 0; i < 3; i++) {
                if (word.includes(cada[i])) {
                    console.log(cada[i])
                } else {
                    console.log('nada')
                }
            }
        }
        console.log(cada, index)

    })
    console.log(word)
}




secret1 = "whatisup"
triplets1 = [
    ['t', 'u', 'p'],
    ['w', 'h', 'i'],
    ['t', 's', 'u'],
    ['a', 't', 's'],
    ['h', 'a', 'p'],
    ['t', 'i', 's'],
    ['w', 'h', 's']
]

recoverSecret(triplets1)