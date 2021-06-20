def power(a, b):
    if b == 1: # b의 값이 1이면 a % C를 return한다.
        return a % c
    else:
        temp = power(a, b // 2) # a^(b // 2)를 미리 구한다.
        if b % 2 == 0:
            return temp * temp % c # b가 짝수인 경우
        else:
            return temp * temp * a % c # b가 홀수인 경우
a,b,c = map(int, input().split())
result = power(a, b)
print(result)