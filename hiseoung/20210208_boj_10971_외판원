#도시의 개수
N = int(input())

Edge = []
#도시간 이동비용(가중치 행렬)
for i in range(N):
    Edge.append(list(map(int, (input().split()))))

#이동 경로(도시 방문 확인용)
path = [False for i in range(N)]

#최소비용
Min = 1000000000

def dfs(start, cur_pos, sum, cnt):

    global Min
    try:
        # 탈출 조건
        if cnt == N and start == cur_pos:
            # print(1)
            if Min > sum:
                Min = sum
                return

        for z in range(N):
            # print("여긴 들어가냐?")
            if Edge[cur_pos][z] == 0:
                # print("간선 연결 안됨")
                continue

            if not path[cur_pos] and Edge[cur_pos][z] > 0:
                path[cur_pos] = True
                sum += Edge[cur_pos][z]
                # print(str(sum))

                if (sum <= Min):
                    dfs(start, z, sum, cnt + 1)

                path[cur_pos] = False
                sum -= Edge[cur_pos][z]

    except IndexError:
        pass

for i in range(N):
    dfs(i, i, 0, 0)
print(Min)
