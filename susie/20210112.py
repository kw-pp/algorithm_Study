#조건잘보기 / 만약, 0<A,B<10이 아닐 경우 종료되도록 설정할 것.
loop = True

while(loop == True):
    try:
        A,B = map(int,input().split())

        if 0<A and A<10:
            if 0<B and B<10:
                print(A+B)
            else:
                loop = False
        else:
            loop = False
            
    except BaseException:
        loop = False
