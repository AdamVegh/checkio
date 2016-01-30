__author__ = 'Vegh Adam'

def count_neighbours(grid, row, col):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (0 <= row + i <= (len(grid) - 1)) and (0 <= col + j <= (len(grid[0]) - 1)) and not (i == 0 and j == 0):
                count += grid[row + i][col + j]
    return count