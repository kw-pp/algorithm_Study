import sys
from collections import deque

def solution(n, m, arr):
    '''
    출처 : https://www.acmicpc.net/problem/2206
    티어 : 골드 4
    유형 : BFS
    - 1차 시도 : 시간초과!!!!
    - 2차 시도 : 반례는 다 넘기는데 시간초과 해결 못함 -> 3차원 배열 이용?!
    '''

    Min = float('inf')
    is_checked = False

    for r in range(n):
        for c in range(m):
            if arr[r][c] == '1':
                arr[r][c] = '0'
                path = 0
                check = False
                q = deque()
                q.append((0, 0))
                breaker = False
                is_visited = [[False] * m for _ in range(n)]
                while q:
                    if breaker:
                        break
                    for _ in range(len(q)):
                        x, y = q.popleft()
                        if x == n - 1 and y == m - 1:
                            check = True
                            breaker = True
                            break
                        for a, b in (1, 0), (0, 1), (-1, 0), (0, -1):
                            if 0 <= x+a < n and 0 <= y+b < m and not is_visited[x+a][y+b]:
                                if arr[x+a][y+b] == '0':
                                    is_visited[x+a][y+b] = True
                                    q.append((x+a, y+b))
                    path += 1
                if check and Min > path:
                    Min = path
                    is_checked = True

                arr[r][c] = '1'
            else:
                continue

    if not is_checked:
        Min = False

    return Min


n, m = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(list(sys.stdin.readline().strip()))

print(solution(n, m, arr))



