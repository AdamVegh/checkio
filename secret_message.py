__author__ = 'Vegh Adam'

def find_message(text):
    return ''.join(list(filter(lambda s: s.isupper(), text)))
