#왜 이게 성립하는지 이해하지 못한 코드
#추가 이해 필요

n = int(input())
k = int(input())

answer = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i//2 + 1):
        if j == 1:
            answer[i][j] = i
        else:
            answer[i][j] = answer[i-1][j] + answer[i-2][j-1]
            answer[i][j] %= 1000000003

print(answer[n][k])
