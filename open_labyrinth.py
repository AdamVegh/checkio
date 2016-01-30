__author__ = 'Vegh Adam'


def more_way(lab_map, x, y):
    return "" + "N"*(lab_map[x-1][y]==0) + "E"*(lab_map[x][y+1]==0) +\
                "S"*(lab_map[x+1][y]==0) + "W"*(lab_map[x][y-1]==0)


def checkio(lab_map):
    x, y = (1, 1)
    d = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}
    memory = []
    way = [""]
    while x != 10 or y != 10:
        lab_map[x][y] = 5
        if len(more_way(lab_map, x, y)) > 1:
            memory.append([(x, y), list(more_way(lab_map, x, y))])
            direction = memory[-1][1].pop()
            x, y = memory[-1][0][0] + d[direction][0], memory[-1][0][1] + d[direction][1]
            way.append(direction)
        elif len(more_way(lab_map, x, y)) == 1:
            direction = more_way(lab_map, x, y)
            x, y = x + d[direction][0], y + d[direction][1]
            way[-1] += direction
        elif len(more_way(lab_map, x, y)) == 0:
            try:
                direction = memory[-1][1].pop()
                x, y = memory[-1][0][0] + d[direction][0], memory[-1][0][1] + d[direction][1]
                way[-1] = direction
            except IndexError:
                while not memory[-1][1]:
                    memory.pop()
                    way.pop()
                direction = memory[-1][1].pop()
                x, y = memory[-1][0][0] + d[direction][0], memory[-1][0][1] + d[direction][1]
                way[-1] = direction
    return "".join(way)
