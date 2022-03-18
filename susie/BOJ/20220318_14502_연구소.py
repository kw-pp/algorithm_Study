import sys
import copy
from collections import deque

read = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = 0

N, M = map(int, read().split())
m = [list(map(int, read().split())) for _ in range(N)]
queue = deque()

def bfs():
  global answer
  cm = copy.deepcopy(m)
  for i in range(N):
    for j in range(M):
      if cm[i][j] == 2:
        queue.append([i, j])

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      mx = x + dx[i]
      my = y + dy[i]
      if 0 <= mx < N and 0 <= my < M:
        if cm[mx][my] == 0:
          cm[mx][my] = 2
          queue.append([mx, my])
  cnt = 0
  for i in cm:
    cnt += i.count(0)
  answer = max(answer, cnt)

def wall(x):
  if x == 3:
    bfs()
    return
  for i in range(N):
    for j in range(M):
      if m[i][j] == 0:
        m[i][j] = 1
        wall(x+1)
        m[i][j] = 0

wall(0)
print(answer)
