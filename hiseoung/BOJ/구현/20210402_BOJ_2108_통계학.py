import sys
from collections import Counter

n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append(int(sys.stdin.readline()))

# 산술평균
r1 = sum(a) / n
print(round(r1))

# 중앙값
a.sort()
idx = n // 2
r2 = a[idx]
print(r2)

# 최빈값
Max = float('-inf')
r = []
count = Counter(a).most_common()
for k, v in count:
    if v > Max:
        Max = v
        r = [k]
    elif v == Max:
        r.append(k)
if len(r) > 1:
    r.sort()
    print(r[1])
else:
    print(r[0])

# 범위
print(a[-1]-a[0])
