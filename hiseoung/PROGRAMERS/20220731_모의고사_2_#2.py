from collections import deque
from collections import Counter

def solution(topping):
    answer = 0
    topping_dict = Counter(topping)

    prev = deque([])
    next = deque(topping)

    prev_set = set()
    next_set = set(topping)


    for i in range(len(topping)):
        val = next.popleft()

        prev.append(val)
        prev_set.add(val)

        topping_dict[val] -= 1

        if topping_dict[val] == 0:
            next_set.remove(val)

        if len(prev_set) == len(next_set):
            answer += 1

    return answer