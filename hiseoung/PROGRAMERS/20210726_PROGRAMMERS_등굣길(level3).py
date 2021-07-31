def solution(m, n, puddles):
    '''
    출처 : https://programmers.co.kr/learn/courses/30/lessons/43105
    문제 유형 : 동적 계획법
    풀이 시간 : 1시간
    '''
    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
                if i == j == 1:
                    dp[i][j] = 1
                elif [j,i] in puddles:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1] % 1000000007