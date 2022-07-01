import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
posList = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]

for i in range(M):
    answer = 0
    x1, y1, x2, y2 = posList[i]
    min_val = 0
    max_val = 0

    if x1 >= x2:
        min_val = x2
        max_val = x1
    else:
        min_val = x1
        max_val = x2

    for j in range(min_val, max_val+1):

        min_val_y = 0
        max_val_y = 0

        if y1 >= y2:
            min_val_y = y2
            max_val_y = y1
        else:
            min_val_y = y1
            max_val_y = y2

        answer += sum(table[j][min_val_y:max_val_y+1])
    print(answer)

    