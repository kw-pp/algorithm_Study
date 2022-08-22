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
    flag = False
    for j in range(n, i):
        val = euclid(i, j)
        if val == 1:
            pass
        else:
            flag = True
            count += 1
    if flag:
        answer += i - (count * 2)
    else:
        answer += i - 1

print(answer)
