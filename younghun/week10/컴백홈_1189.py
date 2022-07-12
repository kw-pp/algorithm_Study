import sys

r, c, k = map(int, sys.stdin.readline().split())

table = [list(sys.stdin.readline().rstrip()) for _ in range(r)]

visited = [[False]*c for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

global cnt
cnt = 0


def dfs(x, y, distance):
    global cnt

    if distance == k and x == 0 and y == c-1:
        cnt += 1
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue
        if visited[nx][ny]:
            continue
        if table[nx][ny] == 'T':
            continue
        visited[nx][ny] = True
        dfs(nx, ny, distance + 1)
        visited[nx][ny] = False


visited[r-1][0] = True
dfs(r-1, 0, 1)
print(cnt)
