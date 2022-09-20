from collections import deque

def solution(queue1, queue2):
    n = len(queue1)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    prev_sum = sum(queue1)
    next_sum = sum(queue2)
    cnt = 0

    while prev_sum != next_sum:
        if cnt >= 3 * n:
            break
        if prev_sum > next_sum:
            tmp = queue1.popleft()
            queue2.append(tmp)
            prev_sum -= tmp
            next_sum += tmp
            cnt += 1
        elif prev_sum < next_sum:
            tmp = queue2.popleft()
            queue1.append(tmp)
            next_sum -= tmp
            prev_sum += tmp
            cnt += 1
    if prev_sum == next_sum:
        return cnt
    else:
        return -1

