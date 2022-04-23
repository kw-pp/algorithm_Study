import sys

input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0, 0, 0] for _ in range(N)]

answer = 1000 * 1000 + 1

#처음 색 선택
for j in range(3):
  dp[0][j] = arr[0][j]
  dp[0][j-1] = 1001
  dp[0][(j+1)%3] = 1001
  
  #다음 색 각각 선택하는 방식
  for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
    dp[i][1] = min(dp[i-1][2], dp[i-1][0]) + arr[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]
  
  #마지막에 처음 색 겹치는 경우 제외하고 비교하기
  for i in range(3):
    if i != j:
      answer = min(answer, dp[-1][i])

print(answer)
