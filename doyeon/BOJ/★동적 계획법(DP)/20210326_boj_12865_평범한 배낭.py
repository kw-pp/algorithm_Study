# 0-1 knapsack problem
# https://dojinkimm.github.io/algorithm/2019/10/19/dp-2.html 참고
import sys

r = sys.stdin.readline
n,k = map(int, r().split())
bag = [tuple(map(int, r().split())) for _ in range(n)]

knap = [0 for _ in range(k+1)]

for i in range(n):
  for j in range(k, 1, -1):
    if bag[i][0] <= j:
      # knap[j-bag[i][0]] 은 기존의 index에서 새로 들어온 물품의 무게를 뺀 것
      knap[j] = max(knap[j], knap[j-bag[i][0]] + bag[i][1])
  print(knap)
print(knap[-1])