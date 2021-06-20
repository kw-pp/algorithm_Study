n = int(input())
arr = [['*' for i in range(n)] for _ in range(n)]

def star(length, x,y):
  global arr

  if length==1:
    return
  
  a = length//3
  for row in arr[x-length+a: x-a]:
    row[y-length+a: y-a] = ' '*a
  for i in range(length//a):
    for j in range(length//a):
      star(a, x-i*a, y-j*a)

star(n,n,n)
for i in arr:
  print(''.join(i))