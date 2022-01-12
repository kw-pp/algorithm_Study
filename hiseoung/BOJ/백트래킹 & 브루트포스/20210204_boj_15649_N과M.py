import itertools
import sys
N, M = map(int, input().split())

a = range(1, N+1)
p = list(itertools.permutations(a, M))
for i in range(len(p)):
    for j in range(N):
        try:
            sys.stdout.write(str(p[i][j]) + " ")
        except IndexError:
            pass
    print()
