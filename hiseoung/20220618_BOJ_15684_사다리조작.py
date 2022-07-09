import sys

def check():
    # i번 세로선의 결과가 i번이 나오는지 체크
    for i in range(n):
        temp = i     # 이동하는 세로선 위치
        for j in range(h):
            if graph[j][temp]:  # 오른쪽이 1인 경우
                temp += 1
            elif temp > 0 and graph[j][temp - 1]: # 왼쪽이 1인 경우
                temp -= 1
        if temp != i:
            return False
    return True


def dfs(cnt, x, y):
    """
    :  param cnt: 가로선을 만든 횟수
    """
    global ans
    if ans <= cnt:   # 가로선을 정답보다 많이 만든 경우 확인 필요 x
        return
    if check():      # i번 세로선의 결과가 i번이 나오는지 체크
        ans = min(ans, cnt)
        return
    if cnt == 3:
        return
    for i in range(x, h):
        k = y if i == x else 0     # 같은 세로줄 확인하면 y부터 확인. 세로줄 다르면 0부터
        for j in range(k, n - 1):
            if graph[i][j] == 0: # 0인 경우 가로줄 만들고, 연속된 가로선을 만들지 않기 위해 j + 2호출
                graph[i][j] = 1
                dfs(cnt + 1, i, j + 2)
                graph[i][j] = 0


n, m, h = map(int, sys.stdin.readline().split())  # 세로, 가로, 세로선마다 가로선을 놓을수 있는 위치 수
graph = [[0]*n for _ in range(h)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split()) # 가로, 세로선
    graph[a - 1][b - 1] = 1

ans = 4
dfs(0, 0, 0)
print(ans if ans <= 3 else -1)