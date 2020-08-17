from itertools import chain


def namelist(names):
    nueva = list(chain(* [each.values() for each in names]))
    valor = ''
    for i in range(0, len(nueva)):
        if len(nueva)-i > 2:
            valor += nueva[i]+', '
        elif (len(nueva)-i) > 1:
            valor += nueva[i]+' & '
        else:
            valor += nueva[i]
    return valor


namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}])
# returns 'Bart, Lisa & Maggie'

namelist([{'name': 'Bart'}, {'name': 'Lisa'}])
# returns 'Bart & Lisa'

namelist([{'name': 'Bart'}])
# returns 'Bart'

namelist([])
# returns ''
