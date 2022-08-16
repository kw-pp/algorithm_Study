import sys
from collections import Counter
input = sys.stdin.readline

# 주어진 방향으로 CCTV 탐색
def view_cctv(x, y, a, b):
    area = []
    while True:
        x = x + a
        y = y + b
        if 0 <= x < N and 0 <= y < M:
            if office[x][y] == 6:
                break
            elif office[x][y] == 0:
                office[x][y] = 7
                area.append((x, y))
        else:
            break
    return area


# CCTV가 달려 있는 위치에서 해당 장비의 유형에 따라서 반복문 실행
def search_area(cctv, k, n):
    global min_val
    # 재귀 종료 조건 : 더 이상 탐색할 CCTV가 남아 있지 않는 경우
    if k == n:
        val = sum([Counter(row)[0] for row in office])
        if val < min_val:
            min_val = val
        return
    x, y, t = cctv[k]
    if t == 1:
        for a, b in (1, 0), (0, 1), (-1, 0), (0, -1):
            area = view_cctv(x, y, a, b)
            search_area(cctv, k+1, n)
            for nx, ny in area:
                office[nx][ny] = 0
    elif t == 2:
        for a, b, c, d in (1, 0, -1, 0), (0, 1, 0, -1):
            area1 = view_cctv(x, y, a, b)
            area2 = view_cctv(x, y, c, d)
            search_area(cctv, k+1, n)
            for nx, ny in area1:
                office[nx][ny] = 0
            for nx, ny in area2:
                office[nx][ny] = 0
    elif t == 3:
        for a, b, c, d in (1, 0, 0, 1), (1, 0, 0, -1), (-1, 0, 0, -1), (-1, 0, 0, 1):
            area1 = view_cctv(x, y, a, b)
            area2 = view_cctv(x, y, c, d)
            search_area(cctv, k+1, n)
            for nx, ny in area1:
                office[nx][ny] = 0
            for nx, ny in area2:
                office[nx][ny] = 0
    elif t == 4:
        for a, b, c, d, e, f in (1, 0, 0, 1, 0, -1), (1, 0, 0, -1, -1, 0), (-1, 0, 0, -1, 0, 1), (-1, 0, 0, 1, 1, 0):
            area1 = view_cctv(x, y, a, b)
            area2 = view_cctv(x, y, c, d)
            area3 = view_cctv(x, y, e, f)
            search_area(cctv, k+1, n)
            for nx, ny in area1:
                office[nx][ny] = 0
            for nx, ny in area2:
                office[nx][ny] = 0
            for nx, ny in area3:
                office[nx][ny] = 0
    elif t == 5:
        a, b, c, d, e, f, g, h = 1, 0, -1, 0, 0, 1, 0, -1
        area1 = view_cctv(x, y, a, b)
        area2 = view_cctv(x, y, c, d)
        area3 = view_cctv(x, y, e, f)
        area4 = view_cctv(x, y, g, h)
        search_area(cctv, k+1, n)
        for nx, ny in area1:
            office[nx][ny] = 0
        for nx, ny in area2:
            office[nx][ny] = 0
        for nx, ny in area3:
            office[nx][ny] = 0
        for nx, ny in area4:
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