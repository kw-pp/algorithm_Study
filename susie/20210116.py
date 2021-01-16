#N까지 존재하는 한수의 개수를 출력
#한수는 3자리수부터 성립, 따라서 2자리수까지는 모두 한수
#

def seq(args):
    han_list = []
    
    for i in range(1, args+1):
        if len(str(i)) == 3:
            a = i // 100
            b = i % 100 // 10
            c = i % 100 % 10

            if (a-b) == (b-c) :
                han_list.append(i)
            else:
                continue
            
        elif len(str(i)) == 4:
            continue
            
        else:
            han_list.append(i)
        
    print(len(han_list))

N = int(input())
seq(N)
