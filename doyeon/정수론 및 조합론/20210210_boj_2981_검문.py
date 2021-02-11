# n개 숫자들의 차이 구해서 공약수들 구하기
import math
n = int(input())
nums = []

gcd = 0
for i in range(n):
  nums.append(int(input()))
  if i==1:
    gcd = abs(nums[1]-nums[0]) # 절댓값
  gcd = math.gcd(abs(nums[i]-nums[i-1]), gcd) # 최대공약수

# 최대공약수의 약수 구하기
output = []
gcd_a = int(gcd ** 0.5)
for i in range(2, gcd_a+1):
  if gcd % i == 0:
    output.append(i)
    output.append(gcd//i)
output.append(gcd)
output = list(set(output)) # 중복값 제거
output.sort()
for i in output:
  print(i, end=' ')