import sys
input = sys.stdin.readline

N, M = map(int, input().split())

name_dic = {}
num_dic = {}
for i in range(N):
  poketmon = input().strip()
  name_dic[poketmon] = i
  num_dic[i] = poketmon

for _ in range(M):
  prob = input().rstrip()
  if prob[0].isdigit() == 1: #문제가 숫자일때
    print(num_dic[int(prob)-1])
  else:
    print(name_dic[prob]+1)
