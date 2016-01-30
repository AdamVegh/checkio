__author__ = 'Vegh Adam'


def min(*args, **kwargs):
    key = kwargs.get("key", None)
    args = sorted(args, key=key) if len(args) > 1 else sorted(args[0], key=key)
    index = 0
    min_arg = args[index]
    if not key:
        return min_arg
    while index < len(args) and list(map(key, args))[index] == list(map(key, args))[index+1]:
        index += 1
        min_arg = args[index]
    return min_arg


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    args = sorted(args, key=key) if len(args) > 1 else sorted(args[0], key=key)
    index = len(args)-1
    max_arg = args[index]
    if not key:
        return max_arg
    while index > 0 and list(map(key, args))[index] == list(map(key, args))[index-1]:
        index -= 1
        max_arg = args[index]
    return max_arg
