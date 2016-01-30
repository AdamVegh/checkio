__author__ = 'Vegh Adam'

def checkio(game_result):
    count_dia1X, count_dia1O = 0, 0
    count_dia2X, count_dia2O = 0, 0
    for i in range(3):
        count_rowX, count_rowO = 0, 0
        count_colX, count_colO = 0, 0
        for j in range(3):
            # in row
            if game_result[i][j] == 'X':
                count_rowX += 1
            elif game_result[i][j] == 'O':
                count_rowO += 1
            # in column
            if game_result[j][i] == 'X':
                count_colX += 1
            elif game_result[j][i] == 'O':
                count_colO += 1
            # in main diagonal
            if (i - j) == 0 and game_result[i][j] == 'X':
                count_dia1X += 1
            elif (i - j) == 0 and game_result[i][j] == 'O':
                count_dia1O += 1
            # in second diagonal
            if (i + j) == 2 and game_result[i][j] == 'X':
                count_dia2X += 1
            elif (i + j) == 2 and game_result[i][j] == 'O':
                count_dia2O += 1
            
            if count_rowX == 3:
                return 'X'
            elif count_rowO == 3:
                return 'O'
            elif count_colX == 3:
                return 'X'
            elif count_colO == 3:
                return 'O'
            elif count_dia1X == 3:
                return 'X'
            elif count_dia1O == 3:
                return 'O'
            elif count_dia2X == 3:
                return 'X'
            elif count_dia2O == 3:
                return 'O'
    else:
        return "D"