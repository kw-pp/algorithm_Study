import sys
import copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
table = [[*map(int, input().split())] for _ in range(n)]
virus_pos = []
room_num = 0
answer = float('inf')

# 연구소를 순회하면서 현재 바이러스 위치 저장
for i in range(n):
    for j in range(n):
        if table[i][j] == 2:
            virus_pos.append((i, j))
        elif table[i][j] == 0:
            room_num += 1

# 초기 활성 바이러스 위치 선정
virus_list = [*combinations(virus_pos, m)]

# BFS
def bfs(virus):
    global room_num
    t = copy.deepcopy(table)
    q = deque(virus)
    is_visited = [[False] * n for _ in range(n)]
    count = 0
    num = room_num

    for x, y in virus:
        is_visited[x][y] = True

    while q:
        # 더 이상 탐색할 방이 없다면 루프 종료
        if num == 0:
            break
        for _ in range(len(q)):
            x, y = q.popleft()
            for a, b in (1, 0), (0, 1), (-1, 0), (0, -1):
                nx = x+a
                ny = y+b
                if 0 <= nx < n and 0 <= ny < n and not is_visited[nx][ny] and t[nx][ny] != 1:
                    # 빈 벽이면 확산
                    if t[nx][ny] == 0:
                        q.append((nx, ny))
                        t[nx][ny] = 2
                        num -= 1
                        is_visited[nx][ny] = True
                    elif t[nx][ny] == 2:
                        q.append((nx, ny))
                        is_visited[nx][ny] = True
        count += 1
    # 모든 방을 탐색할 수 있는 경우에만 진행 시간 반환
    return float('inf') if num != 0 else count

for virus in virus_list:
    answer = min(answer, bfs(virus))
print(-1) if answer == float('inf') else print(answer)

