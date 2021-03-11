num = int(input())

dt = [0 for _ in range(num)]

for i in range(0, num):
    dt[i] = list(map(int, input().split()))

result = []
summation = 0

for i in range(0, num):
    for j in range(1, len(dt[i])):
        summation += dt[i][j]
    m = summation / dt[i][0]
    result.append(m)
    summation = 0


count = 0

for i in range(0, num):
    for j in range(1, len(dt[i])):
        if dt[i][j] > result[i]:
         count += 1

    ratio = float(count) / (dt[i][0]) * 100
    print("%.3f" % ratio + "%")
    count = 0
