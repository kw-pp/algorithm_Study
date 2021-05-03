import sys
from collections import deque

n = int(sys.stdin.readline())

li = []
for i in range(n):
    li.append(list(str(sys.stdin.readline().strip())))


is_visited = [[False] * n for _ in range(n)]
q = deque()
answer = []

for i in range(n):
    for j in range(n):
        count = 0
        if li[i][j] == '0' or is_visited[i][j]:
            continue
        else:
            count += 1
            q.append((i, j))
            while q:
                x, y = q.popleft()
                for a, b in (1, 0), (-1, 0), (0, 1), (0, -1):
                    if 0 <= x+a < n and 0 <= y+b < n and li[x+a][y+b] == '1' and not is_visited[x+a][y+b]:
                        q.append((x+a, y+b))
                        is_visited[x+a][y+b] = True
                        count += 1
                    else:
                        continue
            if count == 1:
                answer.append(count)
            else:
                answer.append(count-1)

print(len(answer))
answer.sort()
for i in range(len(answer)):
    print(answer[i])




