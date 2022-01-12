import math

t = int(input())
a = set([])
b = []
gcd = 0
for i in range(t):
    b.append(int(input()))
#인접한 수의 차에 대한 최대공약수를 구함
#n[1] - n[0] = M1 * (a[1] - a[0])
#n[2] - n[1] = M2 * (a[1] - a[0])
#M1과 M2의 최대공약수가 구하고자하는 나머지가 됨

#인접한 수의 차에 대한 최대공약수를 저장(0~t)
try:
    for i in range(t):
        gcd = math.gcd(abs(b[i] - b[i - 1]), gcd)
except IndexError:
    pass

#출력된 최대공약수에 대해서 루트를 씌움
#이렇게 안하고 최대공약수만큼 돌리면 시간초과(어렵다어려워)
gcd_a = int(gcd ** 0.5)

#구한 최대공약수에 대한 약수를 구해서 출력
#중복을 제거하기 위해 집합을 이용
for i in range(2, gcd_a + 1):
    if gcd % i == 0:
        a.add(i)
        a.add(gcd // i)
a.add(gcd)
a = list(a)
a.sort()
for i in a:
    print(i, end=' ')
