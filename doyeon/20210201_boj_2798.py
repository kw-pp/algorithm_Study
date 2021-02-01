N, M = map(int, input().split())
A = list(map(int, input().split()))

result = 0
for i in range(N):
  for j in range(i+1, N):
    for k in range(j+1, N):
      sumit = A[i] + A[j] + A[k]
      if sumit <= M:
        result = max(result, sumit)
print(result)


  