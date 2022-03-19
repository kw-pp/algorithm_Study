import sys

direction = {
    0: "NORTH",
    1: "EAST",
    2: "SOUTH",
    3: "WEST"
}

N, M = map(int, sys.stdin.readline().split())
row, col, way = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cleaned = [[False]*M for _ in range(N)]  # 청소한지 체크.
stack = [(row, col)]  # dfs를 위한 stack
cnt = 0

while True:
    if stack:  # 새롭게 청소할 곳이 있으면 청소.
        row, col = stack.pop()
        cleaned[row][col] = True
        cnt += 1

    for _ in range(4):
        way = (way + 3) % 4  # 왼쪽으로 방향 전환

        if direction[way] == "NORTH":  # 전진 준비
            new_row = row - 1
            new_col = col
        elif direction[way] == "EAST":
            new_row = row
            new_col = col + 1
        elif direction[way] == "SOUTH":
            new_row = row + 1
            new_col = col
        elif direction[way] == "WEST":
            new_row = row
            new_col = col - 1

        if table[new_row][new_col] != 1 and not cleaned[new_row][new_col]:  # 나아갈 곳이 벽이 아니고 청소 안한 곳이면
            stack.append((new_row, new_col))  # 청소할 곳으로 추가
            break

    if not stack:  # 네방향 다 탐색했는데도 청소할 곳이 없으면
        if direction[way] == "NORTH":  # 후진 준비
            new_row = row + 1
            new_col = col
        elif direction[way] == "EAST":
            new_row = row
            new_col = col - 1
        elif direction[way] == "SOUTH":
            new_row = row - 1
            new_col = col
        elif direction[way] == "WEST":
            new_row = row
            new_col = col + 1

        if table[new_row][new_col] == 1:  # 뒤에 벽이라면 종료
            break
        else:  # 후진
            row = new_row
            col = new_col
print(cnt)
