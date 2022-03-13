import sys


result = []

while True:
    sent = sys.stdin.readline().rstrip()
    stack = []
    is_stacked = 0
    flag = 0

    if sent == '.':
        break

    for char in sent:
        if char == '(':
            stack.append(')')
            is_stacked += 1
        elif char == '[':
            stack.append(']')
            is_stacked += 1
        elif char == ')' or char == char == ']':
            if is_stacked:
                if stack.pop() != char:
                    flag = 1
                    is_stacked -= 1
            else:
                flag = 1
        else:
            continue

    if flag:
        result.append('no')
    else:
        result.append('yes')

answer = [print(i) for i in result]


