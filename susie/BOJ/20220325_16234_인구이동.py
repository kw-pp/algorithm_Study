import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int,input().split())
population=[list(map(int, input().split())) for _ in range(N)]

#동서남북
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
answer = 0

while True:
    cnt = 0
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1 #방문한 국가
                pop_cnt = population[i][j]
                union = [(i, j)] #연합
                q = deque([(i, j)])

                while q:
                    x, y = q.popleft()
                    
                    for k in range(4):
                        mx = x + dx[k]
                        my = y + dy[k]
                        if 0 <= mx < N and 0 <= my < N and visited[mx][my] == 0:
                            if L <= abs(population[mx][my] - population[x][y]) <= R: #절대값으로 비교하기
                                union.append((mx,my))
                                visited[mx][my]=1
                                q.append((mx,my))
                                pop_cnt += population[mx][my]

                for x, y in union:
                    population[x][y] = pop_cnt // len(union)
                cnt += 1

    if cnt == N**2: #국가 전체 탐색 완료시
        break
    answer += 1

print(answer)
