import sys

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def solution(x, y ,count, arr):
    '''
    출처 : https://www.acmicpc.net/problem/1987
    티어 : 골드 4
    유형 : 그래프 탐색
    - 처음에 BFS로 접근했는데 경로상의 중복을 체크할 수 가 없음 -> DFS로 짜는게 나을 듯
    - DFS로 짜서 답은 맞추는데 시간초과...
    - bfs / dfs + 백트래킹기법이 추가되어야 풀이가 가능하다고 한다..

    '''
    global Max, r, c
    Max = max(count, Max)

    for a, b in zip(dx, dy):
        if 0 <= x + a < r and 0 <= y + b < c and not is_visited[ord(arr[x + a][y + b])]:
            is_visited[ord(arr[x + a][y + b])] = 1
            solution(x+a, y+b, count + 1, arr)
            is_visited[ord(arr[x + a][y + b])] = 0



r, c = map(int, sys.stdin.readline().split())
arr = []
for i in range(r):
    arr.append(list(sys.stdin.readline().strip()))
is_visited = [0] * 91
Max = float('-inf')
count = 1
is_visited[ord(arr[0][0])] = 1
solution(0, 0, count, arr)
print(Max)



# def solution(r, c, arr):
#     '''
#     출처 : https://www.acmicpc.net/problem/1987
#     티어 : 골드 4
#     유형 : 그래프 탐색
#     - 처음에 BFS로 접근했는데 경로상의 중복을 체크할 수 가 없음 -> DFS로 짜는게 나을 듯
#     '''
#     q = deque()
#     is_visited = [0] * 100
#     q.append((0, 0))
#     is_visited[ord(arr[0][0])] = 1
#     count = 0
#
#     while q:
#         print(q)
#         for _ in range(len(q)):
#             x, y = q.popleft()
#             for a, b in zip(dx, dy):
#                 if 0 <= x+a < r and 0 <= y+b < c and not is_visited[ord(arr[x+a][y+b])]:
#                     q.append((x+a, y+b))
#                     is_visited[ord(arr[x+a][y+b])] = 1
#         count += 1
#     return count

# a = set()
# for i in range(5):
#     for j in range(5):
#         a.add(arr[i][j])


