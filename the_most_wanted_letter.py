__author__ = 'Vegh Adam'

def checkio(text):
    text = text.lower()
    dict_letters = {}
    for letter in text:
        if letter.isalpha():
            dict_letters[letter] = dict_letters.get(letter, 0) + 1
    tup_letters = sorted(dict_letters.items())
    letter = tup_letters[0]
    mwl = letter[0]
    for item in tup_letters:
        if item[1] > letter[1]:
            letter = item
            mwl = letter[0]
    return mwl