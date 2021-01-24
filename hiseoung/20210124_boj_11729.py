num = int(input())

load = []
count = []

def hanoi(num, start, mid, end):

    count.append(1)

    #재귀 탈출
    if num == 1:
        load.append(str(start) + " " + str(end))
    else:
        #1. 작은 원반 1 -> 2
        hanoi(num-1, start, end, mid)
        #2. 남아있는 큰 원반 1 -> 3
        load.append(str(start) + " " + str(end))
        #3. 2에 남아있는 작은 원반들을 3으로 옮기기
        #남은 원반을 다른 막대로 옮기는 과정은 위에 진행한 것과 같음(재귀)
        hanoi(num-1, mid, start, end)

hanoi(num, 1, 2, 3)

print(sum(count))
for i in range(0, len(load)):
    print(load[i])
