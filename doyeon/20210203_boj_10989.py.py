import sys
# 값을 입력받지 않고 값을 저장하는 방법 외우기
input = sys.stdin.readline
# 0부터 10000까지 index를 가진 리스트 생성
num_list = [0 for x in range(10001)]
case = int(input())
# 입력받은 숫자의 index를 1씩 증가
for x in range(case):
  num_list[int(input())] += 1
# 리스트 앞부터 값이 0이 아니면 출력
for i in range(10001):
  if num_list[i] != 0:
    for j in range(num_list[i]):
      print(i)