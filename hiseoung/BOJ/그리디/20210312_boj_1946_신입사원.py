import sys
T = int(sys.stdin.readline())
result = []
for i in range(T):
    n = int(sys.stdin.readline())
    a = []
    count = 0
    Max = float('inf')
    for j in range(n):
        a.append(list(map(int, sys.stdin.readline().split())))
    # 서류 점수 기준 정렬
    a.sort(key=lambda x: x[0])
    # for문 중첩하면 시간 초과, 값을 갱신해서 사용하는 것으로 중첩을 줄일 수 있음
    for i in range(0, len(a)):
        if a[i][1] < Max:
            count += 1
            Max = a[i][1]
    print(count)
