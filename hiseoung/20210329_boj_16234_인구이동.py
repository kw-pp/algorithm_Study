import sys; input = sys.stdin.readline
from collections import deque

n, l ,r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(start):
    dq, check = deque(), [start]
    dq.append(start)
    s, ll = graph[start[0]][start[1]], 1
    while dq:
        y, x = dq.popleft()
        for k in range(4):
            b, a = y+dy[k], x+dx[k]
            if 0<=b<n and 0<=a<n:
                if l<=abs(graph[b][a]-graph[y][x])<=r and (b,a) not in check:
                    dq.append((b, a))
                    check.append((b,a))
                    s += graph[b][a]
                    ll += 1
    if ll==1:
        return 0
    for i, j in check:
        visited[i][j] = s//ll
    return 1
count = 0
while True:
    flag = True
    visited = [[-1]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]==-1 and bfs((i, j)):
                flag = False
    if flag:
        break
    count += 1
    for i in range(n):
        for j in range(n):
            if visited[i][j]!=-1:
                graph[i][j] = visited[i][j]
print(count)