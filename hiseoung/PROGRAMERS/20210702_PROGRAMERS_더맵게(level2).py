import heapq
scoville = [1, 2, 3, 9, 10, 12]
K = 7

heap = []
for i in scoville:
    heapq.heappush(heap, i)

answer = 0
while heap[0] < K:
    try:
        fi = heapq.heappop(heap)
        se = heapq.heappop(heap)
        result = fi + (se * 2)
        heapq.heappush(heap, result)
    except IndexError:
        answer = -1
        break
    answer += 1
