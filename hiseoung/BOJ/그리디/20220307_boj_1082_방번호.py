import sys

roomNo = int(sys.stdin.readline())
roomPrice = {key: value for key, value in enumerate(list(map(int, sys.stdin.readline().split())))}
totalPrice = int(sys.stdin.readline())

numberDP = [[i for i in range(roomNo)]]
priceDP = [[roomPrice[i] for i in range(roomNo)]]

while True:
    numTemp = []
    priceTemp = []
    for i in range(roomNo):
        if i == 0:
            priceTemp.append(0)
            numTemp.append(0)
        else:
            priceList = [priceDP[-1][i] + priceDP[0][x] for x in range(roomNo)]
            maxValue = 0
            selectNum = -1
            for j in range(roomNo):
                if maxValue < priceList[j] <= totalPrice:
                    maxValue = priceList[j]
                    selectNum = j
            priceTemp.append(maxValue)
            try:
                numTemp.append(int(str(numberDP[-1][i]) + str(selectNum)))
            except Exception:
                numTemp.append(0)
    print(sum(priceTemp))
    if sum(priceTemp) == 0:
        print(11)
        break
    numberDP.append(numTemp)
    priceDP.append(priceTemp)

print(max(numberDP))


