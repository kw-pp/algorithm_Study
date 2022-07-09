import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
temp = [arr[-1]]
answer = [-1 for _ in range(N)]

for i in range(N-2,-1,-1):
  #마지막 값은 무조건 -1
  while True:
    #오른쪽에 자기 자신보다 큰 수가 없는 경우
    if len(temp) == 0:
      temp.append(arr[i])
      break

    comp = temp.pop()
    if comp != arr[i] and min(comp, arr[i]) == arr[i]:
      answer[i] = comp
      temp.append(comp)
      temp.append(arr[i])
      break

for x in answer:
  print(x, end=' ')
