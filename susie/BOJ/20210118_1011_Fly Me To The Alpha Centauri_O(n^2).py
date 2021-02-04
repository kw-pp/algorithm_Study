T = int(input())

for case in range(T):
    x, y = map(int, input().split())
    dist = y-x
    count = 0
    sb_dist = 1
    mult2 = 0

    while(dist>0):
        dist -= sb_dist
        mult2 += 1 
        if  mult2 % 2 == 0:
            sb_dist += 1
        count += 1

    print(count)
