import sys
from collections import deque

n = int(sys.stdin.readline())
graph = {i:[] for i in range(n+1)}
parents = [0]*n

for i in range(n-1):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

q = deque()
q.append(1)

while q:
    x = q.popleft()
    for i in graph[x]:
        if parents[x - 1] != i:
            parents[i - 1] = x
            q.append(i)



for i in parents[1:]:
    print(i)

