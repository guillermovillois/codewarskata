def solution(s):
    if len(s) > 0:
        lista = ["".join(list(s)[i:i + 2]) for i in range(0, len(list(s)), 2)]
        if len(lista[-1]) != 2:
            lista[-1] = lista[-1]+'_'
        print(lista)


solution('abc')  # should return ['ab', 'c_']
solution('abcdef')  # should return ['ab', 'cd', 'ef']
solution('x')
