import sys
from collections import deque

n, w, L = map(int, sys.stdin.readline().split())
car_list = list(map(int, sys.stdin.readline().split()))
car_list.reverse()
bridge = deque()

# 시작값을 배열에 입력
t = 1
bridge.append(car_list.pop())

# bridge 리스트에 포함된 값들의 합이 0이면 ( 다리에 올라가 있는 트럭이 없으면 ) 탈출
while sum(bridge) != 0:
    # 다리 끝까지 왔다면 리스트에서 pop
    if len(bridge) == w:
        bridge.pop()

    # 기다리고 있는 차들의 무게 val 선언
    if len(car_list) != 0:
        val = car_list[-1]
    else:
        val = 0

    # 다리가 버틸 수 있는 하중을 넘어서면 0을 추가
    if sum(bridge) + val > L or len(car_list) == 0:
        bridge.appendleft(0)

    # 다리가 버틸 수 있는 무게라면 기다리고 있는 마지막 차를 리스트에 추가
    else:
        bridge.appendleft(car_list.pop())

    # 시간 Count
    t += 1

print(t)
