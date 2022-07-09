import sys
sys.setrecursionlimit(10 ** 6)

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
dp = [0] * 1001


# N개 중에 K를 선택 ( 조합 ), 인접한 두 색을 동시에 선택 X
def func(n, k, count):
    if n < 0:
        return 0
    if count == k:
        return 1

    if dp[n] != 0:
        return dp[0]

    dp[n] = func(n - 1, k, count) + func(n - 2, k, count + 1)

    return dp[n]


print((func(N, K, 0) + 1) % 1000000003)
