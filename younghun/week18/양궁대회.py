from itertools import combinations_with_replacement
from collections import defaultdict


def compare(ryan, apeach, win_dict):  # 승패 판단
    ryan_score = 0
    apeach_score = 0

    for i in range(11):  # 점수 계산
        if apeach[i] >= ryan[i]:
            if apeach[i] == 0:
                continue
            apeach_score += 10 - i
        else:
            ryan_score += 10 - i

    if ryan_score > apeach_score:  # 라이언이 이겼으면 win_dict에 {점수 차 : [라이언 결과들]} 형태로 같은 점수 차를 갖는 라이언 결과들을 모음
        win_dict[ryan_score - apeach_score].append(ryan)
    return win_dict


def solution(n, info):
    cases = list(combinations_with_replacement([i for i in range(11)], n))
    cands = []
    win_dict = defaultdict(list)

    for case in cases:  # 중복조합을 이용하여 라이언을 쏠 수 있는 모든 경우의 수를 구함
        ryan = [0] * 11
        for i in case:
            ryan[i] += 1
        cands.append(ryan)

    for cand in cands:
        win_dict = compare(cand, info, win_dict)  # 이긴 것만 win_dict에 기록

    if not win_dict:  # 한번도 이길 수 없다면
        return [-1]

    target = win_dict[max(win_dict.keys())]  # 점수 차가 가장 큰 라이언 결과들
    target.sort(key=lambda x: tuple([-x[i] for i in range(10, -1, -1)]))  # 문제의 조건에 따라 정렬
    return target[0]
