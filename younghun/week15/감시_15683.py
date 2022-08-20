import sys
from itertools import product
from copy import deepcopy


answer = []
n, m = map(int, sys.stdin.readline().split())
office = [sys.stdin.readline().split() for _ in range(n)]
table = []
cameras = []


def zero_cnt():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if table[i][j] == '0':
                cnt += 1
    return cnt


def dfs(x, y, direction):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    if direction == 'U':
        nx = x + dx[0]
        ny = y + dy[0]
    elif direction == 'D':
        nx = x + dx[1]
        ny = y + dy[1]
    elif direction == 'L':
        nx = x + dx[2]
        ny = y + dy[2]
    elif direction == 'R':
        nx = x + dx[3]
        ny = y + dy[3]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        return
    if table[nx][ny] == '6':
        return
    if table[nx][ny] == '0':
        table[nx][ny] = '#'
    dfs(nx, ny, direction)
    return


for i in range(n):
    for j in range(m):
        if office[i][j] == '1':
            cameras.append(['U', 'D', 'L', 'R'])
        elif office[i][j] == '2':
            cameras.append(['U', 'L'])
        elif office[i][j] == '3':
            cameras.append(['U', 'D', 'L', 'R'])
        elif office[i][j] == '4':
            cameras.append(['U', 'D', 'L', 'R'])
        elif office[i][j] == '5':
            cameras.append(['U'])

cases = list(product(*cameras))

for case in cases:
    camera_num = 0
    table = deepcopy(office)
    for i in range(n):
        for j in range(m):
            if table[i][j] == '1':
                dfs(i, j, case[camera_num])
                camera_num += 1
            elif table[i][j] == '2':
                if case[camera_num] == 'U':
                    dfs(i, j, 'U')
                    dfs(i, j, 'D')
                elif case[camera_num] == 'L':
                    dfs(i, j, 'L')
                    dfs(i, j, 'R')
                camera_num += 1
            elif table[i][j] == '3':
                if case[camera_num] == 'U':
                    dfs(i, j, 'U')
                    dfs(i, j, 'R')
                elif case[camera_num] == 'D':
                    dfs(i, j, 'D')
                    dfs(i, j, 'L')
                elif case[camera_num] == 'L':
                    dfs(i, j, 'L')
                    dfs(i, j, 'U')
                elif case[camera_num] == 'R':
                    dfs(i, j, 'R')
                    dfs(i, j, 'D')
                camera_num += 1
            elif table[i][j] == '4':
                if case[camera_num] == 'U':
                    dfs(i, j, 'U')
                    dfs(i, j, 'L')
                    dfs(i, j, 'R')
                elif case[camera_num] == 'D':
                    dfs(i, j, 'D')
                    dfs(i, j, 'L')
                    dfs(i, j, 'R')
                elif case[camera_num] == 'L':
                    dfs(i, j, 'L')
                    dfs(i, j, 'U')
                    dfs(i, j, 'D')
                elif case[camera_num] == 'R':
                    dfs(i, j, 'R')
                    dfs(i, j, 'U')
                    dfs(i, j, 'D')
                camera_num += 1
            elif table[i][j] == '5':
                dfs(i, j, 'U')
                dfs(i, j, 'D')
                dfs(i, j, 'L')
                dfs(i, j, 'R')
                camera_num += 1
    answer.append(zero_cnt())

print(min(answer))

