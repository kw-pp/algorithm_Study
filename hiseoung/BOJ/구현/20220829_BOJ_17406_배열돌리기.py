import sys
from itertools import permutations
from copy import deepcopy
input = sys.stdin.readline

n, m, k = map(int, input().split())
table_prev = [[*map(int, input().split())] for _ in range(n)]
order = [(*map(int, input().split()), ) for _ in range(k)]
order_list = permutations(order, len(order)) # 가능한 모든 순서 내에서 배열 A의 최솟값 도출
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
min_val = float('inf')

def rotate_table(r, c, s):
    # 재귀 탈출 조건 : s 값이 0인 경우 즉, 중심값에 도달해서 더 이상 연산이 필요없는 경우
    if s == 0:
        return
    # 시작값 : 왼, 위
    x = r - s
    y = c - s
    # 회전 연산을 위해 연산 내 유지해야할 캐시값
    temp_prev = table[x][y]
    for a, b in dirs:
        while True:
            # 현재 방향 내에서 범위를 만족
            if r-s <= x + a <= r+s and c-s <= y + b <= c+s:
                temp_next = table[x + a][y + b]
                table[x + a][y + b] = temp_prev
                temp_prev = temp_next
                x = x + a
                y = y + b
            # 현재 방향 내에서 범위를 만족하지 못하므로 다음 방향으로 연산 진행
            else:
                break

    return rotate_table(r, c, s - 1)


for li in order_list:
    table = deepcopy(table_prev)
    for r, c, s in li:
        rotate_table(r - 1, c - 1, s)
    min_val = min(min_val, min([sum(row) for row in table]))

print(min_val)
