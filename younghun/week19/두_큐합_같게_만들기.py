from collections import deque


def solution(queue1, queue2):
    answer = 0
    target = (sum(queue1) + sum(queue2)) // 2

    q1 = deque(queue1)
    q2 = deque(queue2)

    sum_val = sum(q1)

    while sum_val != target:

        if sum_val < target:
            item = q2.popleft()
            q1.append(item)
            sum_val += item
        else:
            item = q1.popleft()
            sum_val -= item

        if not q2:
            return -1

        answer += 1

    return answer
