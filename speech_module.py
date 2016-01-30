__author__ = 'Vegh Adam'

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    string = []
    if number//100 > 0:
        string.append(FIRST_TEN[number//100 - 1] + ' ' + HUNDRED)
    number %= 100
    if number//10 == 1:
        number %= 10
        string.append(SECOND_TEN[number])
    elif number//10 > 1:
        string.append(OTHER_TENS[number//10 - 2])
        number %= 10
        if number > 0:
            string.append(FIRST_TEN[number - 1])
    else:
        number %= 10
        if number > 0:
            string.append(FIRST_TEN[number - 1])
    return ' '.join(string)
