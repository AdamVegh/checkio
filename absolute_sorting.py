__author__ = 'Vegh Adam'


def checkio(numbers_array):
    numbers_array = list(numbers_array)
    change = 1
    while change > 0:
        change = 0
        for i in range(len(numbers_array)-1):
            if abs(numbers_array[i]) > abs(numbers_array[i+1]):
                numbers_array[i], numbers_array[i+1] = numbers_array[i+1], numbers_array[i]
                change += 1
    return numbers_array
