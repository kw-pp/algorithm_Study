def solution(a, b, n):
    answer = 0

    while n >= a:
        new_bottle = n // a * b
        n %= a
        answer += new_bottle
        n += new_bottle

    return answer
