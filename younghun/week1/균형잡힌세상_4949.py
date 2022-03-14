sentences = []
sentence = input()

while sentence != '.':
    sentences.append(sentence)
    sentence = input()

for i in sentences:
    stack = []

    for letter in i:
        if letter == '(' or letter == '[':
            stack.append(letter)

        elif letter == ')':
            if stack:
                item = stack.pop()
                if item != '(':
                    stack.append(item)
                    break
            else:
                stack.append(letter)
                break

        elif letter == ']':
            if stack:
                item = stack.pop()
                if item != '[':
                    stack.append(item)
                    break
            else:
                stack.append(letter)
                break

    if stack:
        print("no")
    else:
        print("yes")
