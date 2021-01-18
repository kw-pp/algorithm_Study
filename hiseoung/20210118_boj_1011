num = int(input())
dist = []

for i in range(0, num):
    a, b = input().split()
    a = int(a)
    b = int(b)
    dist.append(b-a)


for x in range(0, num):

    i = 1
    count = 0

    while True:
        i += 1
        if i * i > dist[x]:
            break

    if (i - 1) * (i - 1) == dist[x]:
        count = 2 * (i - 1) - 1

    elif (i-1)*(i-1) + ((i*i - (i-1)*(i-1))/2) >= dist[x]:
        count = 2 * i - 2

    else:
        count = 2*i-1

    print(count)
