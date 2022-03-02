def binarySearch(start, end, target):
    if start > end:
        return 0
    mid = (end + start) // 2
    if target == arr_A[mid]:
        return 1
    elif target < arr_A[mid]:
        return binarySearch(start, mid - 1, target)
    else:
        return binarySearch(mid + 1, end, target)


num_A = int(input())
arr_A = list(map(int, input().split()))
num_B = int(input())
arr_B = list(map(int, input().split()))

arr_A.sort()

for tgt in arr_B:
    print(binarySearch(0, num_A-1, tgt))


