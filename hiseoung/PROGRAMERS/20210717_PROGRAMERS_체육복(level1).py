def solution(n, lost, reserve):
    breaker = False
    for i in reserve:
        if breaker:
            break
        p = 0
        for j in range(len(lost)):
            if lost[p] == i+1 or lost[p] == i-1:
                del lost[p]
                break
            else:
                p += 1
            if len(lost) == 0:
                breaker = True
                break
    return n - len(lost)