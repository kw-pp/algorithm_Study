from collections import deque
import sys

#백준

t = int(sys.stdin.readline())

for _ in range(t):
    n, w = map(int, sys.stdin.readline().split())
    priorities = []
    for i in range(n):
        priorities.append(list(map(int, sys.stdin.readline().split())))
    if len(priorities) == 1:
        print(1)
        continue

    loc = []
    for i in range(len(priorities)):
        loc.append(i)

    target = loc[w]
    q = deque(priorities)
    loc = deque(loc)
    answer = 0

    while True:
        x = q.popleft()
        y = loc.popleft()
        Max = max(q)

        if y == target and x >= Max:
            answer += 1
            break

        if x < Max:
            q.append(x)
            loc.append(y)
        else:
            answer += 1
    print(answer)

from collections import deque

#프로그래머스
def solution(priorities, location):
    loc = []
    if len(priorities) == 1:
        return 1
    for i in range(len(priorities)):
        loc.append(i)

    target = loc[location]
    q = deque(priorities)
    loc = deque(loc)
    answer = 0

    while True:
        x = q.popleft()
        y = loc.popleft()
        Max = max(q)

        if y == target and x >= Max:
            answer += 1
            break

        if x < Max:
            q.append(x)
            loc.append(y)
        else:
            answer += 1

    return answer
