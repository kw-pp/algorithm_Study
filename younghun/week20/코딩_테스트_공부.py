def solution(alp, cop, problems):
    max_alp_req, max_cop_req = [0, 0]  # 목표값

    for problem in problems:
        max_alp_req = max(max_alp_req, problem[0])
        max_cop_req = max(max_cop_req, problem[1])

    dp = [[float('inf')] * (max_cop_req + 1) for _ in range(max_alp_req + 1)]

    alp = min(alp, max_alp_req)  # 둘중 하나라도 목표값을 넘어가면 안된다.
    cop = min(cop, max_cop_req)

    dp[alp][cop] = 0  # dp[i][j]의 의미 : 알고력 i, 코딩력 j을 도달 할 수 있는 최단시간

    for i in range(alp, max_alp_req + 1):
        for j in range(cop, max_cop_req + 1):
            if i < max_alp_req:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j < max_cop_req:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    new_alp = min(i + alp_rwd, max_alp_req)  # 둘중 하나라도 목표값을 넘어가면 안된다.
                    new_cop = min(j + cop_rwd, max_cop_req)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j] + cost)

    return dp[max_alp_req][max_cop_req]
