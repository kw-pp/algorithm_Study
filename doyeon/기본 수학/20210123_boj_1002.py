n = int(input())

for i in range(n):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())
  r = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
  R = [r1, r2, r]
  m = max(R)
  R.remove(m)
  print(-1 if (r1==r2 and r==0) else 1 if (r==r1+r2 or m==sum(R)) else 0 if (m>sum(R)) else 2)