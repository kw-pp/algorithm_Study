from collections import deque


def solution(priorities, location):
    loc = []
    for i in range(len(priorities)):
        loc.append(i)

    target = loc[location]
    q = deque(priorities)
    loc = deque(loc)
    answer = 0

    while True:
        x = q.popleft()
        y = loc.popleft()
        if len(q) != 0:
            Max = max(q)
        else:
            answer += 1
            break

        if x < Max:
            q.append(x)
            loc.append(y)
        else:
            answer += 1
            if y == target:
                break

    return answer