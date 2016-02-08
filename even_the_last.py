__author__ = 'Vegh Adam'

def checkio(array):
    if array == []:
        return 0
    else:
        count = 0
        for i in range(len(array)):
            if i % 2 == 0:
                count += array[i]
        return count * array[len(array)-1]
