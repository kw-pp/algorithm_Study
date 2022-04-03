import sys

'''
    - 시간복잡도가 O(N^2) -> 통과 X
    - 
'''


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# sol_1 : 반복문 중첩 사용하면서 Max 값 도출, python3, pypy 모두 시간 초과
# sol = [[a for a in arr[i:] if a > arr[i]][0] if max(arr[i:]) > arr[i] else -1 \
#        for i in range(len(arr))]

# sol_2
sol = []
for i in range(N):
    for j in range(i):
        if arr[i] < arr[j]:
            sol.append(arr[j])
            break

answer = [print(i, end=' ') for i in sol]
