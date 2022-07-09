n, w, L = map(int, input().split())
arr = list(map(int, input().split()))
bridge = [0 for x in range(w)]
answer = 0

while arr:
  #다리 위에 트럭이 있는 경우
  if sum(bridge) > 0:
    #기존의 다리위 트럭 한칸씩 이동
    bridge[0] = 0
    for i in range(1, w):
      bridge[i-1] = bridge[i]
    bridge[-1] = 0

    if sum(bridge) + arr[0] <= L:
      bridge[-1] = arr.pop(0)
    answer += 1
  #다리 위에 트럭이 없는 경우
  else:
    truck = arr.pop(0)
    bridge[-1] = truck
    answer += 1
 
#마지막 트럭이 다리에 남아있을경우
if bridge:
  answer += w #다리의 길이만큼 더해준다

print(answer)
