import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split())
table = [[*input().strip()] for _ in range(n)]
is_visited = [[False] * m for _ in range(n)]
_wolf, _ship = 0, 0


def bfs(x, y):
    wolf, ship = 0, 0
    q = deque([(x, y)])
    if table[x][y] == 'v':
        wolf += 1
    elif table[x][y] == 'k':
        ship += 1
    is_visited[x][y] = True

    while q:
        x, y = q.popleft()
        for a, b in (1, 0), (0, 1), (-1, 0), (0, -1):
            nx = x + a
            ny = y + b
            if 0 <= nx < n and 0 <= ny < m and not is_visited[nx][ny] and table[nx][ny] != '#':
                q.append((nx, ny))
                is_visited[nx][ny] = True
                if table[nx][ny] == 'v':
                    wolf += 1
                elif table[nx][ny] == 'k':
                    ship += 1
    return (wolf, False) if wolf >= ship else (ship, True)


for i in range(n):
    for j in range(m):
        if not is_visited[i][j] and table[i][j] != '#':
            val = bfs(i, j)
            if val[1]:
                _ship += val[0]
            else:
                _wolf += val[0]

print(_ship, _wolf)

