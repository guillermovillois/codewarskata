
def solution(num):

    roman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
             50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    # roman = OrderedDict(False)
    # print()

    def roman_num(num):
        for r in list(reversed(sorted(roman.keys()))):
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num <= 0:
                break

    print("".join([a for a in roman_num(num)]))


solution(1)
solution(4)
solution(6)
solution(14)
solution(21)
solution(89)
solution(91)
solution(984)
solution(1000)
solution(1889),
solution(1989)
