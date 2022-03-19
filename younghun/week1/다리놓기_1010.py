import sys
from math import factorial


n = int(sys.stdin.readline())
testcase = [map(int, sys.stdin.readline().split()) for _ in range(n)]

for N, M in testcase:
    print(factorial(M) // (factorial(M-N) * factorial(N)))
