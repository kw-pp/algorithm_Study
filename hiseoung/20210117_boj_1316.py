num = int(input())
a = []

for i in range(0, num):
    a.append(input())

count = 0
for i in range(0, len(a)):

    c = []
    not_gb = True
    Breaker = False

    for j in range(0, len(a[i])):

        if Breaker:
            break

        try:
            c.append(a[i][j])

            if j == 0:
                continue

            if a[i][j] == a[i][j - 1]:
                continue

            for z in range(j+1, 1, -1):

                if a[i][j] != c[z-2]:
                    continue
                else:
                    not_gb = False
                    Breaker = True

        except IndexError:
            pass

    if not_gb == False:
        count += 1

result = num - count
print(result)
