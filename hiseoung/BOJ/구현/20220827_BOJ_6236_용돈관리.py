import sys
input = sys.stdin.readline

n, m = map(int, input().split())
table = [int(input()) for _ in range(n)]
_min, _max = min(table), sum(table)
result = _min

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

