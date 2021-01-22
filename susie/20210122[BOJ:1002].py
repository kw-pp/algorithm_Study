T = int(input())

#두 원의 교점의 개수
for case in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d = ((x2-x1)**2 + (y2-y1)**2)**0.5
    #위치의 개수 무한대
    if d == 0:
        if r1==r2:
            print(-1)
        else:
            print(0)
    else:
        if d == (r1+r2) or d == abs(r1-r2):
            print(1)
        elif d < (r1+r2) and d > abs(r1-r2):
            print(2)
        else:
            print(0)
