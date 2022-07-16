import sys

answer = 0
n, m = map(int, sys.stdin.readline().split())

table = [['0'] * m for _ in range(n)]

queen = []
knight = []
pawn = []

q_dx = [1, 1, 1, -1, -1, -1, 0, 0]
q_dy = [0, -1, 1, 0, 1, -1, 1, -1]
k_dx = [2, 2, -2, -2, 1, 1, -1, -1]
k_dy = [-1, 1, -1, 1, 2, -2, 2, -2]

q_pos = list(map(int, sys.stdin.readline().split()))
k_pos = list(map(int, sys.stdin.readline().split()))
p_pos = list(map(int, sys.stdin.readline().split()))

q = q_pos.pop(0)
k = k_pos.pop(0)
p = p_pos.pop(0)

for i in range(0, 2 * q, 2):
    queen.append((q_pos[i] - 1, q_pos[i + 1] - 1))

for i in range(0, 2 * k, 2):
    knight.append((k_pos[i] - 1, k_pos[i + 1] - 1))

for i in range(0, 2 * p, 2):
    pawn.append((p_pos[i] - 1, p_pos[i + 1] - 1))

for i in queen:
    table[i[0]][i[1]] = 'Q'

for i in knight:
    table[i[0]][i[1]] = 'K'

for i in pawn:
    table[i[0]][i[1]] = 'P'


def knight(x, y):
    for i in range(8):
        nx = x + k_dx[i]
        ny = y + k_dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if table[nx][ny].isalpha():
            continue

        table[nx][ny] = '1'
    return


def queen(x, y):
    for i in range(8):
        for scale in range(1, max(n, m)):

            nx = x + scale * q_dx[i]
            ny = y + scale * q_dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                break

            if table[nx][ny].isalpha():
                break

            table[nx][ny] = '1'
    return


for i in range(n):
    for j in range(m):
        if table[i][j] == 'K':
            knight(i, j)
        elif table[i][j] == 'Q':
            queen(i, j)

for i in table:
    answer += i.count('0')
print(answer)
