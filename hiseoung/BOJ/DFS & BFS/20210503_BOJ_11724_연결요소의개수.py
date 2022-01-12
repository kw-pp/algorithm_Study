import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

is_visited = [0] * (n+1)
queue = deque()

def bfs(v):
    global queue
    queue.append(v)
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if is_visited[i] == 0:
                queue.append(i)
                is_visited[i] = 1

answer = 0
for i in range(1, n+1):
    if is_visited[i] == 0:
        bfs(i)
        answer += 1

print(answer)

