__author__ = 'Vegh Adam'

def safe_pawns(pawns):
    safe = 0
    for i in list(pawns):
        for j in list(pawns):
            if (int(j[1])==(int(i[1])-1)) and (j[0]==chr(ord(i[0])-1) or j[0]==chr(ord(i[0])+1)):
                safe += 1
                break
    return safe