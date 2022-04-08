import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
operators = list(map(int, sys.stdin.readline().split()))
case = ['+', '-', '*', '//']
result = []


def dfs(current_value, next_index, operator, operator_list):
    if operator == "+":
        current_value += numbers[next_index]
        operator_list[0] -= 1
    elif operator == "-":
        current_value -= numbers[next_index]
        operator_list[1] -= 1
    elif operator == "*":
        current_value *= numbers[next_index]
        operator_list[2] -= 1
    else:
        if current_value < 0:
            current_value = -(-current_value // numbers[next_index])
        else:
            current_value //= numbers[next_index]
        operator_list[3] -= 1

    if sum(operator_list) == 0:
        result.append(current_value)
        return
    else:
        for j in range(4):
            if operator_list[j] != 0:
                dfs(current_value, next_index + 1, case[j], operator_list[:])


for i in range(4):
    if operators[i] != 0:
        dfs(numbers[0], 1, case[i], operators[:])

print(max(result))
print(min(result))
