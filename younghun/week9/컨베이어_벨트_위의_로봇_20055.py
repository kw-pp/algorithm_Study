import sys


class Cell:
    def __init__(self, durability, on_robot):
        self.durability = durability
        self.on_robot = on_robot

    def __str__(self):
        return "({0}, {1})".format(self.durability, self.on_robot)


n, k = map(int, sys.stdin.readline().split())
durability_list = list(map(int, sys.stdin.readline().split()))
conveyor_belt = [Cell(i, False) for i in durability_list]
phase = 0

while True:
    phase += 1

    ex_cell = conveyor_belt[0]
    for i in range(1, 2 * n):  # 회전
        temp_cell = conveyor_belt[i]
        conveyor_belt[i] = ex_cell
        ex_cell = temp_cell

        if i == 2 * n - 1:
            conveyor_belt[0] = ex_cell
    conveyor_belt[n - 1].on_robot = False

    for i in range(n-2, -1, -1):  # 로봇 이동
        if conveyor_belt[i].on_robot:
            if not conveyor_belt[i + 1].on_robot and conveyor_belt[i + 1].durability > 0:
                conveyor_belt[i].on_robot = False
                conveyor_belt[i + 1].on_robot = True
                conveyor_belt[i + 1].durability -= 1
                conveyor_belt[n - 1].on_robot = False

    if conveyor_belt[0].durability > 0:  # 로봇 올려놓기
        conveyor_belt[0].on_robot = True
        conveyor_belt[0].durability -= 1

    zero_cnt = 0
    for cell in conveyor_belt:  # 종료조건 체크
        if cell.durability == 0:
            zero_cnt += 1

    if zero_cnt >= k:
        break
print(phase)
