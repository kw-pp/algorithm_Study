import sys


def solution(time, pay):
    dp = [0] * (N + 1)  # dp 배열 정의 : i일 까지의 최대 수익.

    for i in range(N - 1, -1, -1):
        # i일에 상담을 하는 것이 퇴사일을 넘기면 상담을 하지 않음
        if i + T[i] > N:
            dp[i] = dp[i + 1]
        else:
            # i일에 상담을 하는 것과 상담을 안하는 것 중 큰 것을 선택
            dp[i] = max(dp[i + 1], P[i] + dp[i + T[i]])

    return dp[0]


N = int(sys.stdin.readline())

T, P = [], []

for _ in range(N):
    t, p = map(int, sys.stdin.readline().split())
    T.append(t)
    P.append(p)

print(solution(T, P))

