X=int(input())
DP=[[0,[]] for _ in range(X+1)]#연산 횟수와 연산 과정
 
#초기화
DP[1][0]=0
DP[1][1]=[1]
 
for i in range(2,X+1):
    #1을뺄때
    DP[i][0]=DP[i-1][0]+1
    DP[i][1]=DP[i-1][1]+[i]
 
    #2로 나누어 떨어질때
    if i%2==0 and DP[i][0]>DP[i//2][0]+1:
        DP[i][0] = DP[i//2][0] + 1
        DP[i][1] = DP[i//2][1] + [i]
 
    #3으로 나누어 떨어질때
    if i%3==0 and DP[i][0]>DP[i//3][0]+1:
        DP[i][0] = DP[i//3][0] + 1
        DP[i][1] = DP[i//3][1] + [i]
 
 
print(DP[X][0])#연산 최솟값 출력
DP[X][1].reverse()#뒤집기
for i in DP[X][1]:
    print(i,end=" ")