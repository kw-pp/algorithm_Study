# https://rebas.kr/761 참고
import sys
n = int(sys.stdin.readline())
count=0
 
row,left,right=[0 for _ in range(n)],[0 for _ in range(2*n-1)],[0 for _ in range(2*n-1)] #수직,왼쪽대각선,오른쪽 대각선
#인덱스의 합과 차가 같은 대각선상에 있을때 같다는 것을 이용함
#ex)0,2과 1,1과 2,0은 같은 대각선 상에 위치한다. 각행열의 합이 같은것을 알수있다.
 
def queenlocation(index):
    global count
    if index==n:    #끝까지 퀸을 넣으면
        count+=1
        return
    for col in range(n):  #열을 이동하며
        if row[col] + left[index+col] + right[n-1+index-col] ==0: #세조건에 걸리지 않는다면
            row[col] = left[index+col] = right[n-1+index-col] = 1
            queenlocation(index+1)
            row[col]= left[index+col]= right[n-1+index-col] = 0#초기화
 
queenlocation(0)
print(count)