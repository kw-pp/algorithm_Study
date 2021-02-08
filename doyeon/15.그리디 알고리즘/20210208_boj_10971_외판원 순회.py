import sys 
def move(now, depth): 
  global charge, ans 
  if depth == n: 
    if path[now][0] > 0: 
      ans = min(ans, charge + path[now][0]) 
    return 
    
  visit[now] = 1 
  for l in link[now]: 
    if not visit[l]: 
      charge += path[now][l] 
      move(l, depth+1) 
      charge -= path[now][l] 
  visit[now] = 0 
  
n = int(sys.stdin.readline()) 
path = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] 
visit = [0] * n 
link = {} 
charge, ans = 0, 10**7 

# link 딕셔너리에 각 행마다 0이 아닌 수의 index를 넣음.
for i in range(n): 
  link[i] = [] 
  for j in range(n): 
    if path[i][j] > 0: 
      link[i].append(j) 
print(link)
      
move(0, 1) 
print(ans)