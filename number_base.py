__author__ = 'Vegh Adam'


def checkio(str_number, radix):
    num = 0
    for i in range(len(str_number)):
        if str_number[i].isalpha() and (ord(str_number[i])-55 < radix):
            ch_num = ord(str_number[i]) - 55
        elif str_number[i].isdigit() and int(str_number[i]) < radix:
            ch_num = int(str_number[i])
        else:
            return -1
        num += ch_num * radix ** (len(str_number)-1-i)
    return num
