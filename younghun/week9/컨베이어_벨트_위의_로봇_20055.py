import sys
from collections import deque


class Cell:
    def __init__(self, durability, on_robot):
        self.durability = durability
        self.on_robot = on_robot


n, k = map(int, sys.stdin.readline().split())
durability_list = list(map(int, sys.stdin.readline().split()))
conveyor_belt = deque([Cell(i, False) for i in durability_list])
phase = 0
zero_cnt = 0

while zero_cnt < k:
    phase += 1

    conveyor_belt.rotate()
    conveyor_belt[n - 1].on_robot = False

    for i in range(n-2, -1, -1):  # 로봇 이동
        if conveyor_belt[i].on_robot:
            if not conveyor_belt[i + 1].on_robot and conveyor_belt[i + 1].durability > 0:
                conveyor_belt[i].on_robot = False
                conveyor_belt[i + 1].on_robot = True
                conveyor_belt[i + 1].durability -= 1

                if conveyor_belt[i + 1].durability == 0:
                    zero_cnt += 1
                conveyor_belt[n - 1].on_robot = False

    if conveyor_belt[0].durability > 0:  # 로봇 올려놓기
        conveyor_belt[0].on_robot = True
        conveyor_belt[0].durability -= 1

        if conveyor_belt[0].durability == 0:
            zero_cnt += 1

print(phase)
