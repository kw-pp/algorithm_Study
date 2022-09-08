import math


def is_prime_num(num):  # 소수인지 판별
    if num == 1:
        return False

    for i in range(2, int(math.sqrt(num) + 1)):  # num의 제곱근까지만 보면 그 이후론 대칭임
        if num % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    k_num = 0
    multiple = 1

    while n >= k:  # k진수 만들어주기
        k_num += (n % k) * multiple
        n = n // k
        multiple *= 10
    k_num += n * multiple

    cand = str(k_num).split('0')  # 0 기준으로 분리

    for i in cand:
        if i.isdigit() and is_prime_num(int(i)):  # 숫자이면서 소수이면 조건을 만족
            answer += 1

    return answer
