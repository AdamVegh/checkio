__author__ = 'Vegh Adam'


def checkio(number):
    fact = 1
    for i in str(number):
        if i != '0':
            fact *= int(i)
    return fact
