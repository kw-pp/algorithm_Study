import sys

N = int(sys.stdin.readline())
stack = list(map(int, sys.stdin.readline().split()))
answer = [-1 for _ in range(N)]

stack.reverse()
idx = 0
temp = [(idx, stack.pop())]

while stack:
    val = stack.pop()
    idx += 1

    while temp and temp[-1][1] < val:
        a, b = temp.pop()
        answer[a] = val

    temp.append((idx, val))
