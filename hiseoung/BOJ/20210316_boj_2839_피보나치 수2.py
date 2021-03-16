import sys
n = int(sys.stdin.readline())
d = [0] * 91

def fibo(n):
    if n == 1:
        return 1
    if n == 2:
        return 1

    if d[n] != 0:
        return d[n]

    d[n] = fibo(n-1) + fibo(n-2)
    return d[n]

print(fibo(n))
