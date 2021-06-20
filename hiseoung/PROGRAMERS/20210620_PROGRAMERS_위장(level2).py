def solution(clothes):
    table = {}
    for i in clothes:
        if table.get(i[1]) != None:
            table[i[1]] += 1
        else:
            table[i[1]] = 2
    answer = 1

    for v in table.values():
        answer *= v

    return answer - 1