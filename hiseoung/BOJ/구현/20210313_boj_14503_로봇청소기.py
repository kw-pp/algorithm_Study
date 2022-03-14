import sys
from collections import deque


def dfs(x, y, d):
    print(0)
    global flag
    if flag:
        print(1)
        return
    if d > 3:
        d = d - 4
    for _ in range(4):
        if d > 3:
            d = d - 4
        if table[x + r_d[d][0]][y + r_d[d][1]] == 0:
            print((x + r_d[d][0], y + r_d[d][1]))
            print("현재 d : ", d)
            table[x + r_d[d][0]][y + r_d[d][1]] = 2
            dfs(x + r_d[d][0], y + r_d[d][1], d+1)
            if table[x + r_d[abs(d - 2)][0]][y + r_d[abs(d - 2)][1]] == 1:
                if d + 1 > 3:
                    f = 0
                else:
                    f = d + 1
                if d - 1 < 0:
                    s = 3
                else:
                    s = d - 1
                if table[x + r_d[f][0]][y + r_d[f][1]] == 2 and table[x + r_d[s][0]][y + r_d[s][1]] == 2:
                    flag = 1
                    print(2)
                    break

        print("d : ", d)
        print(3)
        d += 1
    print(4)




n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())

table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
table[r][c] = 2
flag = 0
# 0 : 북, 1 : 동, 2 : 남, 3: 서
r_d = [(0, -1), (1, 0), (0, 1), (-1, 0)]
dfs(r, c, d)

print(sum([row.count(2) for row in table]))
