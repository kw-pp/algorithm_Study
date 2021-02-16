n, m =map(int, input().split())
count2 = 0
count5 = 0

for i in range(1, n+1):
    i = 5**i
    if i > n:
        break
    count5 += n//i

for i in range(1, n+1):
    i = 5**i
    if i > n-m:
        break
    count5 -= (n-m) // i

for i in range(1, n+1):
    i = 5**i
    if i > m:
        break
    count5 -= m // i

for i in range(1, n+1):
    i = 2**i
    if i > n:
        break
    count2 += n//i

for i in range(1, n+1):
    i = 2**i
    if i > n-m:
        break
    count2 -= (n-m) // i

for i in range(1, n+1):
    i = 2**i
    if i > m:
        break
    count2 -= m // i

if count5 >= count2:
    print(count2)
else:
    print(count5)

