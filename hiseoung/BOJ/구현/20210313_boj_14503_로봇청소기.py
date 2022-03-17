import sys


def rotate(direction):
    if direction == 0:
        return 3
    elif direction == 1:
        return 0
    elif direction == 2:
        return 1
    else:
        return 2


n, m = map(int, sys.stdin.readline().split())
x, y, d = map(int, sys.stdin.readline().split())

table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
table[x][y] = 2
r_d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

while True:
    flag = 0
    for _ in range(4):
        d = rotate(d)
        if 0 <= x + r_d[d][0] < n and 0 <= y + r_d[d][1] < m and table[x + r_d[d][0]][y + r_d[d][1]] == 0:
            table[x + r_d[d][0]][y + r_d[d][1]] = 2
            x = x + r_d[d][0]
            y = y + r_d[d][1]
            flag = 1
            break

    if not flag:
        x = x - r_d[d][0]
        y = y - r_d[d][1]
        if table[x][y] == 1:
            print(sum([row.count(2) for row in table]))
            break