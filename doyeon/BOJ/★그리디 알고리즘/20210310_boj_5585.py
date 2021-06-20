x = 1000 - int(input())
count = 0
change = [500, 100, 50, 10, 5, 1]
for i in change:
  count += x // i
  x = x%i
print(count)