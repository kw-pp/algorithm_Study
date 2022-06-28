import sys
input = sys.stdin.readline

N = int(input())
arr = [[0] * N for _ in range(N)] #배치된 자리
students = [list(map(int, input().split())) for _ in range(N**2)]

#북 동 서 남
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

#자리 배치
for order in range(N**2):
  student = students[order]
  temp = []
  for i in range(N):
    for j in range(N):
      if arr[i][j] == 0:
        like = 0
        empty = 0
        for k in range(4):
          nx = i + dx[k]
          ny = j + dy[k]
          if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] in student[1:]:
              like += 1
            if arr[nx][ny] == 0:
              empty += 1
        temp.append([like, empty, i, j])
  temp.sort(key= lambda x:(-x[0], -x[1], x[2], x[3]))
  arr[temp[0][2]][temp[0][3]] = student[0]
  
res = 0
students.sort()
for i in range(N):
  for j in range(N):
    cnt = 0 #학생별 만족도
    for k in range(4):
      nx = i + dx[k]
      ny = j + dy[k]
      if 0 <= nx < N and 0 <= ny < N:
        if arr[nx][ny] in students[arr[i][j]-1]: #자기자신은 없으므로 전체탐색해도 상관없음
          cnt += 1
    if cnt != 0:
      res += 10 ** (cnt-1)

print(res)
