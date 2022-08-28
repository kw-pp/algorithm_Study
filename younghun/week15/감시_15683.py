from itertools import product
from copy import deepcopy

n, m = map(int, input().split())
office, cctv, camera_num = [], [], 0

for _ in range(n):
    office.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if office[i][j]:
            camera_num += 1
        if 1 <= office[i][j] <= 5:
            cctv.append((i, j))
direction = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
temp, max_cnt = [], 0

for x, y in cctv:
    temp.append(direction[office[x][y]])

for prod in list(product(*temp)):
    cnt = 0
    table = deepcopy(office)

    for i in range(len(cctv)):
        for d in prod[i]:
            t, s = cctv[i][0], cctv[i][1]
            while True:
                nx, ny = t + dx[d], s + dy[d]
                if nx < 0 or nx >= n or ny < 0 or ny >= m or office[nx][ny] == 6:
                    break
                if table[nx][ny] == 0:
                    table[nx][ny] = 7
                    cnt += 1
                t, s = nx, ny
    max_cnt = max(max_cnt, cnt)
print(n * m - camera_num - max_cnt)
