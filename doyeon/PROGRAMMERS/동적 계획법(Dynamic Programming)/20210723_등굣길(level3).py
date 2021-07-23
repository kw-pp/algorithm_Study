def solution(m, n, puddles):
    answers = [[0]*(m+1) for j in range(n+1)]
    answers[1][1]=1
    for i in range(1,n+1):
      for j in range(1,m+1):
        if i==1 and j==1: continue
        if [j,i] in puddles:
            answers[i][j]=0
        else: answers[i][j]=answers[i-1][j]+answers[i][j-1]
    return answers[n][m]%1000000007