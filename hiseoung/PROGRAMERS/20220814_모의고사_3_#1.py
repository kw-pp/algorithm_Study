import sys
sys.setrecursionlimit(10**9)

def dfs(a, b, coke, bottle, result):
    # 콜라와 빈병의 합이 a개 미만이면 재귀를 종료한다.
    if a > coke:
        if a <= coke + bottle:
            return dfs(a,b,coke+bottle,0,result)
        else:
            return result
    # 몫 계산
    k = (coke // a) * b

    # 나머지 계산
    bottle += coke % a

    # 교환한 콜라 개수를 추가해준다
    result += k
    return dfs(a, b, k, bottle, result)

def solution(a, b, n):
    return dfs(a, b, n, 0, 0)