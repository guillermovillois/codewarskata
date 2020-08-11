def find_it(seq):
    numbers = {}
    for each in seq:
        if each in numbers:
            numbers[each] += 1
        else:
            numbers.update({each: +1})
    for each in numbers:
        if numbers[each] % 2 != 0:
            return each


find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5])
find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5])
find_it([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5])
find_it([10])
find_it([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1])
find_it([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10])
