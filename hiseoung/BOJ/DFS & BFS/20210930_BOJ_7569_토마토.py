import sys
from collections import deque
'''
    출처 : https://www.acmicpc.net/problem/7569
    유형 : BFS
    티어 : 실버 1

'''
m, n, h = map(int, sys.stdin.readline().strip().split())
tomato = []
is_visited = [[[False for i in range(m)] for j in range(n)] for k in range(h)]
count = 0
check = 0
for i in range(h):
    height = []
    for j in range(n):
        height.append(list(map(int, sys.stdin.readline().strip().split())))
    tomato.append(height)

q = deque()
for hh in range(len(tomato)):
    for nn in range(len(tomato[hh])):
        for mm in range(len(tomato[hh][nn])):
            if tomato[hh][nn][mm] == 1:
                q.append([hh, nn, mm])
                is_visited[hh][nn][mm] = True
            elif tomato[hh][nn][mm] == 0:
                check += 1

if check == 0:
    print(0)
else:
    while q:
        for _ in range(len(q)):
            x, y, z = q.popleft()
            for a, b, c in (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1):
                if 0 <= x+a < h and 0 <= y+b < n and 0 <= z+c < m and not is_visited[x+a][y+b][z+c]:
                    if tomato[x+a][y+b][z+c] == 0:
                        is_visited[x+a][y+b][z+c] = True
                        tomato[x+a][y+b][z+c] = 1
                        q.append([x+a, y+b, z+c])
        count += 1

    is_tomato = 0
    for h in range(len(tomato)):
        if is_tomato:
            break
        for n in range(len(tomato[h])):
            if is_tomato:
                break
            for m in range(len(tomato[h][n])):
                if tomato[h][n][m] == 0:
                    is_tomato = 1
                    break

    if is_tomato:
        print(-1)
    else:
        print(count-1)


