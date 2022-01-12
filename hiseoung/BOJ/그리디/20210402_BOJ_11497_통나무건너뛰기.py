import sys

t = int(sys.stdin.readline())
answer = []

for i in range(t):
    n = int(sys.stdin.readline())
    li = list(map(int, sys.stdin.readline().split()))
    li.sort()
    temp = [0] * (len(li))
    x = 0
    y = len(li) - 1
    s = 1
    b = len(li) // 2
    while True:
        if temp[b] != 0 and temp[b-1] != 0:
            break
        if s % 2 == 0:
            temp[x] = li[s-1]
            x += 1
            s += 1
        else:
            temp[y] = li[s-1]
            y -= 1
            s += 1

    Max = float('-inf')
    for z in range(len(temp)):
        if z == len(temp) - 1:
            val = abs(temp[z] - temp[0])
            if val > Max:
                Max = val
        else:
            val = abs(temp[z] - temp[z+1])
            if val > Max:
                Max = val

    answer.append(Max)

for i in answer:
    print(i)

