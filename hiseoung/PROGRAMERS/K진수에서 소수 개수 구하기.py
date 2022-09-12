import string
import math
tmp = string.digits+string.ascii_lowercase

def is_prime_num(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


def solution(n, k):
    is_converted = convert(int(n), k)
    is_converted = is_converted.split('0')
    is_converted = map(lambda x:int(x) if x != '' else 1, is_converted)
    cnt = 0

    for i in is_converted:
        if is_prime_num(i) and i != 1:
            cnt += 1
    return cnt
