import sys

# 포켓몬의 개수 : N / 문제 개수 : M
N, M = map(int, sys.stdin.readline().split())

# 포켓몬 도감 채우기
pocketDict = dict()
for i in range(1, N + 1):
    obj = sys.stdin.readline().strip()
    pocketDict[obj] = str(i)
    pocketDict[str(i)] = obj

for _ in range(M):
    print(pocketDict[sys.stdin.readline().strip()])
