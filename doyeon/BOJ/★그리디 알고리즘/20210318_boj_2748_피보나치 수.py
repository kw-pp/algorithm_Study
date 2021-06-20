n = int(input())
# a,b = 0,1
# for i in range(n):
#   a, b = b, a+b
# print(a)
d=[0]*91
d[0] = 0
d[1] = 1

# 피보나치 함수(Fibonacci Function) 반복문으로 구현(보텀업 다이나믹 프로그래밍)
for i in range(2, n+1):
  d[i] = d[i-1] + d[i-2]

print(d[n])