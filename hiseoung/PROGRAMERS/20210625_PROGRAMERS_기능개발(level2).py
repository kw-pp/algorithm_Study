from collections import deque


def solution(progresses, speeds):
    answer = []
    while progresses:
        for i in range(len(progresses)):
            if progresses[i] < 100:
                progresses[i] += speeds[i]

        count = 0

        for _ in range(len(progresses)):
            if progresses[0] >= 100:
                count += 1
                progresses.pop(0)
                speeds.pop(0)
            else:
                break
        if count:
            answer.append(count)

    return answer