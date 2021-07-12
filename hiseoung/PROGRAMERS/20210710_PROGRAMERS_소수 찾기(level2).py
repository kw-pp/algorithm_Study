# https://kokooroom.tistory.com/4

import itertools

def solution(numbers):
    number = list(numbers)
    li = []
    for i in range(1, (len(number) + 1)):
        temp = list(map(int, (list(map(''.join, itertools.permutations(number, i))))))
        li.extend(temp)

    li = list(set(li))
    count = 0

    for i in li:
        if i == 1 or i == 0:
            continue
        # x = int(i **(1/2))
        check = False
        for j in range(2, i):
            if i % j == 0:
                break

        else:
            check = True
        if check:
            count += 1

    return count

