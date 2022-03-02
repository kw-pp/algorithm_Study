def binarySearch(start, end, target):
    try:
        if start > end:
            return 0
        mid = (end + start) // 2
        if target > arr_A[mid]:
            return binarySearch(mid + 1, end, target)
        elif target < arr_A[mid]:
            return binarySearch(start, mid-1, target)
        else:
            return 1
    except IndexError:
        return 0


num_A = int(input())
arr_A = list(map(int, input().split()))
arr_A.sort()
num_B = int(input())
arr_B = list(map(int, input().split()))


for tgt in arr_B:
    print(binarySearch(0, num_B-1, tgt))


