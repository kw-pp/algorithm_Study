import sys
from collections import deque

N, M = map(int, input().split())
arr = [list(input()) for _ in range(M)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[0] * N for _ in range(M)]
my_sol, your_sol = 0, 0

for i in range(M):
  for j in range(N):
    if visited[i][j] == 0:
      if arr[i][j] == 'W':
        label, cnt = 'W', 0
      else:
        label, cnt = 'B', 0

      q = deque([(i, j)])
      while q:
        x, y = q.popleft()
        for k in range(4):
          mx = x + dx[k]
          my = y + dy[k]
          if 0 <= mx < M and 0 <= my < N and visited[mx][my] == 0 and arr[mx][my] == label:
            visited[mx][my] = 1
            cnt += 1
            q.append((mx, my))
      if cnt == 0:
        cnt += 1
      if label == 'W':
        my_sol += cnt**2
      else:
        your_sol += cnt**2

print(my_sol, your_sol)
