'''
정확성 : 50
효율성 : 5
합계 : 55 / 100
'''

def solution(alp, cop, problems):
    alp_max = sorted(problems, key=lambda x:x[0], reverse=True)[0][0]
    cop_max = sorted(problems, key=lambda x:x[1], reverse=True)[0][1]

    if alp >= alp_max and cop >= cop_max:
        return 0

    a = alp_max if alp_max >= alp else alp
    c = cop_max if cop_max >= cop else cop

    if alp_max >= alp and cop_max >= cop:
        dp = [[0] * (c + 2) for _ in range(a + 2)]

        for i in range(alp + 1, a + 2):
            for j in range(cop + 1, c + 2):
                if i == alp + 1 and j == cop + 1:
                    continue
                if j == cop + 1:
                    dp[i][j] = dp[i-1][j] + 1
                elif i == alp + 1:
                    dp[i][j] = dp[i][j - 1] + 1
                else:
                    dp[i][j] = min(dp[i][j - 1] + 1, dp[i - 1][j] + 1)

                for q in problems:
                    if i - q[2] >= q[0] + 1 and j - q[3] >= q[1] + 1 and i - q[2] >= alp + 1 and j - q[3] >= cop + 1:
                        dp[i][j] = min(dp[i][j], dp[i - q[2]][j - q[3]] + q[4])
        return dp[-1][-1]

    elif alp_max >= alp and cop_max < cop:
        dp = [[0] * (c + 2) for _ in range(a + 2)]

        for i in range(alp + 1, a + 2):
            for j in range(cop + 1, c + 2):
                if i == alp + 1 and j == cop + 1:
                    continue
                if j == cop + 1:
                    dp[i][j] = dp[i - 1][j] + 1
                elif i == alp + 1:
                    dp[i][j] = dp[i][j - 1] + 1
                else:
                    dp[i][j] = min(dp[i][j - 1] + 1, dp[i - 1][j] + 1)

                for q in problems:
                    if i - q[2] >= q[0] + 1 and i - q[2] >= alp + 1:
                        dp[i][j] = min(dp[i][j], dp[i - q[2]][j] + q[4])
        return dp[-1][-1]

    elif alp_max < alp and cop_max >= cop:
        dp = [[0] * (c + 2) for _ in range(a + 2)]

        for i in range(alp + 1, a + 2):
            for j in range(cop + 1, c + 2):
                if i == alp + 1 and j == cop + 1:
                    continue
                if j == cop + 1:
                    dp[i][j] = dp[i - 1][j] + 1
                elif i == alp + 1:
                    dp[i][j] = dp[i][j - 1] + 1
                else:
                    dp[i][j] = min(dp[i][j - 1] + 1, dp[i - 1][j] + 1)

                for q in problems:
                    if j - q[3] >= q[1] + 1 and j - q[3] >= cop + 1:
                        dp[i][j] = min(dp[i][j], dp[i][j - q[3]] + q[4])
        return dp[-1][-1]