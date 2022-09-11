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

# 시작 번호와 현재 촌수를 큐에 추가
q = deque([(k1, 0)])
is_visited = [False for _ in range(n+1)]
is_visited[k1] = True
answer = 0

# 시작 번호부터 도착 번호 찾을 때까지 탐색 ( BFS )
while q:
    current, w = q.popleft()
    # 종료 조건 : 현재 큐에서 꺼낸 노드가 도착 번호인 경우
    if current == k2:
        answer = w
        break
    for next in graph[current]:
        if not is_visited[next]:
            q.append((next, w+1))
            is_visited[next] = True
print(answer) if answer else print(-1)
