from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

max_val = max(map(max, arr))

#동서남북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0

def solution(x, y, cnt, num):
  global answer
  #\자꾸 틀려서 코드 찾아봄 : 이 예외 식을 생각을 못함\
  if answer >= num + max_val * (3 - cnt):
    return
  if cnt == 3:
    answer = max(answer, num)
    return    
  for k in range(4):
    mx = x + dx[k]
    my = y + dy[k]
    if 0 <= mx < N and 0 <= my < M and visited[mx][my] == 0:
      if cnt == 1:
        visited[mx][my] = 1
        solution(x, y, cnt+1, num+arr[mx][my])
        visited[mx][my] = 0
      visited[mx][my] = 1
      solution(mx, my, cnt+1, num+arr[mx][my])
      visited[mx][my] = 0

for i in range(N):
  for j in range(M):
    visited[i][j] = 1
    solution(i, j, 0, arr[i][j])
    visited[i][j] = 0
print(answer)
