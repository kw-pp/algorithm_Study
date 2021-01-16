def func(num):
    
    
    count = 0
    
    #변수가 한수라면 count += 1
    for x in range(1, num+1):
        
        #100보다 작은 경우는 모두 한수이므로 count증가
        if x < 100:
            count += 1
            continue
        else:
            #a는 각 자릿수의 값을 저장, b는 공차를 저장
            a = list(str(x))
            
            for i in range(0, len(a)):
                
                a[i] = int(a[i])
                
            b = []
            try:
                for i in range(0, 3):
                   
                    b.append(a[i+1] - a[i])
                
            except IndexError:
                pass
            
            #b를 집합으로 변환해서 중복 제거 공차가 모두 같다면 1이남음
            c = set(b)
            if len(c) == 1:
                count += 1
                
    print(count)
        
n = int(input())
func(n)
