def same_structure_as(original, other):
    # your code here


    # should return True
same_structure_as([1, 1, 1], [2, 2, 2])
same_structure_as([1, [1, 1]], [2, [2, 2]])

# should return False
same_structure_as([1, [1, 1]], [[2, 2], 2])
same_structure_as([1, [1, 1]], [[2], 2])

# should return True
same_structure_as([[[], []]], [[[], []]])

# should return False
same_structure_as([[[], []]], [[1, 1]])
