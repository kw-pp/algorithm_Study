def solution(alp, cop, problems):
    alp_max = sorted(problems, key=lambda x:x[0], reverse=True)[0][0]
    cop_max = sorted(problems, key=lambda x:x[1], reverse=True)[0][1]

    dp = [[0] * (cop_max + 2) for _ in range(alp_max + 2)]

    # 첫 행만 따로 계산
    for i in range(alp + 1, alp_max + 2):
        for j in range(cop + 1, cop_max + 2):
            if i == alp + 1 and j == cop + 1:
                continue
            if j == cop + 1:
                dp[i][j] = dp[i-1][j] + 1
            else:
                dp[i][j] = dp[i][j - 1] + 1

            for q in problems:
                if i >= q[0] + 1 and j >= q[1] + 1 and i - q[2] - 1 >= alp and j - q[3] - 1 >= cop:
                    if alp + 1 <= i - q[2] < cop_max + 2 and cop + 1 <= j - q[3] < cop_max + 2:
                        dp[i][j] = min(dp[i][j], dp[i - q[2]][j - q[3]] + q[4])
    return dp[-1][-1]