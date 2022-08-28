import sys
input = sys.stdin.readline

n, m = map(int, input().split())
table = [int(input()) for _ in range(n)]
# 탐색 범위 지정
_min, _max = 1, int(1e9)
result = _min

# 인출 횟수 반환 : 현재 주어진 돈 기준 
def get_num_withdrawal(cash):
    count = 0
    current = 0
    for i in table:
        if i > current:
            count += 1
            current = cash
            current -= i
        else:
            current -= i
    return count

while _min <= _max:
    mid = (_min + _max) // 2
    cnt = get_num_withdrawal(mid)
    if cnt > m or mid < max(table):
        _min = mid + 1
    else:
        _max = mid - 1
        result = mid
print(result)