import sys

row, col = map(int, sys.stdin.readline().split())
mat_A, mat_B = [], []
for i in range(row):
    if i < row:
        mat_A.append(list(map(int, sys.stdin.readline().split())))
    else:
        mat_B.append(list(map(int, sys.stdin.readline().split())))


