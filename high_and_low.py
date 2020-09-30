def high_and_low(numbers):
    numbers = [int(x) for x in numbers.split(' ')]
    print('%x %x' % (max(numbers), min(numbers)))


high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5")  # return "5 -3"
high_and_low("1 9 3 4 -5")  # return "9 -5"
