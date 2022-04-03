import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

# 1. 완전 탐색
is_visited = [False for _ in range(N)]
