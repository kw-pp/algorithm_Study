import sys
import heapq

def solution1916(start):
    '''
    출처 : https://www.acmicpc.net/problem/1916
    문제 유형 : 최단 경로 / 다익스트라
    티어 : 골드 5
    '''
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

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]

for i in range(m):
    x, y, k = map(int, sys.stdin.readline().split())
    graph[x].append((y, k))

start, end = map(int, sys.stdin.readline().split())
distance = [float('inf') for _ in range(n+1)]

solution1916(start)
print(distance[end])

