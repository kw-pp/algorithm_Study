while True:
  str = input()
  stack = []
  #예외처리 1
  if str == '.':
    break
  #스택 로직
  for x in str:
    if x == '.':
      if stack:
        print("no")
      else:
        print("yes")
      break
    if x == '(' or x == '[':
      stack.append(x)
    elif x == ')':
      if not stack or stack[-1] != '(':
        print("no")
        break
      else:
        stack.pop()
    elif x == ']':
      if not stack or stack[-1] != '[':
        print("no")
        break
      else:
        stack.pop()
    else:
      continue
