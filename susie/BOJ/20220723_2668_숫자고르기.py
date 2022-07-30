N = int(input())

second_map = [[] for _ in range(N+1)]

ans = set([])

for i in range(N):
  tmp = int(input())
  second_map[tmp].append(i+1)

for i in range(1, N+1):
  visited = [0 for _ in range(N+1)]
  visited[i] = 1
  stack = [i]

  while stack:
    num = stack.pop()

    for j in second_map[num]:
      if not visited[j]:
        stack.append(j)
        visited[j] = 1
      elif visited[j] and i == j:
        ans.add(j)

ans = list(ans)
print(len(ans))
ans.sort()
for i in range(len(ans)):
  print(ans[i])
