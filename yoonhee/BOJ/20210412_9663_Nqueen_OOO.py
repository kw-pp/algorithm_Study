def ck(row, col):
    if ck_col[col] == 1:
        return False
    if ck_dig[row + col] == 1:
        return False
    if ck_dig2[row - col + N-1] == 1:
        return False
    return True

def dfs(row):
    if row == N:
        return 1
    result = 0
    for col in range(N):
        if ck(row, col):
            D[row][col] = 1
            ck_col[col] = 1
            ck_dig[row + col] = 1
            ck_dig2[row - col + N-1] = 1
            result += dfs(row + 1)
            D[row][col] = 0
            ck_col[col] = 0
            ck_dig[row + col] = 0
            ck_dig2[row - col + N-1] = 0
    return result

N = int(input())
D = [[0]*N for _ in range(N)]
ck_col = [0] * N
ck_dig = [0] * (2*N-1)
ck_dig2 = [0] * (2*N-1)
print(dfs(0))
