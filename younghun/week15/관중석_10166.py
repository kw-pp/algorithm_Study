import sys
from math import gcd


def solve():
    min_r, max_r = map(int, sys.stdin.readline().split())
    fractions = [[0] * max_r for _ in range(max_r)]
    answer = 0

    for i in range(min_r, max_r + 1):
        for j in range(1, i + 1):
            g = gcd(i, j)
            denominator = i // g  # 기약분수 분모
            numerator = j // g  # 기약분수 분자

            if not fractions[denominator - 1][numerator - 1]:
                fractions[denominator - 1][numerator - 1] = 1
                answer += 1

    print(answer)

solve()