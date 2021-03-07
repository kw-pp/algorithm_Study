# https://god-gil.tistory.com/62 참고
n, m = map(int, input().split())
board =[]

for _ in range(n):
  board.append(input())

repair = []

for i in range(n-7):
  for j in range(m-7):
    first_W = 0
    first_B = 0
    for k in range(i,i+8):
      for l in range(j,j + 8):
        if (k + l) % 2 == 0:
          if board[k][l] != 'W':
            first_W = first_W+1
          if board[k][l] != 'B':
            first_B = first_B + 1
        else:
          if board[k][l] != 'B':
            first_W = first_W+1
          if board[k][l] != 'W':
            first_B = first_B + 1
    repair.append(first_W)
    repair.append(first_B)

print(min(repair))