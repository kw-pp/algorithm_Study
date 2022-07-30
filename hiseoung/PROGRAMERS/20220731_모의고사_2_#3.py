import heapq

def solution(n, roads, sources, destination):
    answer = []
    heap = []
    edge = [[] for _ in range(n + 1)]
    dist = [float('inf')] * (n + 1)

    for i in range(len(roads)):
        u, v = roads[i]
        edge[u].append([1, v])
        edge[v].append([1, u])

    def dijkatra(start):
        dist[start] = 0
        heapq.heappush(heap, (0, start))

        while heap:
            weight, current = heapq.heappop(heap)

            if dist[current] < weight:
                continue

            for w, next in edge[current]:
                next_weight = w + weight

                if next_weight < dist[next]:
                    dist[next] = next_weight
                    heapq.heappush(heap, (next_weight, next))

    dijkatra(destination)

    for i in sources:
        if dist[i] == float('inf'):
            answer.append(-1)
        else:
            answer.append(dist[i])

    return answer

