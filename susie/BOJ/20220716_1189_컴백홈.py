# map에서 (0, 0)에서 (R-1, C-1)까지 길이가 K인 가짓수를 구하라
# 단, T는 맵에서 지나갈 수 없는 길이다
# brute force로 진행하고, T인 경우만 백트래킹으로 진행하기
# 한번 지나친 곳은 다시 방문하지 않는다. visited

R, C, K = map(int, input().split())

map = [list(input()) for _ in range(R)]
visited = [list(0 for _ in range(C)) for _ in range(R)]
visited[R-1][0] = 1
answer = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def find_path(x, y, length):
    global answer
    if x == 0 and y == (C-1) and length == K:
        answer += 1
    else:   
        for i in range(4): #사방으로 체크하기
            mx = x + dx[i]
            my = y + dy[i]
            if 0 <= mx < R and 0 <= my < C and map[mx][my] != 'T' and visited[mx][my] != 1:
                visited[mx][my] = 1 # 방문 표시
                find_path(mx, my, length + 1)
                visited[mx][my] = 0 # 방문 초기화

find_path(R-1, 0, 1)
print(answer)
