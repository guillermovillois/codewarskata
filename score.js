function score(dice) {
    // Fill me in!
    let sides = {};
    let suma = 0;
    for (i in dice) {
        let num = dice[i];
        sides[num] = sides[num] ? sides[num] + 1 : 1;
    }
    Object.keys(sides).forEach((value) => {
        if (value == 1) {
            (sides[value] >= 3) ? suma += 1000 + (sides[value] - 3) * 100 : suma += sides[value] * 100;
        } else if (value == 5) {
            (sides[value] >= 3) ? suma += 500 + (sides[value] - 3) * 10 : suma += sides[value] * 50;
        } else if (sides[value] >= 3) {
            suma += value * 100;
        }
    })
    console.log(suma)
}

score([4, 4, 4, 3, 3, 1, 1, 1, 1, 5, 9])
score([2, 3, 4, 6, 2])
score([2, 4, 4, 5, 4])
score([4, 4, 4, 3, 3])