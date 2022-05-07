N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dir = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while dir:
    #이동 direction 유효 좌표 확인
    d = dir.pop(0)
    mx = x + dx[d-1]
    my = y + dy[d-1]
    
    #유효 좌표인 경우에만
    if 0 <= mx < N and 0 <= my < M:
      if d == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
      elif d == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
      elif d == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
      else:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
  
      x, y = mx, my
      if arr[x][y] == 0:
        arr[x][y] = dice[5]
      else:
        dice[5] = arr[x][y]
        arr[x][y] = 0
      
      print(dice[0])
