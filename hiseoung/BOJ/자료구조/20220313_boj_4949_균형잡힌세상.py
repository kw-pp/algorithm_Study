import sys


result = []

while True:
    sent = sys.stdin.readline().rstrip()
    if sent == '.':
        break

    stack = []
    flag = 0

    for char in sent:
        if char == '(':
            stack.append(')')
        elif char == '[':
            stack.append(']')
        elif char == ')' or char == ']':
            if stack:
                if stack.pop() != char:
                    flag = 1
                else:
                    continue
            else:
                flag = 1
        else:
            continue

    if stack:
        flag = 1

    if flag:
        result.append('no')
    else:
        result.append('yes')

answer = [print(i) for i in result]


