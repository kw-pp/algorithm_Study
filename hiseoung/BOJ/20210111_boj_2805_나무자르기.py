import sys

heightMax = float('-inf')
def binary_search(target, start, end):
    global heightMax
    if start > end:
        return None

    mid = (start + end) // 2
    value = sum([i-mid for i in treeList if i >= mid])

    if value < target:
        return binary_search(target, start, mid-1)
    else:
        if mid > heightMax:
            heightMax = mid
        return binary_search(target, mid+1, end)


n, m = map(int, sys.stdin.readline().split())
treeList = list(map(int, sys.stdin.readline().split()))
binary_search(m, 0, max(treeList))
print(heightMax)
