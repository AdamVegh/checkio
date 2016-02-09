__author__ = 'Vegh Adam'


def checkio(first, second):
    cw = []
    for w1 in first.split(','):
        for w2 in second.split(','):
            if w1 == w2:
                cw.append(w1)
    return ','.join(sorted(cw))
