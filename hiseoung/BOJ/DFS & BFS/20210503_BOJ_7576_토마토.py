import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
li = []

for i in range(m):
    li.append(list(map(int, sys.stdin.readline().split())))

q = deque()

# 초기값을 큐에 넣어주기
for i in range(m):
    for j in range(n):
        if li[i][j] == 1:
            q.append((i, j))

count = 0

while q:
    count += 1
    for _ in range(len(q)):
        x, y = q.popleft()
        for a, b in (-1, 0), (1, 0), (0, -1), (0, 1):
            if 0 <= x+a < m and 0 <= y+b < n and li[x+a][y+b] == 0:
                li[x+a][y+b] = 1
                q.append((x+a, y+b))
            else:
                continue

breaker = False

# 안익은 토마토가 있다면 -1로 저장
for i in range(m):
    if breaker:
        break
    for j in range(n):
        if li[i][j] == 0:
            count = -1
            breaker = True

if count == -1:
    print(count)
else:
    print(count-1)
