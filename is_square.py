import math


def is_square(n):
    print((math.sqrt(n)).is_integer() if n >= 0 else False)


is_square(-1)
is_square(0)
is_square(3)
is_square(4)
is_square(25)
is_square(26)
