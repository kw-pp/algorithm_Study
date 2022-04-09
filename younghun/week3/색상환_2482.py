MOD = 1000000003

N = int(input())
K = int(input())

dp = [[0] * (N + 1) for i in range(N + 1)]

for i in range(N + 1):
    dp[i][0] = 1
    dp[i][1] = i

for i in range(3, N + 1):
    for j in range(2, int((i + 1) / 2) + 1):
        dp[i][j] = (dp[i - 1][j] + dp[i - 2][j - 1]) % MOD

print((dp[N - 3][K - 1] + dp[N - 1][K]) % MOD)
