import sys

input = sys.stdin.readline

N, M = map(int, input().split())
li = [[0] * (N+1)]

# 리스트에 전체 값 넣기, 다만 리스트 범위 확보를 위한 첫번째 행과 첫번째 열에 0 값 넣기
for _ in range(N):
    num = [0] + [int(x) for x in input().split()]
    li.append(num)

# 행 기준으로 누적합
for i in range(1, N+1):
    for j in range(1, N):
        li[i][j+1] += li[i][j]

# 열 기준으로 누적합
for j in range(1, N+1):
    for i in range(1, N):
        li[i+1][j] += li[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    #인덱스까지의 누적합을 다음 인덱스로 넘기므로, 인덱스 위치까지의 누적합은 그 전 값, 
    # 아닐 경우 인덱스 범위 초과로 에러 발생
    print(li[x2][y2] - (li[x1-1][y2] + li[x2][y1-1]) + li[x1-1][y1-1])
