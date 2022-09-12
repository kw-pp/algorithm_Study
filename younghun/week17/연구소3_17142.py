import sys
from itertools import combinations
from copy import deepcopy
from collections import deque


n, m = map(int, sys.stdin.readline().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cand = []
target_num = 0
answer = []
fail = []


def spread(pos):  # BFS
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    is_visited = [[False] * n for _ in range(n)]
    table = deepcopy(lab)
    time = 0
    global target_num  # 0의 갯수
    num = target_num

    queue = deque(pos)  # M개의 시작 지점

    while queue:
        if num == 0:
            break
        for _ in range(len(queue)):  # 현재 큐에 있는 바이러스들을 모두 퍼트리고 시간 1초 증가
            x, y = queue.popleft()

            if table[x][y] == 0:
                table[x][y] = 2

            is_visited[x][y] = True

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n and not is_visited[nx][ny] and table[nx][ny] != 1:
                    if table[nx][ny] == 0:
                        table[nx][ny] = 2
                        num -= 1
                    queue.append([nx, ny])  # 다음 초에 퍼트릴 바이러스 큐에 추가
                    is_visited[nx][ny] = True
        time += 1  # 시간 1초 증가

    if num > 0:  # 바이러스 퍼트리기 실패
        return -1
    return time  # 성공하면 소요된 시간 리턴


for i in range(n):
    for j in range(n):
        if lab[i][j] == 2:
            cand.append([i, j])  # 바이러스 위치 저장
        elif lab[i][j] == 0:
            target_num += 1  # 0 갯수 관리

cases = list(combinations(cand, m))  # 바이러스 시작지점 선택 조합의 경우의 수

for case in cases:
    result = spread(case)
    if result == -1:
        fail.append(result)
    else:
        answer.append(result)

if not answer:
    print(-1)
else:
    print(min(answer))
