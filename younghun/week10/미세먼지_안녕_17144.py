import sys
from copy import deepcopy

r, c, time = map(int, sys.stdin.readline().split())

room = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
cleaner = []
answer = 0


def spread(room):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    new_room = deepcopy(room)
    for i in range(r):
        for j in range(c):

            if room[i][j] == -1:
                cleaner.append(i)

            if room[i][j] >= 5:
                piece = room[i][j] // 5
                for k in range(4):
                    new_row = i + dx[k]
                    new_col = j + dy[k]

                    if new_row < 0 or new_row >= r or new_col < 0 or new_col >= c:
                        continue
                    if room[new_row][new_col] == -1:
                        continue

                    new_room[new_row][new_col] += piece
                    new_room[i][j] -= piece
    return new_room


def clean_up(room):
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = cleaner[0], 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == cleaner[0] and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        room[x][y], before = before, room[x][y]
        x = nx
        y = ny
    return room


def clean_down(room):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = cleaner[1], 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == cleaner[1] and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        room[x][y], before = before, room[x][y]
        x = nx
        y = ny
    return room


while time != 0:
    room = clean_down(clean_up(spread(room)))
    time -= 1

for i in range(r):
    for j in range(c):
        if room[i][j] > 0:
            answer += room[i][j]
print(answer)
