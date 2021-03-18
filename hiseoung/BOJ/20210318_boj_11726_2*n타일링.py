import sys

n = int(sys.stdin.readline())
a = [1, 2]
# 상향식 접근
for i in range(2, n):
    a.append(a[i-1] + a[i-2])

print(a[n-1] % 10007)
