import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
table = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
is_visited = [[False for _ in range(M)] for _ in range(N)]
count = 0

for i in range(N):
    for j in range(M):
        if is_visited[i][j]:
            continue
        else:
            q = deque()
            q.append((i,j))

            while q:
                x, y = q.popleft()
                if table[x][y] == '-':
                    for a, b in (0, 1), (0, -1):
                        if 0 <= y+b < M and table[x+a][y+b] == '-' and not is_visited[x+a][y+b]:
                            q.append((x+a, y+b))
                            is_visited[x+a][y+b] = True

                else:
                    for a, b in (1, 0), (-1, 0):
                        if 0 <= x+a < N and table[x+a][y+b] =='|' and not is_visited[x+a][y+b]:
                            q.append((x+a, y+b))
                            is_visited[x+a][y+b] = True

            count += 1

print(count)





