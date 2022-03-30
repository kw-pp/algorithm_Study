def factorial(num):
  if num > 1:
    return num * factorial(num-1)
  else:
    return 1

T = int(input())

for _ in range(T):
  N, M = map(int, input().split())
  print(factorial(M) // (factorial(N) * factorial(M-N)))
