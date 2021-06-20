# https://velog.io/@ready2start/Python-%EB%B0%B1%EC%A4%80-11497-%ED%86%B5%EB%82%98%EB%AC%B4-%EA%B1%B4%EB%84%88%EB%9B%B0%EA%B8%B0 참고
from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    heights = [int(x) for x in stdin.readline().split()]
    heights.sort()

    max_level = 0
    for i in range(2, n):
        max_level = max(max_level, abs(heights[i] - heights[i - 2]))

    print(max_level)