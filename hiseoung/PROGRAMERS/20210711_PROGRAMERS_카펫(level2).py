brown = 12
yellow = 6

total = brown + yellow
li = []

for i in range(2, total):
    if total % i == 0:
        if len(li) != 0 and (int(total/i), i) == li[-1]:
            temp = (i, int(total / i))
            li.append(temp)
            break
        else:
            temp = (i, int(total/i))
            li.append(temp)

    print((li.pop()))

