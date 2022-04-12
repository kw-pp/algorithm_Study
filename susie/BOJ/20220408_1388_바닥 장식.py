N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
sign = 0
answer = 0

for i in range(N):
  for j in range(M):
    if arr[i][j] == '-':
      sign = 1

    if sign == 1 and j == M-1:
      sign = 0
      answer += 1
      continue

    if sign == 1 and arr[i][j] == '|':
      answer += 1
      sign = 0

for j in range(M):
  for i in range(N):
    if arr[i][j] == '|':
      sign = 1

    if sign == 1 and i == N-1:
      sign = 0
      answer += 1
      continue

    if sign == 1 and arr[i][j] == '-':
      answer += 1
      sign = 0

if N == 1 and M == 1:
  answer = 1
print(answer)
