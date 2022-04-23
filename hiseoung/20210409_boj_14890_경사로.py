import sys

N, L = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
path = 0

for i in range(N):
    is_visited = [False for _ in range(N)]
    flag = True
    for j in range(N-1):
        # 0. Flag 값이 False로 변경되어 있으면 Loop 탈출
        if not flag:
            break
        # 1. 현재 값과 다음 값이 같다면 계속 유지
        if table[i][j] == table[i][j+1]:
            continue
        # 2. 현재 값과 다음 값의 차이가 2이상 이라면 지나갈 수 없음
        if abs(table[i][j] - table[i][j+1]) > 1:
            flag = False
            break
        # 3. 현재 값보다 다음 값이 1크다면 경사로 설치 가능 여부를 체크함
        if table[i][j+1] - table[i][j] == 1:
            # 3.1 현재 값 기준으로 L 범위만큼 왼쪽 탐색
            for idx in range(L):
                if j - idx >= 0 and not is_visited[j-idx]:
                    is_visited[j-idx] = True
                else:
                    flag = False
        # 4. 현재 값보다 다음 값이 1 작다면 경사로 설치 가능 여부를 체크함
        if table[i][j+1] - table[i][j] == -1:
            # 4.1 현재 값 기준으로 L 범위만큼 오른쪽 탐색
            for idx in range(1, L+1):
                if j + idx < N and not is_visited[j+idx]:
                    is_visited[j+idx] = True
                else:
                    flag = False
    if flag:
        path += 1



for i in range(N):
    is_visited = [False for _ in range(N)]
    flag = True
    for j in range(N-1):
        # 0. Flag 값이 False로 변경되어 있으면 Loop 탈출
        if not flag:
            break
        # 1. 현재 값과 다음 값이 같다면 계속 유지
        if table[j][i] == table[j+1][i]:
            continue
        # 2. 현재 값과 다음 값의 차이가 2이상 이라면 지나갈 수 없음
        if abs(table[j][i] - table[j+1][i]) > 1:
            flag = False
            break
        # 3. 현재 값보다 다음 값이 1크다면 경사로 설치 가능 여부를 체크함
        if table[j+1][i] - table[j][i] == 1:
            # 3.1 현재 값 기준으로 L 범위만큼 왼쪽 탐색
            for idx in range(L):
                if j - idx >= 0 and not is_visited[j-idx]:
                    is_visited[j-idx] = True
                else:
                    flag = False
        # 4. 현재 값보다 다음 값이 1 작다면 경사로 설치 가능 여부를 체크함
        if table[j+1][i] - table[j][i] == -1:
            # 4.1 현재 값 기준으로 L 범위만큼 오른쪽 탐색
            for idx in range(1, L+1):
                if j + idx < N and not is_visited[j+idx]:
                    is_visited[j+idx] = True
                else:
                    flag = False
    if flag:
        path += 1

print(path)