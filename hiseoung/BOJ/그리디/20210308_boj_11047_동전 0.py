n, k = map(int, input().split())
coin = []

for i in range(n):
    coin.append(int(input()))

coin.sort(reverse=True)
count = 0
i = 0

while True:
        if k == 0:
            break
        if k >= coin[i]:
            k -= coin[i]
            count += 1
        else:
           i += 1
print(count)
