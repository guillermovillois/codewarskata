function goodVsEvil(good, evil) {
    let Gd = [1, 2, 3, 3, 4, 10]
    let Evl = [1, 2, 2, 2, 3, 5, 10]
    let goodNumber = (good.split(' ').map((element, index) => Gd[index] * element).reduce(function (a, b) {
        return a + b;
    }, 0))
    let evilNumber = (evil.split(' ').map((element, index) => Evl[index] * element).reduce(function (a, b) {
        return a + b;
    }, 0))

    if (goodNumber > evilNumber) {
        console.log("Battle Result: Good triumphs over Evil");
    } else if (goodNumber < evilNumber) {
        console.log("Battle Result: No victor on this battle field");
    } else {
        console.log('Battle Result: No victor on this battle field');
    }
}


goodVsEvil('1 0 0 0 0 0', '1 0 0 0 0 0 0')
goodVsEvil('0 0 0 0 0 10', '0 1 1 1 1 0 0')
goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1')