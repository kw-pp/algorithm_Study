def dfs(x,y, count):
  # 주어진 범위를 벗어나는 경우에는 즉시 종료
  if x<=-1 or x>=n or y<=-1 or y>=n:
    return False
  if graph[x][y] == 1:
    graph[x][y] = 0
    count=dfs(x-1,y,count)+dfs(x+1,y,count)+dfs(x,y-1,count)+dfs(x,y+1,count)+1
    return count
  return False
  # 현재 노드를 아직 방문하지 않았다면

n = int(input())

graph = []
for i in range(n):
  graph.append(list(map(int, input())))

result = []
for i in range(n):
  for j in range(n):
    # 현재 위치에서 DFS 수행
    count= dfs(i,j, 0)
    if count!=False:
      result.append(count)
print(len(result))
for i in sorted(result):
  print(i)