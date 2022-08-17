import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
table = [[*input().strip()] for _ in range(n)]
max_val = float('-inf')


def search_treasure(x, y):
    q = deque([(x, y)])
    is_visited = [[False] * m for _ in range(n)]
    is_visited[x][y] = True
    count = -1
    while q:
        for _ in range(len(q)):
            n_x, n_y = q.popleft()
            for a, b in (1, 0), (0, 1), (-1, 0), (0, -1):
                nx = n_x+a
                ny = n_y+b
                if 0 <= nx < n and 0 <= ny < m and not is_visited[nx][ny] and table[nx][ny] == 'L':
                    is_visited[nx][ny] = True
                    q.append((nx, ny))
        count += 1
    return count


for i in range(n):
    for j in range(m):
        if table[i][j] == 'L':
            count = 0
            for a, b in (1, 0), (0, 1), (-1, 0), (0, -1):
                nx = i+a
                ny = j+b
                if 0 <= nx < n and 0 <= ny < m and table[nx][ny] == 'L':
                    count += 1
            if count < 3:
                max_val = max(max_val, search_treasure(i, j))
print(max_val)
