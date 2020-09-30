def high_and_low(numbers):
    numbers = [int(x) for x in numbers.split(' ')]
    for i, each in enumerate(numbers):
        if i == 0:
            high = each
            low = each
        else:
            if each > high:
                print(each)
                high = each
            elif each < low:
                low = each
    print(low, high)


high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5")  # return "5 -3"
high_and_low("1 9 3 4 -5")  # return "9 -5"
