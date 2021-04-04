import sys
input = sys.stdin.readline
t = int(input())

def check():
  for i in range(len(a)-1):
    if a[i] == a[i+1][0:len(a[i])]:
      print('NO')
      return
  print('YES')

for _ in range(t):
  n = int(input())
  a = []
  for i in range(n):
    a.append(input().strip())
  a.sort()
  check()