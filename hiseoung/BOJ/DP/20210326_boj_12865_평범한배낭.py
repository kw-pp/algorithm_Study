import sys
n, k = map(int, sys.stdin.readline().split())
val = [[0,0]]
for i in range(n):
    val.append(list(map(int, sys.stdin.readline().split())))
dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        if j < val[i][0]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(val[i][1] + dp[i - 1][j - val[i][0]], dp[i - 1][j])
print(dp[n][k])
