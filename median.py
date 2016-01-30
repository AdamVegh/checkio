__author__ = "Vegh Adam"

def checkio(data):
    data.sort()
    if len(data) % 2 == 0:
        med = (data[(len(data)-1) // 2] + data[(len(data)-1) // 2 + 1]) / 2
    else:
        med = data[(len(data)-1) // 2]
    return med
