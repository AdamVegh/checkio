__author__ = 'Vegh Adam'


def checkio(data):
    a = {}
    for i in data:
        a[i] = a.get(i,0) + 1
    for i in a:
        if a[i] == 1:
            data.remove(i)
    return data
