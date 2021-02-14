# DFS
def dfs(graph, v, visited):
  visited[v] = True
  print(v, end=' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

# BFS
from collections import deque
def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v, end=' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  x,y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)
for i in range(len(graph)):
  graph[i].sort()

visited = [False]*(n+1)
dfs(graph,v,visited)
print()
visited = [False]*(n+1)
bfs(graph,v,visited)