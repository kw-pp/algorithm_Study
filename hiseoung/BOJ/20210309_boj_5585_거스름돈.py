n = int(input())

#거스름돈
rest = 1000 - n

a = [500, 100, 50, 10, 5, 1]
count = 0
i = 0

while True:
    if a[i] > rest:
        i += 1
        continue
    else:
        rest -= a[i]
        count += 1
        if rest == 0:
            break
print(count)

