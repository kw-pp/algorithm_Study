import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k1, k2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
q = deque([(k1, 0)])
is_visited = [False for _ in range(n+1)]
is_visited[k1] = True
answer = 0
while q:
    for _ in range(len(q)):
        current, w = q.popleft()
        if current == k2:
            answer = w
            break
        for next in graph[current]:
            if not is_visited[next]:
                q.append((next, w+1))
                is_visited[next] = True
print(answer) if answer else print(-1)
