import sys


def binarySearch(start, end, target):
    global budgetMax
    if start > end:
        return None

    mid = (start + end) // 2
    arrSum = sum([mid if num > mid else num for num in budget])

    if target >= arrSum:
        if mid > budgetMax:
            budgetMax = mid
        return binarySearch(mid+1, end, target)
    else:
        return binarySearch(start, mid-1, target)


budgetMax = 1
numArea = int(sys.stdin.readline().rstrip())
budget = sorted((map(int, sys.stdin.readline().split())))
totalBudget = int(sys.stdin.readline().rstrip())

if sum(budget) <= totalBudget:
    print(max(budget))
else:
    binarySearch(1, budget[-1], totalBudget)
    print(budgetMax)

