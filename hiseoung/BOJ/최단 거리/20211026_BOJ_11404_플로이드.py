import sys

def solution11404():
    '''
    출처 : https://www.acmicpc.net/problem/11404
    분류 : 최단거리-플로이드 와샬
    시간복잡도 : O(N^3)
    '''
    for i in range(n):
        for a in range(n):
            for b in range(n):
                busInfo[a][b] = min(busInfo[a][b], busInfo[a][i] + busInfo[i][b])

    return busInfo

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
busInfo = [[float('inf') for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            busInfo[i][j] = 0

for i in range(m):
    start, end, edge = map(int, sys.stdin.readline().strip().split())
    if busInfo[start-1][end-1] != float('inf'):
        busInfo[start - 1][end - 1] = min(busInfo[start - 1][end - 1], edge)
    else:
        busInfo[start-1][end-1] = edge

solution11404()

for i in busInfo:
    for j in i:
        if j == float('inf'):
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()
