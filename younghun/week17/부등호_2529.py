import sys
from itertools import permutations


k = int(sys.stdin.readline())
symbols = sys.stdin.readline().split()  # 부등호 리스트
digits = [i for i in range(10)]
cases = list(permutations(digits, len(symbols)+1))  # 가능한 케이스들을 순열을 이용해 구함
max_val = '0'
min_val = "9999999999"

for case in cases:

    left = case[0]
    exit_flag = False

    for i in range(len(symbols)):
        right = case[i+1]
        symbol = symbols[i]

        if symbol == '<' and left > right:
            exit_flag = True
            break
        elif symbol == '>' and left < right:
            exit_flag = True
            break

        left = right

    if exit_flag:  # 부등호 조건에 안맞으면 넘김
        continue

    num = ''.join(map(str, case))

    if num > max_val:  # 조건을 통과한 수들 중 최대, 최솟값을 구함
        max_val = num
    if num < min_val:
        min_val = num

print(max_val)
print(min_val)
