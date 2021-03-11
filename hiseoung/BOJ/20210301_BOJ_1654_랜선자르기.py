k, n = map(int, input().split())
a = []

for i in range(k):
    a.append(int(input()))

var = max(a)
Max = float('-INF')


def BS(left, right):

    global Max, Target
    # 탈출 조건?
    count = 0
    if right - left == 1:
        mid = right
        for i in range(k):
            count += a[i] // mid
        if count >= n:
            if mid >= Max:
                Max = mid
        return

    if (right - left) % 2 == 0:
        mid = left + (right - left) // 2
    else:
        mid = left + (((right - left) // 2) + 1)

    for i in range(k):
        count += a[i] // mid
    # if mid == 99:
    #     print(str(left) + ' ' + str(right))
    if count >= n:
        if mid >= Max:
            Max = mid
            if right - left == 2:
                return
            BS(mid, right)
    else:
        if right - left == 2:
            if right - left == 2:
                return
        BS(left, mid)


if n == k == 1:
    print(a.pop())
else:
    BS(0, var)
    print(Max)
