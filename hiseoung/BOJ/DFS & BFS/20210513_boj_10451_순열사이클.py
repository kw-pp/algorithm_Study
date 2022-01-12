import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    v1 = []
    for i in range(n):
        v1.append(i+1)
    v2 = list(map(int, sys.stdin.readline().split()))
    graph = [[0] * 2 for _ in range(n)]
    for i in range(n):
        graph[i][0] = v1[i]
        graph[i][1] = v2[i]

    count = 0
    is_visited = [False] * n

    while graph:

        q = deque()
        px, py = graph[0][0], graph[0][1]
        q.append((px, py))
        count += 1

        while q:
            x, y = q.popleft()
            if px == y:
                break
            for i in range(len(graph)):
                if graph[i][0] == y:
                    q.append(graph[i])
                    del graph[i]
                    break

    print(count)
