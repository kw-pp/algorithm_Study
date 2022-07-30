from collections import Counter

X = '100'
Y = '2345'

x_counter = Counter(list(X))
y_counter = Counter(list(Y))
result = []

for i in range(9, -1, -1):
    idx = min(x_counter[str(i)], y_counter[str(i)])
    for j in range(idx):
        result.append(str(i))

answer = ''.join(result)
if answer == '':
    answer = '-1'
elif int(answer) == 0:
    answer = '0'

print(answer)