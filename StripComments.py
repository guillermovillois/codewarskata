def solution(string, markers):
    lista = string.split('\n')
    for i, each in enumerate(lista):
        for marker in markers:
            each = each.split(marker)[0]
        lista[i] = each
    print('\n'.join(lista))


# result = solution(
#     "apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
solution('cherries strawberries cherries ? oranges =\npears avocados\nbananas\n! pears bananas\n.', [
         '?', '^', '@', '!', '#'])
