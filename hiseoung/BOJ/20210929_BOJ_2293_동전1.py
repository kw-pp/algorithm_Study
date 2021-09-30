import sys


def solution(k):
    '''
    출처 : https://www.acmicpc.net/problem/2293
    문제 유형 : 다이내믹 프로그래밍
    티어 : 실버 1
    '''

    for i in li:
        for j in range(i, k + 1):
            dp[j] += dp[j - i]
    return dp[k]


n, k = map(int, sys.stdin.readline().strip().split())
li = [int(input()) for i in range(n)]
dp = [0 for i in range(k+1)]
dp[0] = 1
print(solution(k))
