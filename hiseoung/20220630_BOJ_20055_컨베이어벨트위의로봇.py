import sys
from itertools import islice
from collections import deque
from collections import Counter

input = sys.stdin.readline

def rotate():
    # 벨트를 회전시킨다.
    temp = belt[0].pop()
    belt[1].append(temp)
    temp = belt[1].popleft()
    belt[0].appendleft(temp)

    # 로봇의 위치도 동일하게 변경한다.
    temp = robot[0].pop()
    robot[1].append(temp)
    temp = robot[1].popleft()
    robot[0].appendleft(temp)

    # 로봇이 내리는 위치에 도착했으면 로봇을 옮긴다.
    if robot[0][-1] == 1:
        robot[0][-1] = 0


N, K = map(int, input().split())
belt = iter(list(map(int, input().split())))
belt = [deque(islice(belt, elem)) for elem in [N, N]]
robot = [deque(0 for _ in range(N)) for _ in range(2)]
answer = 0


while True:
    answer += 1

    # 1. 회전을 한다.
    rotate()

    # 2. 로봇을 이동시킨다.
    for i in range(N-2, 0, -1):
        # 현재 위치에 로봇이 있고, 이동 위치에 로봇이 없으며, 벨트의 내구도가 0이 아니라면
        if robot[0][i] == 1 and not robot[0][i+1] and belt[0][i+1] != 0:
            belt[0][i+1] -= 1
            robot[0][i+1] = 1
            robot[0][i] = 0

            # 로봇이 내리는 위치에 도착했으면 로봇을 옮긴다.
            if robot[0][-1] == 1:
                robot[0][-1] = 0

    # 3. 올리는 위치에 벨트의 내구도가 남아 있는 경우 로봇을 올린다.
    if belt[0][0] != 0:
        robot[0][0] = 1
        belt[0][0] -= 1

    # 4. 벨트의 내구도가 지정 값에 도달했으면 종료한다.
    val = Counter(belt[0])[0] + Counter(belt[1])[0]

    if val >= K:
        break


print(answer)



