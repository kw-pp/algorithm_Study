from collections import defaultdict


def solution(X, Y):
    answer = ''

    x = list(X)
    y = list(Y)

    dict_x = defaultdict(int)
    dict_y = defaultdict(int)

    for i in x:
        dict_x[i] += 1
    for i in y:
        dict_y[i] += 1

    for i in range(9, -1, -1):
        key = str(i)
        if key in dict_x.keys() and key in dict_x.keys():
            answer += key * (min(dict_x[key], dict_y[key]))

    if len(answer) == 0:
        answer = "-1"
    elif answer[0] == "0":
        answer = "0"

    return answer
