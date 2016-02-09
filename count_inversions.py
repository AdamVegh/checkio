__author__ = 'Vegh Adam'


def count_inversion(values):
    count = 0
    for i in range(len(values)-1):
        for j in range(i+1, len(values)):
            if values[j] < values[i]:
                count += 1
    return count
