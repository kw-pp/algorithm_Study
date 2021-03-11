import re
ep = input()
# '-'기준으로 짜르기
a = re.split('[-]', ep)
b = []
result = 0
j = 0
count = 0
l = len(a)

first = a.pop(0)

# +가 붙어 있는 것과 그렇지 않은 것 구분
while True:
    if count == l:
        break
    if a[j].find('+') == -1:
        b.append(int(a.pop(j)))
    else:
        a[j] = re.split('[+]', a[j])
        for z in range(len(a[j])):
            a[j][z] = int(a[j][z])
        j += 1
    count += 1

# 괄호를 붙인 뒤 -1을 곱하는 과정
for i in range(len(a)):
    result += -1 * sum(a[i])


# 처음에 제외했던 첫 항 계산(제일 처음에 오는 수는 -1을 곱할 필요가 없음)
if first.find('+') == -1:
    first = int(first)
else:
    first = re.split('[+]', first)
    for i in range(len(first)):
        first[i] = int(first[i])
    first = sum(first)

for i in range(len(b)):
    result += -1 * b[i]

result += first
print(result)
