import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())

que = deque()
for i in range(n):
  data = sys.stdin.readline().rstrip().split()
  order = data[0]
  if order == 'push':
    que.append(int(data[1]))
  elif order == 'pop':
    if not que:
      print(-1)
    else:
      print(que.popleft())
  elif order == 'size':
    print(len(que))
  elif order == 'empty':
    if que:
      print(0)
    else:
      print(1)
  elif order == 'front':
    if que:
      print(que[0])
    else:
      print(-1)
  elif order == 'back':
    if que:
      print(que[-1])
    else:
      print(-1)