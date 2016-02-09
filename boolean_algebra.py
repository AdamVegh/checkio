__author__ = 'Vegh Adam'

OP_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")


def boolean(x, y, op):
    if op == OP_NAMES[0]:
        return x & y
    elif op == OP_NAMES[1]:
        return x | y
    elif op == OP_NAMES[2]:
        return (1*(not x)) | y
    elif op == OP_NAMES[3]:
        return x ^ y
    elif op == OP_NAMES[4]:
        return ((1*(not x)) | y) & (x | (1*(not y)))
