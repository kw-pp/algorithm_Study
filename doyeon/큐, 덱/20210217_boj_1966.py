t = int(input())
for i in range(t):
  n,m = map(int, input().split())
  s = list(map(int, input().split()))
  idx = [0 for i in range(n)]
  idx[m] = 1

  order = 0
  while True:
    if s[0]==max(s):
      order += 1
      if idx[0]==1:
        print(order)
        break
      else:
        s.pop(0)
        idx.pop(0)
    else:
      s.append(s.pop(0))
      idx.append(idx.pop(0))