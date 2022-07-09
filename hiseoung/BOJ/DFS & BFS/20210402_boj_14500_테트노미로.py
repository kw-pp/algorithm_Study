
'''
    - BFS 이용
    - python3 시간초과, pypy3 통과
    - python3 넘길 수 있도록 재풀이 필요
'''

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_val = float('-inf')

for i in range(0, N):
    for j in range(0, M):
        q = deque([(i, j, i, j, table[i][j])])
        count = 0
        while q:
            if count == 3:
                break
            for _ in range(len(q)):
                x, y, px, py, v = q.popleft()
                for a, b in (0, 1), (1, 0), (0, -1), (-1, 0):
                    if 0 <= x + a < N and 0 <= y + b < M:
                        if x + a == px and y + b == py:
                            continue
                        else:
                            q.append((x + a, y + b, x, y, table[x + a][y + b] + v))
            count += 1

        # BFS로 가려낼 수 없는 케이스 : 'ㅗ' 모양 테크노미로
        expt_case = []
        for a, b in (0, 1), (1, 0), (0, -1), (-1, 0):
            if 0 <= i + a < N and 0 <= j + b < M:
                if a == 0 and b == 1:
                    if 0 <= i + a - 1 < N and 0 <= i + a + 1 < N:
                        expt_case.append(
                            table[i][j] + table[i + a][j + b] + table[i + a - 1][j + b] + table[i + a + 1][j + b])
                elif a == 1 and b == 0:
                    if 0 <= j + b - 1 < M and 0 <= j + b + 1 < M:
                        expt_case.append(
                            table[i][j] + table[i + a][j + b] + table[i + a][j + b - 1] + table[i + a][j + b + 1])
                elif a == 0 and b == -1:
                    if 0 <= i + a - 1 < N and 0 <= i + a + 1 < N:
                        expt_case.append(
                            table[i][j] + table[i + a][j + b] + table[i + a - 1][j + b] + table[i + a + 1][j + b])
                else:
                    if 0 <= j + b - 1 < M and 0 <= j + b + 1 < M:
                        expt_case.append(
                            table[i][j] + table[i + a][j + b] + table[i + a][j + b - 1] + table[i + a][j + b + 1])
        if expt_case:
            val = max(max(list(q), key=lambda x: x[4])[4], max(expt_case))
        else:
            val = max(list(q), key=lambda x: x[4])[4]
        if val > max_val:
            max_val = val

print(max_val)
