import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
num_arr = list(map(int, input().split()))
op_arr = list(map(int, input().split()))
op_li = ['+', '-', '*', '//']
op = []

for i in range(4):
  for _ in range(op_arr[i]):
    op.append(op_li[i])

max_cnt = (-10)**9
min_cnt = 10**9

def solution(N):
  global max_cnt, min_cnt
  for li in permutations(op):
    answer = num_arr[0]
    
    for j in range(N-1):
      if li[j] == '+':
        answer += num_arr[j+1]
      elif li[j] == '-':
        answer -= num_arr[j+1]
      elif li[j] == '*':
        answer *= num_arr[j+1]
      elif li[j] == '//':
        if answer >= 0:
          answer //= num_arr[j+1]
        else:
          #이전값을 다 더하였을때 음수이면 예외처리
          answer = -answer // num_arr[j+1]
          answer = -answer
    
    max_cnt = max(answer, max_cnt)
    min_cnt = min(answer, min_cnt)

solution(N)
print(max_cnt)
print(min_cnt)
