#에라토스테네스의 체를 이용한다.
def is_Prime(num):
    sqrt = int(num**0.5)

    if num == 1:
        return False
    else:
        for i in range(2, sqrt+1):
            if num % i == 0:
                return False
        return True
    
M,N = map(int,input().split())

for x in range(M, N+1):
    if is_Prime(x) == True:
        print(x)
