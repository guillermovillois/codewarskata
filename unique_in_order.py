def unique_in_order(valor):
    lista = []
    for index, each in enumerate(valor):
        if (valor[index-1] != each or index == 0):
            lista.append(each)
    print(lista)


unique_in_order('A')
