import sys
from collections import deque

roomNo = int(sys.stdin.readline())
roomPrice = {key: value for key, value in enumerate(list(map(int, sys.stdin.readline().split())))}
totalPrice = int(sys.stdin.readline())

tableDP = [[(i, roomPrice[i]) for i in range(roomNo-1, -1, -1)]]
priceTable = sorted(tableDP[0], key = lambda x:x[0], reverse=True)
q = deque(tableDP[-1])
temp = []

while q:
    temp = list(q)
    max_value = (0, 0)

    for _ in range(len(q)):
        x, y = q.popleft()
        for a, b in priceTable:
            if max_value[1] == 0 and y+b <= totalPrice and x != 0:
                room = (int(str(x) + str(a)))
                max_value = (room, y + b)
                q.append(max_value)
                continue

            if y+b < max_value[1] <= totalPrice:
                room = (int(str(x)+str(a)))
                max_value = (room, y+b)
                q.append(max_value)

if priceTable == temp:
        max = -1
        for i in range(len(temp)):
            if max < temp[i][1] <= totalPrice:
                max = temp[i][0]
        print(max)
else:
    print(temp[0][0])







