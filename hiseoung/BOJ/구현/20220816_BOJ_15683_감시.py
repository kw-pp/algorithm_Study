import sys
from collections import Counter
input = sys.stdin.readline

# 주어진 방향으로 CCTV 탐색, 벽이 있으면 반환
def view_cctv(x, y, a, b):
    area = []
    while True:
        x = x + a
        y = y + b
        if 0 <= x < N and 0 <= y < M:
            if office[x][y] == 6: # 벽에 마주친 경우 루프 종료
                break
            elif office[x][y] == 0:
                office[x][y] = 7 # 해당 영역에 방문 했다면, 7로 마킹
                area.append((x, y))
        else:
            break
    return area # DFS 탐색 종료 후 마킹했던 위치를 반환


# CCTV가 감시할 수 있는 영역을 탐색 (DFS)
def search_area(cctv, k, n):
    global min_val

    # 재귀 종료 조건 : 더 이상 탐색할 CCTV가 남아 있지 않는 경우
    if k == n:
        val = sum([Counter(row)[0] for row in office]) # 비어있는 영역 계산
        if val < min_val:
            min_val = val
        return

    x, y, t = cctv[k]
    area = []

    if t == 1:
        # 1번 CCTV -> 네 방향 순회
        for a, b in (1, 0), (0, 1), (-1, 0), (0, -1):
            area.append(view_cctv(x, y, a, b))
            search_area(cctv, k + 1, n)
            for pos in area:
                for nx, ny in pos:
                    office[nx][ny] = 0
    elif t == 2:
        # 2번 CCTV -> 두 방향 순회
        for a, b, c, d in (1, 0, -1, 0), (0, 1, 0, -1):
            area.append(view_cctv(x, y, a, b))
            area.append(view_cctv(x, y, c, d))
            search_area(cctv, k + 1, n)
            for pos in area:
                for nx, ny in pos:
                    office[nx][ny] = 0
    elif t == 3:
        # 3번 CCTV -> 네 방향 순회
        for a, b, c, d in (1, 0, 0, 1), (1, 0, 0, -1), (-1, 0, 0, -1), (-1, 0, 0, 1):
            area.append(view_cctv(x, y, a, b))
            area.append(view_cctv(x, y, c, d))
            search_area(cctv, k + 1, n)
            for pos in area:
                for nx, ny in pos:
                    office[nx][ny] = 0
    elif t == 4:
        # 4번 CCTV -> 네 방향 순회
        for a, b, c, d, e, f in (1, 0, 0, 1, 0, -1), (1, 0, 0, -1, -1, 0), (-1, 0, 0, -1, 0, 1), (-1, 0, 0, 1, 1, 0):
            area.append(view_cctv(x, y, a, b))
            area.append(view_cctv(x, y, c, d))
            area.append(view_cctv(x, y, e, f))
            search_area(cctv, k + 1, n)
            for pos in area:
                for nx, ny in pos:
                    office[nx][ny] = 0
    elif t == 5:
        # 5번 CCTV -> 모든 방향 탐색이므로 한번만 처리
        a, b, c, d, e, f, g, h = 1, 0, -1, 0, 0, 1, 0, -1
        area.append(view_cctv(x, y, a, b))
        area.append(view_cctv(x, y, c, d))
        area.append(view_cctv(x, y, e, f))
        area.append(view_cctv(x, y, g, h))
        search_area(cctv, k + 1, n)
        for pos in area:
            for nx, ny in pos:
                office[nx][ny] = 0
    return

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]
min_val = float('inf')
# 벽이 아닌 CCTV 위치를 받아와 저장 ( 장비 유형에 대한 정보도 같이 넘김 )
cctv_pos = []
for i in range(N):
    for j in range(M):
        if office[i][j] == 1:
            cctv_pos.append((i, j, 1))
        elif office[i][j] == 2:
            cctv_pos.append((i, j, 2))
        elif office[i][j] == 3:
            cctv_pos.append((i, j, 3))
        elif office[i][j] == 4:
            cctv_pos.append((i, j, 4))
        elif office[i][j] == 5:
            cctv_pos.append((i, j, 5))
search_area(cctv_pos, 0, len(cctv_pos))
print(min_val)