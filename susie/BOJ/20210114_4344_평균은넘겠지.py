C = int(input())
for c in range(C):
    L = list(map(int, input().split()))
    avg = 0
    rat = 0

    #리스트의 평균 측정
    for e in range(1,len(L)):
        avg += L[e]
    avg = avg / (len(L)-1)
    #평균을 넘는 학생들의 비율 측정
    for s in range(1, len(L)):
        if L[s] > avg:
            rat += 1
    rat = (rat / (len(L)-1)) * 100
    print('%.3f%%' % rat)
