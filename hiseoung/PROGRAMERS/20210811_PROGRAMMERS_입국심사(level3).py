def solution(n, times):
    '''
    출처 : https://programmers.co.kr/learn/courses/30/lessons/43238
    문제 유형 : 이분 탐색
    
    '''
    
    answer = 0
    left = 1
    right = max(times) * n

    while left <= right:
        mid = (left + right) // 2

        cnt = 0
        for time in times:
            cnt += (mid // time)

        #심사관이 주어진 시간동안 모든 사람을 처리할 수 있으면
        if cnt >= n:
            # 종료되기 전에 answer을 바꿔줌
            right = mid - 1
            answer = mid
        else:
            # 종료 조건 바뀌는 부분
            left = mid + 1

    return answer
