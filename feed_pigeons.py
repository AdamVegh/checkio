__author__ = 'Vegh Adam'

def checkio(number):
    list_bird = []
    i = 0
    while True:
        i += 1
        for j in range(i):
            list_bird.append(0)
        for k in range(len(list_bird)):
            list_bird[k] += 1
            number -= 1
            if number == 0:
                break
        if number == 0:
            break
    bird = 0
    for l in list_bird:
        if l > 0:
            bird += 1
    return bird