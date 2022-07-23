import sys
from itertools import islice
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m = map(int, input().split())
queen = input().strip().split()[1:]
knight = input().strip().split()[1:]
pawn = input().strip().split()[1:]
table = [[0 for _ in range(m)] for _ in range(n)]
count = 0

iter_q = iter(queen)
iter_k = iter(knight)
iter_p = iter(pawn)

queen = [list(map(lambda x:int(x) - 1, islice(iter(iter_q), 2))) for _ in range(len(queen) // 2)]
knight = [list(map(lambda x:int(x) - 1, islice(iter(iter_k), 2))) for _ in range(len(knight) // 2)]
pawn = [list(map(lambda x:int(x) - 1, islice(iter(iter_p), 2))) for _ in range(len(pawn) // 2)]


def move_queen(x, y, a, b):
    if 0 <= x + a < n and 0 <= y+b < m and table[x+a][y+b] != 1:
        table[x+a][y+b] = 2
        move_queen(x+a, y+b, a, b)
    else:
        return


for x, y in knight:
    table[x][y] = 1
for x, y in pawn:
    table[x][y] = 1
for x, y in queen:
    table[x][y] = 1


# 1. Knight
for x, y in knight:
    for a, b in (1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1):
        if 0 <= x + a < n and 0 <= y+b < m and table[x+a][y+b] != 1:
            table[x+a][y+b] = 2
# 3. Queen
for x, y in queen:
    for a, b in (1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1):
        move_queen(x, y, a, b)

for i in range(n):
    for j in range(m):
        if table[i][j] == 0:
            count += 1

print(count)