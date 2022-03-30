import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
target = [0]
cand = deque([(i, j) for i in range(N) for j in range(i % 2, N, 2)])
answer = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    start = (x, y)

    queue = deque()
    queue.append(start)

    local_visited = [start]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if (nx, ny) in local_visited:
                continue

            if L <= abs(table[x][y] - table[nx][ny]) <= R:
                local_visited.append((nx, ny))
                visited[nx][ny] = True
                queue.append((nx, ny))

    if len(local_visited) == 1:
        return []

    return local_visited


while target:
    target = []
    visited = [[False] * N for _ in range(N)]

    for _ in range(len(cand)):
        i, j = cand.popleft()
        if not visited[i][j]:
            new_target = bfs(i, j)
            if new_target:
                target.append(new_target)

    if target:
        for i in target:
            sum_val = 0

            for x, y in i:
                sum_val += table[x][y]

            for x, y in i:
                table[x][y] = sum_val // len(i)
                cand.append((x, y))  # 인구이동이 일어났던 곳만 살펴보면 된다.

        answer += 1

print(answer)
