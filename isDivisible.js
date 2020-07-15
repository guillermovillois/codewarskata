function isDivisible(n, x, y) {
    return 0 == (n % x + n % y);
}

isDivisible(3, 3, 4);
isDivisible(12, 3, 4);
isDivisible(8, 3, 4);
isDivisible(48, 3, 4);