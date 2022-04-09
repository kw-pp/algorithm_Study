from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
arr = []
red_x, red_y = 0, 0
blue_x, blue_y = 0, 0
for i in range(N):
    arr.append(list(input().strip()))
    for j in range(len(arr[i])):
        if arr[i][j] == 'R':
            red_x, red_y = i, j
            arr[i][j] = '.'
        elif arr[i][j] == 'B':
            blue_x, blue_y = i, j
            arr[i][j] = '.'
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def move(x, y, dx, dy):
    nx, ny = x, y
    moving = 0
    while True:
        if arr[nx+dx][ny+dy] != '#' and arr[nx+dx][ny+dy] != 'O':
            nx += dx
            ny += dy
            moving += 1
        else:
            break
    return nx, ny, moving


def bfs():
    q = deque()
    q.append((red_x, red_y, blue_x, blue_y, 0))
    while q:
        x, y, a, b, count = q.popleft()
        if count > 10:
            continue
        for k in range(4):
            nx, ny, Rmove = move(x, y, dx[k], dy[k])
            na, nb, Bmove = move(a, b, dx[k], dy[k])

            if arr[na+dx[k]][nb+dy[k]] == 'O':
                continue
            if arr[nx+dx[k]][ny+dy[k]] == 'O' and count < 10:
                return (count+1)

            if nx == na and ny == nb:
                if Rmove > Bmove:
                    nx -= dx[k]
                    ny -= dy[k]
                else:
                    na -= dx[k]
                    nb -= dy[k]
            if x == nx and y == ny and na == a and nb == b:
                continue
            q.append((nx, ny, na, nb, count+1))
    return -1


result = bfs()
print(result)
