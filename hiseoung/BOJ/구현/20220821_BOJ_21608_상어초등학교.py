import sys
input = sys.stdin.readline

n = int(input())
info_list = [*reversed([[*map(int, input().split())] for _ in range(n**2)])]
table = [[0] * n for _ in range(n)]
is_visited = [[False] * n for _ in range(n)]
info_dict = dict()
answer = 0

# 주어진 학생 정보를 순서대로 탐색 ( 완전 탐색 )
while info_list:
    student_info = info_list.pop()
    num = student_info[0]
    liked = student_info[1:]
    info_dict[num] = liked
    seat_info = []
    # 모든 좌석을 탐색하면서 해당 영역에서 발생 할 수 있는 모든 케이스 계산 후 배열 추가
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
    # 계산을 통해 추가한 모든 후보 좌석에 대해서 조건 기준에 따라서 정렬 후 최적값을 테이블에 갱신
    seat_info.sort(key=lambda x:(x[0], x[1], -x[2], -x[3]))
    seat = seat_info[-1]
    table[seat[2]][seat[3]] = num
    is_visited[seat[2]][seat[3]] = True

# 점수 계산
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
