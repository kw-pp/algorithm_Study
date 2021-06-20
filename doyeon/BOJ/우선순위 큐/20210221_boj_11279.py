import heapq as hq
import sys

n = int(input())
heap = []
for i in range(n):
  x = int(sys.stdin.readline())
  if x:
    hq.heappush(heap, (-x,x))
  else:
    if heap:
      print(hq.heappop(heap)[1])
    else:
      print(0)