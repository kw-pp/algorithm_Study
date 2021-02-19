import sys
k,n = map(int, input().split())
long = [int(sys.stdin.readline()) for _ in range(k)]
start = 1
end = max(long)

# 이진 탐색 수행(반복적)
while(start <= end):
  total = 0
  mid = (start+end)//2
  for x in long:
    total += x // mid
  if total < n:
    end = mid-1
  else:
    start = mid+1

print(end)