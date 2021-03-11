N, M = map(int, input().split())
a = range(1, N+1)
b = [False for i in range(N+1)]
r = []

def dfs(cnt):
    if cnt == M:
        for z in range(M):
            print(r[z], end=" ")
        print()
        return
    for j in range(N):
        if not b[j + 1]:
            r.append(a[j])
            dfs(cnt + 1)
            r.pop()
            b[j + 1] = False
        else:
            continue

dfs(0)
