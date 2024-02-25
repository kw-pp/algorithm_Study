from itertools import combinations

def solution(number):
    answer = 0
    combo = list(combinations(number, 3))
    for idx, e in enumerate(combo):
        if sum(e) == 0:
            answer += 1
    return answer
