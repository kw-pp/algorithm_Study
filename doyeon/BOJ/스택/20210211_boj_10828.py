import sys
n = int(sys.stdin.readline().rstrip())

stack = []
for i in range(n):
  data = sys.stdin.readline().rstrip().split()
  order = data[0]
  if order == 'push':
    stack.append(int(data[1]))
  elif order == 'pop':
    if not stack:
      print(-1)
    else:
      print(stack.pop())
  elif order == 'size':
    print(len(stack))
  elif order == 'empty':
    if stack:
      print(0)
    else:
      print(1)
  elif order == 'top':
    if stack:
      print(stack[-1])
    else:
      print(-1)