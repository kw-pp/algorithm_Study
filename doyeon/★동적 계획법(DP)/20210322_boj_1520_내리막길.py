# 그리디 해결방법
# import sys
# input = sys.stdin.readline
# from collections import deque
# n, m = map(int, input().split())
# graph = []
# for _ in range(n):
#   graph.append(list(map(int, input().split())))

# # 이동한 세 방향 정의(하, 좌, 우)
# dx = [1, 0, 0]
# dy = [0, -1, 1]

# count = 0
# queue = deque()
# queue.append((0,0))
# while queue:
#   x,y = queue.popleft()
#   # 만약 목적지에 도착하면 
#   if x==n-1 and y==m-1:
#     count+=1
#     continue
#   # 현재 위치에서 세 방향으로의 위치 확인
#   for i in range(3):
#     nx = x+dx[i]
#     ny = y+dy[i]
#     # 공간을 벗어난 경우 무시
#     if nx<0 or ny<0 or nx>=n or ny>=m:
#       continue
#     # 더 작은 경우에만 이동
#     if graph[nx][ny] < graph[x][y]:
#       queue.append((nx,ny))
# print(count)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y):
    if x == 0 and y == 0:
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if s[x][y] < s[nx][ny]:
                    dp[x][y] += dfs(nx, ny)
    return dp[x][y]
m, n = map(int, input().split())
s = [list(map(int, input().split())) for i in range(m)]
dp = [[-1] * n for i in range(m)]
print(dfs(m - 1, n - 1))