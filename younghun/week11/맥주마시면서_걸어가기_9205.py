import sys
from collections import deque


def check():
    q = deque([start])
    visited = set()
    while q:
        x, y = q.popleft()
        if abs(x-festival[0]) + abs(y-festival[1]) <= 1000:
            return True
        for i in range(n):
            if i not in visited:
                nx, ny = store[i]
                if abs(x-nx) + abs(y-ny) <= 1000:
                    q.append((nx, ny))
                    visited.add(i)
    return False


t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    start = tuple(map(int, sys.stdin.readline().split()))
    store = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    festival = tuple(map(int, sys.stdin.readline().split()))

    if check():
        print("happy")
    else:
        print("sad")
