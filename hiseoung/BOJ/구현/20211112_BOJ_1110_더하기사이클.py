import sys

def solution1110():
    '''
    출처 : https://www.acmicpc.net/problem/1110
    분류 : 구현
    시간복잡도 :
    '''
    n = sys.stdin.readline().strip()
    if int(n) < 10:
        li = [0] * 2
        li[1] = n
    else:
        li = list(n)
    target = -1
    count = 0

    while int(n) != target:
        count += 1
        temp = int(li[0]) + int(li[1])
        if temp >= 10:
            target = int(li[1]) * 10 + int(list(str(temp))[1])
            li = list(str(target))
        else:
            target = int(li[1]) * 10 + temp
            if target < 10:
                li[0] = 0
                li[1] = target
            else:
                li = list(str(target))
    print(count)


solution1110()
