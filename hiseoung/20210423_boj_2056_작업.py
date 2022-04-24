import sys

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
dict = {key:0 for key in range(N+1)}
for i in range(N):
    li = list(map(int, sys.stdin.readline().split()))
    graph[i+1].extend(li[2:])
    dict[i+1] = li[1]





