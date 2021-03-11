n = int(input())
b = []
c = []


idx = 0
breaker = 0

for i in range(n):

    f = int(input())

    while idx < f:
        idx += 1
        b.append(idx)
        c.append("+")

    if b[-1] == f:
        b.pop()
        c.append("-")

    else:
        breaker = 1
        break


if breaker:
    print('NO')
else:
    for i in range(len(c)):
        print(c[i])


