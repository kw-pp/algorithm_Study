num, Max = map(int, input().split())

a = list(map(int, input().split()))
Best = 0

#입력받은 숫자중에 3개를 고름 -> 삼중 for문(모든 Case확인을 위해)
for i in range(0, num):

    for j in range(1, num):
        #값 중복 방지
        if i >= j:
            while i >= j:
                j += 1

        for z in range(2, num):
            # 값 중복 방지
            if j >= z:
                while j >= z:
                    z += 1
            try:
                #max값보다 작으면 일단 저장하고 루프 돌리면서 계속 비교
                if a[i] + a[j] + a[z] <= Max and a[i] + a[j] + a[z] > Best:
                    Best = a[i] + a[j] + a[z]
            except IndexError:
                pass

print(Best)
