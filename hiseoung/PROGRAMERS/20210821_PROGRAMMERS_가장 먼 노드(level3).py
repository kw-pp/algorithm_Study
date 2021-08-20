import heapq


def solution(n, edge):
    '''
    출처 : https://programmers.co.kr/learn/courses/30/lessons/49189
    문제 유형 : 그래프
    - 문제를 풀어가는 방법이 다양하게 있을 수 있을 것 같다.
    - 다익스트라 알고리즘이 생각나서 이를 이용해 문제를 풀이했다.
    '''
    graph = [[] for i in range(n+1)]
    for x, y in edge:
        graph[x].append((y, 1))
        graph[y].append((x, 1))

    distance = [float('inf')] * (n + 1)
    start = 1

    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    del distance[0]
    Max = max(distance)
    return distance.count(Max)