import sys
import math
ft = math.factorial

T = int(sys.stdin.readline())
bridge = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]

for a, b in bridge:
    print(int((ft(b) // (ft(b - a) * ft(a)))))