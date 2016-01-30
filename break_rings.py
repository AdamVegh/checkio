__author__ = 'Vegh Adam'


from itertools import combinations

def break_rings(rings):
    to_break = 0
    list_rings = list(rings)
    while list_rings:
        to_break += 1
        a = list(combinations(range(1,len(set.union(*rings))+1), to_break))
        for i in a:
            list_rings = list(rings)
            for n in i:
                list_rings = list(filter(lambda x: n not in x, list_rings))
                if not list_rings:
                    return to_break
