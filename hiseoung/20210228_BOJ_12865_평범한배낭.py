n, k = map(int, input().split())

bag = [[0] * (k+1) for _ in range(n+1)]
a = []
w=[0]
v=[0]
for i in range(n):
    w1,v1 = map(int, input().split())
    w.append(w1)
    v.append(v1)

for i in range(1, n+1):
    for j in range(k, 0, -1):
        if j - w[i] >= 0:
            bag[i][j] = max(bag[i-1][j], v[i] + bag[i-1][j-w[i]])
        else:
            bag[i][j] = bag[i-1][j]
print(max(bag[n]))
