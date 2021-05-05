import sys
from collections import deque

n = int(sys.stdin.readline())
li = []
Max = float('-inf')
Min = float('inf')
for i in range(n):
    li.append(list(map(int, sys.stdin.readline().split())))
    Max = max(max(li[i]), Max)
    Min = min(min(li[i]), Min)

count = []

for z in range(Min, Max):
    q = deque()
    num = 0

    co = [[0] * n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            if li[a][b] > z:
                co[a][b] = 1

    for i in range(n):
        for j in range(n):
            if co[i][j] == 1:
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    for a, b in (1, 0), (0, 1), (-1, 0), (0, -1):
                        if 0 <= x + a < n and 0 <= y + b < n and co[x + a][y + b] == 1:
                            q.append((x + a, y + b))
                            co[x + a][y + b] = 0
                num += 1
    count.append(num)
try:
    answer = max(count)
except:
    answer = 1
print(answer)
