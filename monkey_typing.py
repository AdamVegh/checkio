__author__ = 'Vegh Adam'

def count_words(text, words):
    return len(list(filter(lambda word: word in text.lower(), words)))
