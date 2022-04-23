import sys
from collections import deque
input = sys.stdin.readline

N, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    p, q, r = (map(int, input().split()))
    graph[p].append((q, r))
    graph[q].append((p, r))

for _ in range(Q):
    k, v = map(int, input().split())
    answer = 0
    visited = [0] * (N + 1)
    visited[v] = True
    q = deque([(v, 10**9+1)])

    while q:
        v, r = q.pop()
        for x, y in graph[v]:
            y = min(r, y)
            if y >= k and not visited[x]:
                visited[x] = 1
                answer += 1
                q.append((x, y))
    print(answer)

"""
1) not using bfs + 시간초과
import sys

input = sys.stdin.readline
N, Q = map(int, input().split())

graph = [[0] * N for _ in range(N)]
visited = [0] * N

#연결 노드 + 엣지 값 저장
for _ in range(N-1):
  p, q, r = map(int, input().split())
  graph[p-1][q-1] = r
  graph[q-1][p-1] = r

for _ in range(Q):
  k, v = map(int, input().split())
  answer = 0

  for i in range(N):
    if i == v-1:
      continue
    if min(max(graph[i]), max(graph[v-1])) >= k:
      answer += 1

  print(answer)
  """
