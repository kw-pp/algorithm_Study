import sys
input = sys.stdin.readline

n = int(input())
info = [[*map(int, input().split())] for _ in range(n**2)]

table = [[0] * n for _ in range(n)]
is_visited = [[False] * n for _ in range(n)]
# 자리를 지정하는 학생의 순서가 정해져 있음 -> 스택 자료구조 활용을 위해 리스트 뒤집기
info_list = list(reversed(info))
info_dict = dict()
answer = 0

while info_list:
    student_info = info_list.pop()
    num = student_info[0]
    liked = student_info[1:]
    info_dict[num] = liked
    seat_info = []
    for i in range(n):
        for j in range(n):
            if not is_visited[i][j]:
                # 0: 좋아하는 사람 수, 1: 비어있는 자리 수, 2: 행, 3:열
                temp = [0, 0, i, j]
                for a, b in (1, 0), (0, 1), (-1, 0), (0, -1):
                    nx = i + a
                    ny = j + b
                    if 0 <= nx < n and 0 <= ny < n:
                        if table[nx][ny] == 0:
                            temp[1] += 1
                        elif table[nx][ny] == liked[0]:
                            temp[0] += 1
                        elif table[nx][ny] == liked[1]:
                            temp[0] += 1
                        elif table[nx][ny] == liked[2]:
                            temp[0] += 1
                        elif table[nx][ny] == liked[3]:
                            temp[0] += 1
                seat_info.append(temp)
    seat_info.sort(key=lambda x:(x[0], x[1], -x[2], -x[3]))
    seat = seat_info[-1]
    table[seat[2]][seat[3]] = num
    is_visited[seat[2]][seat[3]] = True


for i in range(n):
    for j in range(n):
        count = 0
        for a, b in (1, 0), (0, 1), (-1, 0), (0, -1):
            nx = i + a
            ny = j + b
            if 0 <= nx < n and 0 <= ny < n:
                if info_dict[table[i][j]][0] == table[nx][ny]:
                    count += 1
                if info_dict[table[i][j]][1] == table[nx][ny]:
                    count += 1
                if info_dict[table[i][j]][2] == table[nx][ny]:
                    count += 1
                if info_dict[table[i][j]][3] == table[nx][ny]:
                    count += 1
        if count == 4:
            answer += 1000
        elif count == 3:
            answer += 100
        elif count == 2:
            answer += 10
        elif count == 1:
            answer += 1

print(answer)