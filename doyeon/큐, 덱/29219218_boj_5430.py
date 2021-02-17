from sys import stdin, stdout

def AC(p, n, li):
  p.replace('RR', '')
  l,r,isreversed=0,0,True
  for c in p:
    if c=='R':
      isreversed = not isreversed
    elif c=='D':
      if isreversed: 
        l +=1
      else:
        r +=1
  if l+r <= n:
    res = li[l:n-r]
    if isreversed:
      return '['+','.join(res)+']\n'
    else:
      return '['+','.join(res[::-1])+']\n'
  else:
    return 'error\n'

t = int(stdin.readline())
for _ in range(t):
  p = stdin.readline()
  n = int(stdin.readline())
  li = stdin.readline().rstrip()[1:-1].split(',')
  if n == 0: []
  stdout.write(AC(p, n, li))