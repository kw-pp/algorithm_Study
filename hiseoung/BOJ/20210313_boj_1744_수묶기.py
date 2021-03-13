import sys
num = int(sys.stdin.readline())
# Positive
p = []
# Negative
n = []
result = []

# 음수와 양수를 나눠서 저장
for i in range(num):
    a = int(sys.stdin.readline())
    if a > 0:
        p.append(a)
    else:
        n.append(a)

# 각 배열을 절댓값 기준으로 정렬
p.sort(reverse=True)
n.sort()

# 1의 경우 곱하는 것보다 더해야 최댓값을 구할 수 있음, 이를 위해 1을 만날때 까지만 곱셈연산
idx = 0
c = False

# 양수 계산
for i in range(0, len(p), 2):
    if len(p) % 2 == 0:
        if p[i] == 1:
            idx = i
            c = True
            break
        elif p[i + 1] == 1:
            idx = i
            c = True
            break
        else:
            result.append(p[i] * p[i+1])
        if i+1 == len(p) - 1:
            break
    else:
        try:
            if p[i] == 1:
                idx = i
                c = True
                break
            elif p[i + 1] == 1:
                idx = i
                c = True
                break
            else:
                result.append(p[i] * p[i + 1])
        except IndexError:
            result.append(p[i])
            break

# 1이 있는 경우 더해주기
if c:
    for i in range(idx, len(p)):
        result.append(p[i])

# 음수 계산
for i in range(0, len(n), 2):
    if len(n) % 2 == 0:
        result.append(n[i] * n[i+1])
        if i+1 == len(n) - 1:
            break
    else:
        try:
            result.append(n[i] * n[i+1])
        except IndexError:
            result.append(n[i])
            break

print(sum(result))
