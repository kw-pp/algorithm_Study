n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

m = price[0]
total = 0
for i in range(n-1):
  if price[i] < m:
    m = price[i]
  total += m * distance[i]
print(total)