from collections import defaultdict


def solution(want, number, discount):
    answer = 0
    membership_term = 10
    want_dict = dict(zip(want, number))

    for i in range(len(discount) - 9):
        discount_dict = defaultdict(int)

        for j in range(i, i + membership_term):
            discount_dict[discount[j]] += 1

        if want_dict == discount_dict:
            answer += 1

    return answer
