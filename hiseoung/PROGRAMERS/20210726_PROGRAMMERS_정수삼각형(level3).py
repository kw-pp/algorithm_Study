def solution(triangle):
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
