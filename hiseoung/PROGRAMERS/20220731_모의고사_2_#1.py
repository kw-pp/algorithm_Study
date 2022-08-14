from itertools import combinations

def solution(number):
    student_list = list(range(1, len(number) + 1))
    num_dict = dict(zip(student_list, number))
    three_list = list(combinations(student_list, 3))
    answer = 0

    for a,b,c in three_list:
        val = num_dict[a] + num_dict[b] + num_dict[c]

        if val == 0:
            answer += 1

    return answer