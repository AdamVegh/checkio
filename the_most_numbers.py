__author__ = 'Vegh Adam'

def checkio(*args):
    return max(args) - min(args) if len(list(args)) != 0 else 0
