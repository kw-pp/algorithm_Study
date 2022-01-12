import sys


def dp(num):
    '''
    출처 : https://www.acmicpc.net/problem/10844
    문제 유형 : DP
    - 주어진 자릿수와 계단수의 마지막 수로 이루어진 2차원 dp배열을 생각해야 푸는게 가능한 문제
    '''

    dp = [[0] * 10 for _ in range(n+1)]

    dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    for i in range(2, n+1):
        dp[i][0] = dp[i-1][1]
        dp[i][9] = dp[i-1][8]

        for j in range(1, 9):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    return (sum(dp[n]) % 1000000000)



n = int(sys.stdin.readline())
print(dp(n))