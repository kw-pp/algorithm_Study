from collections import deque


def make_n_num(decimal, n):  # 10진수를 n진수로 변환
    n_num = deque()

    if decimal == 0:
        n_num.appendleft(str(decimal))

    while decimal > 0:  # n으로 나눠가면서 나머지들을 queue에 왼쪽부터 넣어줌
        decimal, r = divmod(decimal, n)
        if r >= 10:  # 나머지가 10보다 크면 16진수로 바꿔줌
            r = hex(r)[2:].upper()
        n_num.appendleft(str(r))

    return n_num


def solution(n, t, m, p):
    answer = ''
    end = m * t + (p - 1)  # 튜브가 말해야하는 마지막 숫자
    nums = []  # n진수 배열
    decimal = 0

    while len(nums) < end:  # n진수 배열의 길이가 end가 되면 종료
        nums.extend(make_n_num(decimal, n))
        decimal += 1

    for i in range(t):  # 튜브가 말해야하는 숫자들
        answer += nums[m * i + (p - 1)]

    return answer
