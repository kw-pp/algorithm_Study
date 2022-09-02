import sys
from itertools import permutations
from copy import deepcopy
input = sys.stdin.readline

n, m, k = map(int, input().split())
table_prev = [[*map(int, input().split())] for _ in range(n)]
order = [(*map(int, input().split()), ) for _ in range(k)]
order_list = permutations(order, len(order))
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
min_val = float('inf')

def rotate_table(r, c, s):
    if s == 0:
        return
    x = r - s
    y = c - s
    temp_prev = table[x][y]
    for a, b in dirs:
        while True:
            if r-s <= x + a <= r+s and c-s <= y + b <= c+s:
                temp_next = table[x + a][y + b]
                table[x + a][y + b] = temp_prev
                temp_prev = temp_next
                x = x + a
                y = y + b
            else:
                break

    return rotate_table(r, c, s - 1)


for li in order_list:
    table = deepcopy(table_prev)
    for r, c, s in li:
        rotate_table(r - 1, c - 1, s)
    min_val = min(min_val, min([sum(row) for row in table]))

print(min_val)
