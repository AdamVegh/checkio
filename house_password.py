__author__ = 'Vegh Adam'

def checkio(data):
    if len(data) < 10:
        return False
    is_digit, is_upper, is_lower = 0, 0, 0
    for i in data:
        if i.isdigit():
            is_digit += 1
        elif i.isupper():
            is_upper += 1
        elif i.islower():
            is_lower += 1
    return is_digit * is_upper * is_lower
