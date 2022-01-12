target = int(input())
#자릿수 파악
a = list(str(target))

#분해합 계산
def dgit(num):
    a = map(int, list(str(num)))
    return (num + sum(a))

#자릿수마다 최대 9까지 더해질 수 있으므로, 이에따라 반복 범위를 제한할 수 있음
#시간제한이 있어서 1부터 루프를 돌리면 실패

#i값이 음수부터 시작하지 않도록 1~18, 나머지로 범위를 나눔
if target >= 19:
    for i in range(target - (len(a) * 9), target):
        if target == dgit(i):
                print(i)
                break
        if i == target-1:
            print(0)
else:
    for i in range(0, target):
        if target == dgit(i):
            print(i)
        if i == target-1:
            print(0)
