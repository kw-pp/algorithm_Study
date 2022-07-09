import sys

N = int(sys.stdin.readline())
info = [list(map(int, sys.stdin.readline().split())) for _ in range(N ** 2)]
table = [[0 for _ in range(N)] for _ in range(N)]
for row in table:
    idx = row[0]
    idx_info = row[1:]
