import sys
n = int(input())
people = []

for _ in range(n):
  a, b = map(int, sys.stdin.readline().split())
  people.append((a,b))
for i in people:
  rank = 1
  for j in people:
    if i[0] < j[0] and i[1] < j[1]:
      rank+=1
  print(rank, end=" ")