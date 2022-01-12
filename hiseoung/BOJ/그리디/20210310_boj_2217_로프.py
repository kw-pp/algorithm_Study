# 2217
# N(1 <= N <= 100,000)
n = int(input())

a = []
for i in range(n):
    a.append(int(input()))

a.sort()
Max = float('-inf')

for i in range(len(a)):
    w = a[i] * (len(a) - i)
    if Max < w:
        Max = w

print(Max)
