import string
tmp = string.digits+string.ascii_uppercase

def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


def solution(n, t, m, p):
    result = ''
    num = 0
    cnt = 0
    while len(result) != t:
        is_converted = convert(num, n)
        for ch in is_converted:
            if len(result) == t:
                break
            cnt += 1
            if cnt == p:
                result += ch
            if cnt == m:
                cnt = 0
        num += 1

    return result