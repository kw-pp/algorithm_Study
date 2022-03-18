#로봇 청소기
import sys
read = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]

N, M = map(int, read().split()) #맵 사이즈
r, c, d = map(int, read().split()) #청소기 위치 (r, c), 방향 d
m = [list(map(int, read().split())) for _ in range(N)] # 맵

def dfs(x, y, d):
  global answer
  if m[x][y] == 0: #현재 위치가 청소되어있지 않은 경우
    m[x][y] = 2
    answer += 1
  for _ in range(4): #네방향 모두 탐색
    md = (d+3) % 4 #왼쪽방향
    mx = x + dx[md]
    my = y + dy[md]
    if m[mx][my] == 0:
      dfs(mx, my, md) # 벽X, 청소안되어있는경우
      return
    d = md
  #후진해야 하는 경우
  md = (d+2) % 4
  mx = x + dx[md]
  my = y + dy[md]
  if m[mx][my] == 1:
    return
  dfs(mx, my, d)

answer = 0 
dfs(r, c, d)
print(answer)
