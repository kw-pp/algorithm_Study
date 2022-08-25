import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
vip = [int(input().split()[0]) for _ in range(m)]
seats = [i for i in range(1, n+1)]

dp = [0] * 41
count = 0
answer = 1

vip.sort(reverse=True)

def fibo(n):
    if n == 0 or n == 1:
        return 1
    if dp[n]:
        return dp[n]
    else:
        dp[n] = fibo(n-1) + fibo(n-2)
        return dp[n]


for i in range(n+1):
    if i == n:
        answer *= fibo(count)
    if vip and seats[i] == vip[-1]:
        vip.pop()
        answer *= fibo(count)
        count = 0
    else:
        count += 1
print(answer)