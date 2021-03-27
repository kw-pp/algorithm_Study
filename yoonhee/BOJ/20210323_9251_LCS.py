s1 = list(str(input()))
s2 = list(str(input()))

# 2차원 배열 생성
arr = [[0 for _ in range(len(s1) + 1)] for _ in range(len(s2) +1)]
#result = 0

for i in range(len(s1)):
    for j in range(len(s2)):
        # 두 배열의 원소가 같은 경우
        if s1[i] == s2[j]:
            arr[j+1][i+1] = arr[j][i] + 1
        else:
            arr[j+1][i+1]= max(arr[j+1][i], arr[j][i+1])
            
print(arr[-1][-1])
