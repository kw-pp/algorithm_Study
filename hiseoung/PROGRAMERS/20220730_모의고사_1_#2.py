import copy

def solution(want, number, discount):
    answer = 0
    want_list = dict()
    for i in range(len(want)):
        want_list[want[i]] = number[i]

    for i in range(len(discount) - 9):
        temp = discount[i:i+10]
        temp_dict = copy.deepcopy(want_list)
        count = 0

        for j in temp:
            if temp_dict.get(j, 0) > 0:
                temp_dict[j] -= 1
                count += 1
        if count == 10:
            answer += 1

    return answer