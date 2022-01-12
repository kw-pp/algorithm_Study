import sys

a = int(sys.stdin.readline())
d = [0] * 1001

def func(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if d[n] != 0:
        return d[n]
    else:
        d[n] = (func(n-1) + func(n-2)) % 10007
        return d[n]

print(func(a))
