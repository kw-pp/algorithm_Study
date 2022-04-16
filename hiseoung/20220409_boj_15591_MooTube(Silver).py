import sys
from collections import deque

N, Q = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    x, y, z = map(int, sys.stdin.readline().split())
    graph[x].append([y, z, float('inf')])
    graph[y].append([x, z, float('inf')])

q_list = [list(map(int, sys.stdin.readline().split())) for _ in range(Q)]

for k, v in q_list:
    q = deque(graph[v])
    is_visited = [False for _ in range(N + 1)]
    val_list = [False for _ in range(N + 1)]
    count = 0
    while q:
        x, y, z = q.popleft()
        if not is_visited[x]:
            val = min(y, z)
            is_visited[x] = True
            val_list[x] = val
            for edge in graph[x]:
                if not is_visited[edge[0]]:
                    q.append([edge[0], edge[1], val])
    del val_list[v]
    del val_list[0]
    answer = [val for val in val_list if val >= k]
    print(len(answer))







