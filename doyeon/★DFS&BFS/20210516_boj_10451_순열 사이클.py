# DFS
t = int(input())
for _ in range(t):
  n = int(input())
  nums = [0] + list(map(int, input().split()))
  ans = 0
  visited =[1] +[0]*n
  for i in range(1,n+1):
    stack=[nums[i]]
    if visited[i]==0:
      ans+=1
      visited[i]=1
    while(stack):
      n_num = stack.pop()
      if visited[n_num]==0:
        visited[n_num]=1
        stack.append(nums[n_num])
  print(ans)