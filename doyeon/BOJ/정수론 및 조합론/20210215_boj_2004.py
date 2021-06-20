# 10은 2와 5로 구성된다.
# 따라서 nCm 내에 있는 2와 5 중 최소값이 무엇인지 알아낸 뒤 출력하면 된다.
def five_count(n):
    answer = 0
    while n != 0:
        n = n // 5
        answer += n
    return answer

def two_count(n):
    answer = 0
    while n != 0:
        n = n // 2
        answer += n
    return answer

n, m = map(int, input().split())

if m == 0:
    print(0)
else:       
    print(min(two_count(n)-two_count(m)-two_count(n-m), five_count(n)-five_count(m)-five_count(n-m)))