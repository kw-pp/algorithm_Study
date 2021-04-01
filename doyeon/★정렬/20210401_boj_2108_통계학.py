import sys
from collections import Counter

input = sys.stdin.readline
n = int(input())
li = []
for _ in range(n):
  li.append(int(input()))
li.sort()

def mode(x):
  mode_dict = Counter(x)
  modes = mode_dict.most_common()
  if len(x) > 1:
    if modes[0][1] == modes[1][1]:
      mod = modes[1][0]
    else:
      mod = modes[0][0]
  else:
    mod = modes[0][0]
  return mod

# 산술평균
print(round(sum(li)/n))
# 중앙값
print(li[n//2])
# 최빈값
print(mode(li))
# 범위
print(li[-1] - li[0])