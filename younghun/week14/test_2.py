def solution(ingredient):
    answer = 0
    stack = []
    for i in ingredient:
        stack.append(i)
        if len(stack) >= 4 and "".join(map(str, stack[-4:])) == "1231":
            for _ in range(4):
                stack.pop()
            answer += 1
    return answer
