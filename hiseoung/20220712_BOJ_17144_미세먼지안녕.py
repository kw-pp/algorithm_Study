import sys
from collections import deque
input = sys.stdin.readline

R, C, T = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(R)]
robot = []
dust = deque([])
answer = 0

# 0: 동, 1: 북, 2: 서, 3:남
def rotate(x, y, d):
    if d == 0:
        return x-1, y, 1
    elif d == 1:
        return x, y-1, 2
    elif d == 2:
        return x+1, y, 3
    else:
        return x, y+1, 0

def rotate_reverse(x, y, d):
    if d == 0:
        return x+1, y, 3
    elif d == 1:
        return x, y+1, 0
    elif d == 2:
        return x-1, y, 1
    else:
        return x, y-1, 2

def move(x, y, d):
    if d == 0:
        return x, y+1, 0
    elif d == 1:
        return x-1, y, 1
    elif d == 2:
        return x, y-1, 2
    else:
        return x+1, y, 3

for _ in range(T):
    # 1. 미세먼지 확산
    for i in range(R):
        for j in range(C):
            if table[i][j] == -1:
                robot.append((i, j))
                continue
            if table[i][j] != 0:
                temp = table[i][j] // 5
                dust.append((i, j, table[i][j], temp))

    while dust:
        x, y, val, k = dust.popleft()
        count = 0
        for a, b in (1, 0), (0, 1), (-1, 0), (0, -1):
            if 0 <= x+a < R and 0 <= y+b < C and table[x+a][y+b] != -1:
                table[x+a][y+b] += k
                count += 1
        table[x][y] = (table[x][y] - (count * k))

    next_x, next_y = robot.pop()
    prev_x, prev_y = robot.pop()

    x, y, d = move(prev_x, prev_y, 0)
    q = deque([])
    q.append(table[x][y])
    table[x][y] = 0

    # 2. 공기청정기 확산
    while True:
        nx, ny, nd = move(x, y, d)
        if nx == prev_x and ny == prev_y:
            break
        if 0 <= nx < R and 0 <= ny < C:
            q.append(table[nx][ny])
            table[nx][ny] = q.popleft()
            x, y, d = nx, ny, nd
        else:
            nx, ny, nd = rotate(x, y, d)
            q.append(table[nx][ny])
            table[nx][ny] = q.popleft()
            x, y, d = nx, ny, nd

    x, y, d = move(next_x, next_y, 0)
    q = deque([])
    q.append(table[x][y])
    table[x][y] = 0

    while True:
        nx, ny, nd = move(x, y, d)
        if nx == next_x and ny == next_y:
            break
        if 0 <= nx < R and 0 <= ny < C:
            q.append(table[nx][ny])
            table[nx][ny] = q.popleft()
            x, y, d = nx, ny, nd
        else:
            nx, ny, nd = rotate_reverse(x, y, d)
            q.append(table[nx][ny])
            table[nx][ny] = q.popleft()
            x, y, d = nx, ny, nd

for i in range(R):
    for j in range(C):
        if table[i][j] != -1:
            answer += table[i][j]

print(answer)