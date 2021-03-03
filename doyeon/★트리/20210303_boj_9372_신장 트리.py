import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
  # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
  if parent[x]!=x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a != b:
    parent[b] = a

t = int(input())
for _ in range(t):
  edges = []
  result = 0
  n, m = map(int, input().split())
  parent = [i for i in range(n+1)]
  for _ in range(m):
    a,b = map(int, input().split())
    edges.append((a,b))
  for edge in edges:
    a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
      union_parent(parent, a, b)
      result += 1
  print(result)