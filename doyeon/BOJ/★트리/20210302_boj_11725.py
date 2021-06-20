import sys
from collections import deque
inp = sys.stdin.readline
n = int(inp())

parent = [0] * (n+1) # 부모 테이블 초기화
parent[1]=1

tree={}
for i in range(1, n+1):
  tree[i] = []
for _ in range(n-1):
  a, b= map(int, inp().split())
  tree[a].append(b)
  tree[b].append(a)

q = deque([1])
while q: 
  node = q.popleft() 
  for child in tree[node]: 
    if not parent[child]:
      parent[child] = node 
      q.append(child)

for i in parent[2:]:
  print(i)