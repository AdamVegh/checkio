__author__ = 'Vegh Adam'

check_pangram = lambda x: len(set([c for c in x if 'a' <= c.lower() <= 'z'])) == ord('z')-ord('a')+1
