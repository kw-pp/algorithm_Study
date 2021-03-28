s1 = list(str(input()))
s2 = list(str(input()))

# 2차원 배열 생성
arr = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) +1)]

# LCS 길이 출력
for i in range(len(s1)): # 행
    for j in range(len(s2)): # 열
        # 두 배열의 원소가 같은 경우
        if s1[i] == s2[j]:
            arr[i+1][j+1] = arr[i][j] + 1
        else:
            arr[i+1][j+1]= max(arr[i+1][j], arr[i][j+1])
            
print(arr[-1][-1])

# LCS 원소 출력
x = len(s1)
y = len(s2) 
result = []
while x > 0 and y > 0:
    if arr[x-1][y] == arr[x][y]:
        x -= 1
    elif arr[x][y-1] == arr[x][y]:
        y -= 1
    else:
        result.append(s1[x-1])
        x -= 1
        y -= 1

for c in result[::-1]:
    print(c,end='')

        
        
