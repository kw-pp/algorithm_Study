def solution(brown, yellow):
    total = brown + yellow
    li = []

    for i in range(2, total):
        temp = (i, int(total / i))
        li.append(temp)

    for _ in range(len(li)):
        if li:
            x, y = li.pop()
            if x >= y and (x - 2) * (y - 2) == yellow:
                answer = (x, y)
                break
            else:
                continue

    return answer