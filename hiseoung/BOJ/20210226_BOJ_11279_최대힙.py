import heapq

heap = []
result = []

T = int(input())

for i in range(T):
    a = int(input())

    if not a:
        if len(heap) == 0:
            result.append(0)
        else:
            result.append(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-a, a))

for i in result:
    print(i)
