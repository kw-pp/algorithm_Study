from collections import deque
import sys

input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y, dir):
    q.append([x, y, dir])
    c[x][y][dir] = 1
    ans = []
    while q:
        x, y, dir = q.popleft()
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < n and 0 <= ny < n:
            if not c[nx][ny][dir] or c[nx][ny][dir] > c[x][y][dir]:
                if a[nx][ny] != '*':
                    c[nx][ny][dir] = c[x][y][dir]
                    if nx == fx and ny == fy:
                        ans.append(c[nx][ny][dir])
                        continue
                    q.append([nx, ny, dir])
                    if a[nx][ny] == '!':
                        turn(nx, ny, dir)

    print(min(ans)-1)

def turn(x, y, dir):
    ndir = [(dir+1) % 4, (dir+3) % 4]
    for d in ndir:
        if not c[x][y][d] or c[x][y][d] > c[x][y][dir] + 1:
            c[x][y][d] = c[x][y][dir] + 1
            q.append([x, y, d])

n = int(input())
q = deque()
c = [[[0]*4 for _ in range(n)] for _ in range(n)]

a, temp = [], []
for i in range(n):
    row = list(input().strip())
    a.append(row)
    for j in range(n):
        if row[j] == '#':
            temp.extend([i, j])
sx, sy, fx, fy = temp

for i in range(4):
    nx = sx + dx[i]
    ny = sy + dy[i]
    if 0 <= nx < n and 0 <= ny < n:
        if a[nx][ny] != '*':
            dir = i
            break

bfs(sx, sy, dir)
