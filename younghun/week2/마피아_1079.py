import sys
from copy import deepcopy

answer = []
n = int(sys.stdin.readline())
temp = list(map(int, sys.stdin.readline().split()))
people_list = [[i, temp[i]] for i in range(len(temp))]
r = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
mafia = int(sys.stdin.readline())
cnt = 0
global escape_flag

escape_flag = False


def night(people, count):
    global escape_flag

    for i in people:
        if i[0] != mafia:
            temp_cnt = count
            temp_people = deepcopy(people)

            # print(1, temp_people)

            temp_people.remove(i)

            for j in range(len(temp_people)):
                temp_people[j][1] += r[i[0]][temp_people[j][0]]
            temp_cnt += 1

            # print(2, temp_people)

            if len(temp_people) == 1:
                answer.append(temp_cnt)
                escape_flag = True
                # print(temp_cnt)
                return

            temp_people.sort(key=lambda x: (x[1], -x[0]))
            target = temp_people.pop()

            if target[0] == mafia:
                answer.append(temp_cnt)
                continue

            if len(temp_people) == 1:
                answer.append(temp_cnt)
                escape_flag = True
                return
            # print(3, temp_people)

            night(temp_people, temp_cnt)
            if escape_flag:
                return
    return


if n % 2 != 0:
    people_list.sort(key=lambda x: (x[1], -x[0]))
    victim = people_list.pop()

    if victim[0] == mafia:
        answer.append(cnt)
    else:
        night(people_list, cnt)
else:
    night(people_list, cnt)

print(max(answer))
