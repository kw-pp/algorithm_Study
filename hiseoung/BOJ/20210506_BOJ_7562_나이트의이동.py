import sys
from collections import deque

t = int(sys.stdin.readline())
answer = []

for i in range(t):

    n = int(sys.stdin.readline())
    px, py = map(int, sys.stdin.readline().split())
    tx, ty = map(int, sys.stdin.readline().split())

    is_visited = [[False] * n for _ in range(n)]
    q = deque()
    if px == tx and py == ty:
        pass
    else:
        q.append((px, py))
    is_visited[px][py] = True
    count = 0
    breaker = False

    while q:
        count += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            for a, b in (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2):
                if 0 <= x+a < n and 0 <= y+b < n and not is_visited[x+a][y+b]:
                    if x + a == tx and y + b == ty:
                        # print("정답 찾음")
                        # print(count)
                        breaker = True
                        break
                    q.append((x+a, y+b))
                    is_visited[x+a][y+b] = True

            if breaker:
                break
        if breaker:
            break
    answer.append(count)

for i in range(t):
    print(answer[i])






