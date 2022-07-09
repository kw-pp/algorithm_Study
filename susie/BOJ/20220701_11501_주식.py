import sys

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    N = int(input().rstrip())
    li = list(map(int, input().rstrip().split()))

    answer = 0
    maxi = 0

    for i in range(len(li)-1, -1, -1):
        if li[i] > maxi:
            maxi = li[i]
        else:
            answer += maxi-li[i]
    print(answer)
