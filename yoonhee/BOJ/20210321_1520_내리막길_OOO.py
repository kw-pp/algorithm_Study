import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
dx = [1,-1,0,0]
dy = [0,0,-1,1]
def dfs(x,y):
    if x == 0 and y == 0 : # 최종 목적지(출발지점)
        return 1
    if dp[x][y] == -1 : # 한번도 방문하지 않은 지점
        dp[x][y] = 0   # 방문함 == 0
        for i in range(4): 
            nx = x + dx[i] # 위,아래 방향 지정
            ny = y + dy[i] # 오, 왼 방향 지정
            if 0 <= nx < m and 0 <= ny < n: # 조건 : 할당된 범위 내 
                # 조건 : 이동하는 방향의 높이(s[nx][ny])가 높은 경우, 이동함
                # *주의* 역순으로 찾기 때문에 높이가 높은 경우에 이동 <-> 출발지에서 높이가 낮은
                if s[x][y] < s[nx][ny]: 
                    dp[x][y] += dfs(nx, ny) # recursion
    return dp[x][y]

m,n = map(int, input().split())
s = [list(map(int, input().split())) for i in range(m)]
dp = [[-1] * n for i in range(m)]
print(dfs(m-1, n-1))
