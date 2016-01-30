__author__ = 'Vegh Adam'

def checkio(data):
    roman = ''
    if 0 < (data//1000) <= 3:
        roman += ('M' * (data//1000))
    data %= 1000
    if 0 < (data//100) <= 3:
        roman += ('C' * (data//100))
    elif (data//100) == 4:
        roman += 'CD'
    elif 4 < (data//100) <= 8:
        roman += ('D' + 'C' * ((data//100) % 5))
    elif (data//100) == 9:
        roman += 'CM'
    data %= 100
    if 0 < (data//10) <= 3:
        roman += ('X' * (data//10))
    elif (data//10) == 4:
        roman += 'XL'
    elif 4 < (data//10) <= 8:
        roman += ('L' + 'X' * ((data//10) % 5))
    elif (data//10) == 9:
        roman += 'XC'
    data %= 10
    if 0 < data <= 3:
        roman += ('I' * data)
    elif data == 4:
        roman += 'IV'
    elif 4 < data <= 8:
        roman += ('V' + 'I' * (data % 5))
    elif data == 9:
        roman += 'IX'
    return roman