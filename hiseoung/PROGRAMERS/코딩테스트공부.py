def solution(alp, cop, problems):
    # DP 배열 범위 조정을 위해 알고력, 코딩력 최댓값 계산
    alp_max = sorted(problems, key=lambda x:x[0], reverse=True)[0][0]
    cop_max = sorted(problems, key=lambda x:x[1], reverse=True)[0][1]

    # 현재 가진 알고력, 코딩력으로 문제를 모두 풀 수 있다면 종료
    if alp >= alp_max and cop >= cop_max:
        return 0

    # 각 코딩 문제를 풀 수 있는 능력과 현재 능력 중 큰 값을 DP 배열 최댓값으로 사용
    alp_max = alp_max if alp_max >= alp else alp
    cop_max = cop_max if cop_max >= cop else cop
    dp = [[0] * (cop_max + 2) for _ in range(alp_max + 2)]

    for i in range(alp + 1, alp_max + 2):
        for j in range(cop + 1, cop_max + 2):
            # 시작 지점인 경우 패스
            if i == alp + 1 and j == cop + 1:
                continue
            # 코딩력 순회시작 하는 경우 ( 공부 )
            if j == cop + 1:
                dp[i][j] = dp[i-1][j] + 1
            # 알고력 순회시작 하는 경우 ( 공부 )
            elif i == alp + 1:
                dp[i][j] = dp[i][j - 1] + 1
            # 왼쪽 값( 코딩력 공부 ) 위쪽 값( 알고력 공부 )을 비교해서 작은 값을 현재 값에 저장
            else:
                dp[i][j] = min(dp[i][j - 1] + 1, dp[i - 1][j] + 1)

            # 문제 풀이 경우
            for q in problems:
                # 앞에 두개 조건은 참조하는 칸의 알고력, 코딩력이 해당 문제를 풀 수 있는지 체크
                # 뒤에 두개 조건은 참조하는 칸이 DP 배열 시작 범위에 들어가는지 체크
                if i - q[2] >= q[0] + 1 and j - q[3] >= q[1] + 1 and i - q[2] >= alp + 1 and j - q[3] >= cop + 1:
                    dp[i][j] = min(dp[i][j], dp[i - q[2]][j - q[3]] + q[4])
                # 기존 알고력, 코딩력 중 코딩력 조건 만족하고, 알고력 만족하지 못하는 경우
                if i - q[2] >= q[0] + 1 and i - q[2] >= alp + 1 and cop == cop_max:
                    dp[i][j] = min(dp[i][j], dp[i - q[2]][j] + q[4])
                # 기존 알고력, 코딩력 중 알고력 조건 만족하고, 코딩력 만족하지 못하는 경우
                if j - q[3] >= q[1] + 1 and j - q[3] >= cop + 1 and alp == alp_max:
                    dp[i][j] = min(dp[i][j], dp[i][j - q[3]] + q[4])
    return dp[-1][-1]