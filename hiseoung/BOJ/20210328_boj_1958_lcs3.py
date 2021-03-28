import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
c = sys.stdin.readline().strip()
la = len(a)
lb = len(b)
lc = len(c)
dp = [[[0 for _ in range(lc + 1)] for _ in range(lb + 1)] for _ in range(la + 1)]

for i in range(1, la + 1):
    for j in range(1, lb + 1):
        for z in range(1, lc + 1):
            if a[i-1] == b[j-1] == c[z-1]:
                dp[i][j][z] = dp[i-1][j-1][z-1] + 1
            else:
                dp[i][j][z] = max(dp[i-1][j][z], dp[i][j-1][z], dp[i][j][z-1], dp[i-1][j-1][z], dp[i-1][j][z-1], dp[i][j-1][z-1])

print(dp[-1][-1][-1])
