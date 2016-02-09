__author__ = 'Vegh Adam'


def left_join(phrases):
    return ",".join([word.replace("right", "left") for word in phrases])
