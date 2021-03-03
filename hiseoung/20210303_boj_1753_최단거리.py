#1753
import heapq
V, E = map(int, input().split())
INF = float('inf')
start = int(input())
dist = [INF] * (V+1) # 최단거리 기록
heap = []
Edge = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    Edge[u].append((w, v))


def dijkatra(start):
    dist[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        weight, current = heapq.heappop(heap)

        if dist[current] < weight:
            continue
        for w, next in Edge[current]:
            next_weight = w + weight

            if next_weight < dist[next]:
                dist[next] = next_weight
                heapq.heappush(heap,(next_weight,next))




dijkatra(start)

for i in range(1,V+1):
    print("INF" if dist[i] == INF else dist[i])
