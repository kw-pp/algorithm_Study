'''
# LCS를 2회 하는것과 3차원 DP의 차이점
A: dababcf
B: ababdef
C: df
# 반례 
LCS(A,B): ababf
LCS(LCS(A,B),C):  f
LCS(A,B,C): df
'''
'''
s1 = list(str(input()))
s2 = list(str(input()))
s3 = list(str(input()))


def lcs(arr,x,y):
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                arr[i+1][j+1] = arr[i][j] + 1
            else:
                arr[i+1][j+1] = max(arr[i+1][j], arr[i][j+1])

    # 원소 list 만들기
    a = len(x)
    b = len(y)
    res = []
    while a > 0 and b > 0:
        if arr[a-1][b] == arr[a][b]:
            a -= 1
        elif arr[a][b-1] == arr[a][b]:
            b -= 1
        else:
            res.append(x[a-1])
            a -=1
            b -=1
    res.reverse()    
    return res


arr1= [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
res1 = lcs(arr1,s1,s2)
       
arr2= [[0 for _ in range(len(s3)+1)] for _ in range(len(res1)+1)]
res2 = lcs(arr2,res1,s3)
print(len(res2))

'''
# 3 차원 행렬 이용 
s1, s2, s3 = input(), input(), input()

dp = [[[0]*(len(s3)+1) for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
for i in range(1, len(s1)+1): # layer
    for j in range(1, len(s2)+1): # row
        for k in range(1, len(s3)+1): # column
            if s1[i-1] == s2[j-1] == s3[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1]+1
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
print(dp[-1][-1][-1])


