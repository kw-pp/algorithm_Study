import sys

roomNo = int(sys.stdin.readline())
roomPrice = {key: value for key, value in enumerate(list(map(int, sys.stdin.readline().split())))}
totalPrice = int(sys.stdin.readline())

numberDP = [[i for i in range(roomNo)]]
priceDP = [[roomPrice[i] for i in range(roomNo)]]

while True:
    numTemp = []
    priceTemp = []
    for i in range(len(numberDP[-1])):
        if i == 0:
            priceTemp.append(0)
            numTemp.append(0)
        else:
            priceTemp.extend([priceDP[-1][i] + priceDP[0][x] for x in range(roomNo) if priceDP[-1][i] + priceDP[0][x] <= totalPrice])
            numTemp.extend([int(str(numberDP[-1][i]) + str(y)) for y in range(roomNo) if priceDP[-1][i] + priceDP[0][y] <= totalPrice])
    if sum(priceTemp) == 0:
        break
    numberDP.append(numTemp)
    priceDP.append(priceTemp)

if len(numberDP) == 1:
    print(0)
else:
    print(max(map(max, numberDP)))


