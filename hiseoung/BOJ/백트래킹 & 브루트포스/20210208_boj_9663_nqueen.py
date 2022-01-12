
n = int(input())
cnt = 0
#기준열, 좌우대각
a, b, c = [False]*n, [False]*(2*n-1), [False]*(2*n-1)

def NQueen(i):
    global cnt
    if i == n:
        cnt += 1
        return
    for j in range(n):
        if not (a[j] or b[i+j] or c[i-j+n-1]):
            a[j] = b[i+j] = c[i-j+n-1] = True
            NQueen(i+1)
            a[j] = b[i+j] = c[i-j+n-1] = False

NQueen(0)
print(cnt)

