# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.


def move_zeros(array):
    other = []
    zeros = []
    for i, each in enumerate(array):
        if each == 0 and not isinstance(each, bool):
            zeros.append(each)
        else:
            other.append(each)

    print(other + zeros)


move_zeros([False, 1, 0, 1, 2, 0, 1, 3, "a"])
move_zeros(['a', 'b', None, 'c', 'd', 1, 1, 3, [], 1, 9,
            {}, 9, 0, 0, 0, False, 0, 0, 0, 0, 0, 0, 0])
