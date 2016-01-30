__author__ = 'Vegh Adam'

def flatten(dictionary):
    stack = [((), dictionary)]
    result = {}
    while stack:
        path, current = stack.pop()
        for k in current:
            if isinstance(current[k], dict):
                stack += [(path + (k,), current[k])]
            else:
                result["/".join((path + (k,)))] = current[k]
        if len(current) == 0:
            result["/".join(path)] = ""
    return result