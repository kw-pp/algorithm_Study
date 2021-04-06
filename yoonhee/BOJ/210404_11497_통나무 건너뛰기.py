import sys
input = sys.stdin.readline

# 오답
'''
# test case 의 개수
t = int(input())

for i in range(t):
    # 통나무의 개수
    n = int(input())
    # 각 통나무의 높이
    li = list(map(int,input().split()))
    li.sort()
    result = 0
    temp = []
    # list 차례대로 넣기 
    temp.extend(li[::2]) # 한 step 건너뜀)
    del li[::2]
    temp.extend(li[::-1]) # reverse
    temp2 = []
    # Level 계산
    for i in range(len(temp)-1):
       temp2.append(temp[i+1] - temp[i])
    print(max(temp2))
    
'''
# 정답
# test case 의 개수
t = int(input())

for i in range(t):
    # 통나무의 개수
    n = int(input())
    # 각 통나무의 높이
    li = list(map(int,input().split()))
    li.sort()
    result = 0
    for j in range(2,n):
        temp = li[j] - li[j-2]
        result = max(result,temp)
    print(result)
