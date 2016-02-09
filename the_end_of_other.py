__author__ = 'Vegh Adam'


def checkio(words_set):
    for word in list(words_set):
        for ending in list(words_set):
            if word.endswith(ending) and (list(words_set).index(word) != list(words_set).index(ending)):
                return True
    return False
