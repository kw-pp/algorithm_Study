import sys

d = [0] * 101
def fibo(x):

    if x == 1 or x == 2 or x == 3:
        return 1

    if d[x] != 0:
        return d[x]

    d[x] = fibo(x-2) + fibo(x-3)
    return d[x]


n = int(sys.stdin.readline())
for i in range(n):
    num = int(sys.stdin.readline())
    print(fibo(num))