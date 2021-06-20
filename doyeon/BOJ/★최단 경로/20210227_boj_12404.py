import sys
inp = sys.stdin.readline
INF = int(1e9)
n = int(input())
m = int(input())
graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
  a,b,c = map(int, inp().split())
  if graph[a][b]>c:
    graph[a][b] = c

for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      if a!=b:
        graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1, n+1):
  for b in range(1, n+1):
    if graph[a][b] == INF:
      print(0, end=" ")
    else:
      print(graph[a][b], end=" ")
  print()