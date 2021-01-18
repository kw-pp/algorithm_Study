from math import sqrt
T = int(input())

for case in range(T):
    x, y = map(int, input().split())
    dist = y-x

    if int(sqrt(dist)) == 1:
        print(dist)
    elif dist >= (int(sqrt(dist))) * ((int(sqrt(dist)))+1) +1:
        print((int(sqrt(dist))) + ((int(sqrt(dist)))+1))
    elif dist >= (int(sqrt(dist)))**2 +1:
        print((int(sqrt(dist))*2))
    else:
        print((int(sqrt(dist)))*2-1)
