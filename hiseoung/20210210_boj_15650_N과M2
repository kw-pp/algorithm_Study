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
            try:
                r.append(a[j])
                b[j + 1] = True
                if cnt == 0:
                    dfs(cnt + 1)
                    r.pop()
                    b[j + 1] = False
                #원래의 순열 문제에서 아래 조건으로 가지치기만 해주면 오름차순으로 출력
                elif r[cnt] > r[cnt-1]:
                    dfs(cnt + 1)
                r.pop()
                b[j + 1] = False
            except IndexError:
                pass
        else:
            continue

dfs(0)
