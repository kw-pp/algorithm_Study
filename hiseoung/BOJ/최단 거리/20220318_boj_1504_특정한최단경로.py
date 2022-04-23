import heapq
import sys
INF = int(1e9)

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    graph[x].append([y, z])
    graph[y].append([x, z])

x, y = map(int, sys.stdin.readline().split())
way = [[x, y], [y, x]]


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        # if distance[now] < dist:
        #     continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


value = []
for j in way:
    # 0 -> 첫번째 경유지
    distance = [INF] * (n + 1)
    dijkstra(1)
    dist = distance[j[0]]

    # 첫번째 경유지 -> 두번째 경유지
    distance = [INF] * (n + 1)
    dijkstra(j[0])
    dist += distance[j[1]]

    # 두번째 경유지 -> N
    distance = [INF] * (n + 1)
    dijkstra(j[1])
    dist += distance[n]

    value.append(dist)

if min(value) >= INF:
    print(-1)
else:
    print(min(value))






