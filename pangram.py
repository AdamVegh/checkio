__author__ = 'Vegh Adam'


def check_pangram(text):
    # Creating a dict of ASCII letters
    letters = {}
    for i in range(ord('a'), ord('z')+1):
        letters[chr(i)] = letters.get(chr(i), 0) + 1
    letters = sorted(letters.items())
    # Creating a dict of text letters
    text = text.lower()
    count = {}
    for i in text:
        if i.isalpha():
            count[i] = count.get(i, 0) + 1
    count = sorted(count.items())
    return False if len(count) != len(letters) else True
