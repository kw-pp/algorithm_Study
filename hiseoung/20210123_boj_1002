T = int(input())
arr = []
for i in range(0, T):

    a, b, c, d, e, f = map(int, input().split())

    dist = ((d - a) ** 2 + (e - b) ** 2) ** 0.5

    # Case1 : 일치
    if dist == 0 and c == f:
        arr.append(-1)
    elif dist == 0 and c != f:
        arr.append(0)
    else:
        #Case2 : 접점 = 1
        if dist == (c + f) or dist == abs(c - f):
            arr.append(1)
        #Case3 : 접점 = 2
        elif abs(c - f) < dist < (c + f):
            arr.append(2)
        #Case4 : 접점 = 0
        else:
            arr.append(0)
for i in arr:
    print(i)
