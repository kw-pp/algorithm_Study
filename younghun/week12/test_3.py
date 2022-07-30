from collections import deque


def solution(order):
    answer = 0
    n = len(order)
    stack = []
    order = deque(order)

    for i in range(1, n + 1):
        if i == order[0]:
            order.popleft()
            answer += 1
        else:
            stack.append(i)
            continue

        if stack:
            if order[0] == stack[-1]:
                stack.pop(-1)
                order.popleft()
                answer += 1
    while stack:
        if order[0] == stack[-1]:
            stack.pop(-1)
            order.popleft()
            answer += 1
        else:
            break

    return answer
