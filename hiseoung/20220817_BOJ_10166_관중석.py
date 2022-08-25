import sys

input = sys.stdin.readline

n, m = map(int, input().split())
answer = n


def euclid(a, b):
    c = a % b
    if c == 0:
        return b
    else:
        return euclid(b, c)


for i in range(n+1, m + 1):
    count = 0
    for j in range(n, i):
        val = euclid(i, j)
        if val == 1:
            pass
        else:
            count += val - 1
    print(i - count - 1)
    answer += i - count - 1

print(answer)