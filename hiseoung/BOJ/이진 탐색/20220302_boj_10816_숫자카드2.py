import sys


def binarySearch(start, end, target, array):
    if start > end:
        return 0
    mid = (start + end) // 2

    if array[mid] == target:
        return array[start:end+1].count(target)
    elif array[mid] > target:
        return binarySearch(start, mid-1, target, array)
    else:
        return binarySearch(mid+1, end, target, array)


num_A = int(sys.stdin.readline().rstrip())
arr_A = sorted(list(map(int, sys.stdin.readline().split())))
num_B = int(sys.stdin.readline().rstrip())
arr_B = list(map(int, sys.stdin.readline().split()))
countDict = {}

for tgt in arr_B:
    if tgt not in countDict:
        countDict[tgt] = binarySearch(0, len(arr_A)-1, tgt, arr_A)

for tgt in arr_B:
    if countDict[tgt]:
        print(countDict[tgt], end=' ')
    else:
        print(0, end=' ')
