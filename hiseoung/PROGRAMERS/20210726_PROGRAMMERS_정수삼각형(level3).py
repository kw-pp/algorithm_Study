import sys

def solution(triangle):
    '''
    출처 : https://programmers.co.kr/learn/courses/30/lessons/43105
    문제 유형 : 동적 계획법
    풀이 시간 : 40분
    '''
    tri_len = len(triangle)
    dp = [[0] * tri_len for _ in range(tri_len)]
    for i in range(tri_len):
        for j in range(i + 1):
            if i == 0:
                dp[i][j] = triangle[i][j]
            else:
                if j == 0:
                    dp[i][j] = triangle[i][j] + dp[i - 1][j]
                elif j == i:
                    dp[i][j] = triangle[i][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = triangle[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j])

    return max(dp[tri_len-1])

n = int(sys.stdin.readline())
li = [[] for _ in range(n)]
for i in range(0, n):
    temp = list(map(int, input().split()))
    li[i] = temp
    
print(solution(li))

