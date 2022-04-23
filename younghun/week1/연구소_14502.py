import sys
from itertools import combinations
from copy import deepcopy


def virus(row, col):
    if row > 0 and map_lab[row - 1][col] == 0:
        map_lab[row - 1][col] = 2
        virus(row - 1, col)
    if row < N - 1 and map_lab[row + 1][col] == 0:
        map_lab[row + 1][col] = 2
        virus(row + 1, col)
    if col > 0 and map_lab[row][col - 1] == 0:
        map_lab[row][col - 1] = 2
        virus(row, col - 1)
    if col < M - 1 and map_lab[row][col + 1] == 0:
        map_lab[row][col + 1] = 2
        virus(row, col + 1)

    return


def safe_spot():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if map_lab[i][j] == 0:
                cnt += 1

    return cnt


N, M = map(int, sys.stdin.readline().split())

lab_map = []
result = []

for _ in range(N):
    lab_map.append(list(map(int, sys.stdin.readline().split())))

spot = []
for i in range(N):
    for j in range(M):
        if lab_map[i][j] == 0:
            spot.append([i, j])

cases = list(combinations(spot, 3))

for case in cases:
    map_lab = deepcopy(lab_map)

    for i in case:
        map_lab[i[0]][i[1]] = 1

    for i in range(N):
        for j in range(M):
            if map_lab[i][j] == 2:
                virus(i, j)

    result.append(safe_spot())

print(max(result))
