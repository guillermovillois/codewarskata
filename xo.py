def xo(s):
    s = s.lower()
    lista = [char for char in s]
    if all(x in lista for x in ['x', 'o']):
        print(lista.count('x') == lista.count('o'))
    elif any(x in lista for x in ['x', 'o']):
        print(False)
    else:
        print(True)


xo('xo')
xo('xo0')
xo('xxxoo')
print(not xo("zpzpzpp"))
