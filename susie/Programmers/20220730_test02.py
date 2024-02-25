from collections import defaultdict
import copy

def solution(want, number, discount):
    answer = 0

    dic = defaultdict(int)
    for w, n in zip(want, number):
        dic[w] = n

    for day in range(len(discount)-9):
        renew_dic = copy.deepcopy(dic)
        for idx in range(10):
            if idx == 9 and renew_dic[discount[day+idx]]:
                answer += 1
                break

            if renew_dic[discount[day+idx]] == 0:
                break
            else:
                renew_dic[discount[day+idx]] -= 1
            
    return answer
