def d(n):
    cons_list =[]
    for i in range(1,n+1):
        dig = str(i) #자리수
        cons = i #생성자
        num = cons + sum(map(int,dig))
        cons_list.append(num)
        cons_list.sort()

    for j in range(1,n+1):
        if j in cons_list:
            continue
        else:
            print(j)

d(10000)
