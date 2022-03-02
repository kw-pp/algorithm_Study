import sys

arrLen = int(sys.stdin.readline().rstrip())
arr_A = list(map(int, sys.stdin.readline().split()))
arr_B = list(map(int, sys.stdin.readline().split()))

arr_A.sort()
arr_B.sort(reverse=True)

arrSum = sum([i * j for i, j in zip(arr_A, arr_B)])
print(arrSum)



