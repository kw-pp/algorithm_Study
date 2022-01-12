import sys

def solution(n, arr):
    '''
    출처 : https://www.acmicpc.net/problem/2156
    티어 : 실버1
    분류 : 다이나믹 프로그래밍
    - 시간복잡도 : O(N)
    - 문제 풀이 시간 : 약 1시간
    - Bottom-up
    - 테이블로 넘어오는 모든 케이스를 고려해야 풀리는 문제
    '''

    # TODO 점화식 세우는 연습!

    # 값을 저장할 DP테이블을 선언합니다.
    # 리스트를 선언하는 해당 포맷을 기억합시다!
    # 이런식으로 만들지 않으면 값을 수정할 때 같은 컬럼 내의 값이 모두 바뀜
    dp = [[0] * n for _ in range(2)]

    # 주어진 배열 길이 만큼 반복문으로 DP테이블을 처리합니다.
    for i in range(n):
        # i = 1,2,3인 경우 인덱스 오류를 고려해서 각각 값을 선언 및 초기화합니다.
        if i == 0:
            dp[i][0] = arr[0]
            dp[1][i] = 0
        elif i == 1:
            dp[0][i] = dp[0][0] + arr[i]
            dp[1][i] = arr[i]
        elif i == 2:
            dp[0][i] = dp[0][0] + arr[i]
            dp[1][i] = dp[1][1] + arr[i]

        # 해당 순번의 포도주 최댓값을 구할 때 이전에 구한 모든 포도주의 최댓값을 참조해야 합니다.
        else:
            dp[0][i] = max(max(dp[0][:i-1]), max(dp[1][:i-1])) + arr[i]
            dp[1][i] = dp[0][i-1] + arr[i]

    return max(map(max, dp))


n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))
print(solution(n, arr))
