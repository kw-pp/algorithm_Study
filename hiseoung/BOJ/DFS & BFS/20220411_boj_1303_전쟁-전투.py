
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
table = [list(sys.stdin.readline().rstrip()) for _ in range(M)]
is_visited = [[False for _ in range(N)] for _ in range(M)]
count_w = 0
count_b = 0

for i in range(M):
    for j in range(N):
        if is_visited[i][j]:
            continue
        else:
            q = deque()
            q.append((i,j))
            count = 0

            if table[i][j] == 'W':
                flag = 1
            else:
                flag = 0

            while q:
                x, y = q.popleft()
                if table[x][y] == 'W':
                    for a, b in (0, 1), (0, -1), (1, 0), (-1, 0):
                        if 0 <= y+b < N and 0 <= x+a < M and table[x+a][y+b] == 'W' and not is_visited[x+a][y+b]:
                            q.append((x+a, y+b))
                            is_visited[x+a][y+b] = True
                            count += 1

                else:
                    for a, b in (1, 0), (-1, 0), (0, 1), (0, -1):
                        if 0 <= x+a < M and 0 <= y+b < N and table[x+a][y+b] == 'B' and not is_visited[x+a][y+b]:
                            q.append((x+a, y+b))
                            is_visited[x+a][y+b] = True
                            count += 1

            if flag and count:
                count_b += count**2
            elif flag and not count:
                count_b += 1
            elif not flag and count:
                count_w += count**2
            else:
                count_w += 1

print(f'{count_b} {count_w}')





