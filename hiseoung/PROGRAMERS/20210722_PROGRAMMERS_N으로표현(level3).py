from collections import deque

N = 2
number = 11
answer = 0

if N == number:
    answer = 1
    # return 1
else:
    q = deque()
    q.append(N)
    breaker = False
    while q:
        if breaker:
            break
        if answer > 8:
            answer = -1
        answer += 1
        temp = []
        for _ in range(len(q)):
            x = q.pop()
            if x == number:
                breaker = True
                break
            temp.append(int(str(N) * (answer + 1)))
            temp.append(x + N)
            temp.append(x - N)
            temp.append(N - x)
            temp.append(x * N)
            temp.append(x // N)
            if x != 0:
                temp.append(N // x)
        q = deque((set(temp)))
