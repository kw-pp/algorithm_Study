import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
for i in range(1, n):
    # 현재값과 이전에 더해온 값을 비교해서 큰 값을 저장함(DP)
    a[i] = max(a[i], a[i-1] + a[i])
print(max(a))
