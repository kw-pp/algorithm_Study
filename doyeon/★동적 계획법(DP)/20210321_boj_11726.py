n = int(input())
d = [0]*1001
d[1] = 1
d[2] = 2
for i in range(3, n+1):
  d[i] = d[i-2]+d[i-1]
print(d[n]%10007)