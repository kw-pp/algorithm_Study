import sys
from collections import deque

# def dfs():
#     for a, b in r_d:
#         if 0 <= x+a < n and 0 <= y+b < m and table[x+a][y+b] == 0:
#             table[x+a][y+b] = 2

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())

table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# 0 : 북, 1 : 동, 2 : 남, 3: 서
r_d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
temp = r_d[::-1]


if d == 0:
    r_d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
elif d == 1:
    r_d = [(0, 1), (-1, 0), (0, -1), (1, 0)]
elif d == 2:
    r_d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
else:
    r_d = [(0, -1), (1, 0), (0, 1), (-1, 0)]


table[r][c] = 2
q = deque([(r, c)])


while q:
    x,y = q.popleft()
    for a, b in r_d:
        if 0 <= x+a < n and 0 <= y+b < m and table[x+a][y+b] == 0:
            # flag += 1
            table[x+a][y+b] = 2
            q.append((x+a, y+b))

print(sum([row.count(2) for row in table]))





