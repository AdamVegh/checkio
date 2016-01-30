__author__ = 'Vegh Adam'

def count_gold(pyramid):
    maxim = 0
    step = (1 << (len(pyramid)-1))
    while step < (1 << (len(pyramid))):
        index = 0
        length = 0
        for row in range(len(pyramid)):
            length += pyramid[row][index]
            index += int(bin(step)[-1-row])
        if length > maxim:
            maxim = length
        step += 1
    return maxim
