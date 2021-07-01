import heapq

def solution(operations):
    h = []

    for i in operations:
        a, b = i.split()
        if a == 'I':
            heapq.heappush(h, int(b))
        else:
            if len(h) > 0:
                if b == '1':
                    h.pop(h.index(heapq.nlargest(1, h)[0]))
                else:
                    heapq.heappop(h)

    if len(h) == 0:
        return [0, 0]
    else:
        return [heapq.nlargest(1, h)[0], h[0]]