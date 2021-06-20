N = int(input())
weight = []
value = []
for i in range(N):
  weight.append(int(input()))

weight.sort(reverse=True)

for i in range(N):
  value.append(weight[i]*(i+1))
print(max(value))