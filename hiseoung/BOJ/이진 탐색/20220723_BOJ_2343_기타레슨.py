import sys
input = sys.stdin.readline

N, M = map(int, input().split())
videos = list(map(int, input().split()))

# 이분탐색 기준 -> 한 동영상의 최소 길이(left), 모든 동영상 길이의 합(right)
left, right = max(videos), sum(videos)
answer = 0

while left <= right:
    mid = (left+right)//2
    count, sum_blu_ray = 0, 0

    for i in range(N):
        # mid 값보다 크게 되면 현재 블루레이에 추가하는 걸 멈추고 다음 블루레이로 초기화한다.
        if sum_blu_ray + videos[i] > mid:
            count += 1
            sum_blu_ray = 0
        sum_blu_ray += videos[i]

    if sum_blu_ray:
        count += 1

    if count > M:
        left = mid + 1
    else:
        right = mid - 1
        answer = mid

print(answer)