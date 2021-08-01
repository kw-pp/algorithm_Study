from collections import deque

def solution(n, computers):
    '''
    출처 : https://programmers.co.kr/learn/courses/30/lessons/43162
    문제 유형 : DFS/BFS
    - 비어있는 2차원 배열을 선언할 때는 li = [ [] for _ in range(n) ] 이런 식으로 사용할 것!
    - 그래프를 표현하는 두가지 방법 : 인접행렬 & 인접리스트
    '''

    # BFS 구현을 위한 큐를 선언합니다.
    q = deque()
    answer = 0
    # 노드의 방문여부를 확인할 수 있는 리스트를 선언합니다.
    is_visited = [False] * n

    for v in range(n):
        # 방문하지 않은 노드를 추가해 새로운 네트워크를 시작합니다.
        if is_visited[v]:
            continue
        else:
            q.append(v)

        # 큐에 값이 없다면 하나의 네트워크가 완성됩니다.
        while q:
            x = q.popleft()
            for y in range(n):
                if x != y and computers[x][y] == 1 and not is_visited[y]:
                    is_visited[y] = True
                    q.append(y)

        # 네트워크 개수를 추가합니다.
        answer += 1

    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))