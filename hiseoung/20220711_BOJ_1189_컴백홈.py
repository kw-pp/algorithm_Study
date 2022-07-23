import sys
from collections import deque
input = sys.stdin.readline

R, C, K = map(int, input().split())
table = [list(input().strip()) for _ in range(R)]
is_visited = [[0 for _ in range(C)] for _ in range(R)]

is_visited[R-1][0] = 1
answer = 0

def dfs(x, y, k):
    global answer, R, C, K
    if k == K-1:
        if x == 0 and y == C-1:
            answer += 1
        return
    for a, b in (0, 1), (1, 0), (-1, 0), (0, -1):
        if 0 <= x+a < R and 0 <= y+b < C:
            if not is_visited[x+a][y+b] and table[x+a][y+b] == '.':
                is_visited[x+a][y+b] = 1
                dfs(x+a, y+b, k+1)
                is_visited[x+a][y+b] = 0

dfs(R-1, 0, 0)
print(answer)
