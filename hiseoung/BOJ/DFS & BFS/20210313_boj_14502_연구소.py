import sys
from collections import deque
from itertools import combinations
import copy

n, m = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

s_p = list(combinations([(i, j) for i in range(n) for j in range(m) if table[i][j] == 0], 3))
v_p = [(i, j) for i in range(n) for j in range(m) if table[i][j] == 2]

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
q = deque()
max_space = -1

for walls in s_p:
    table_cp = copy.deepcopy(table)
    for x, y in walls:
        table_cp[x][y] = 1
    q = deque(v_p)

    while q:
        x, y = q.popleft()
        for a, b in d:
            if 0 <= x + a < n and 0 <= y + b < m and table_cp[x+a][y+b] == 0:
                table_cp[x+a][y+b] = 2
                q.append((x+a, y+b))

    max_table = sum(row.count(0) for row in table_cp)
    if max_space < max_table:
        max_space = max_table

print(max_space)



