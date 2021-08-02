from collections import defaultdict


def solution(tickets):
    answer = []
    adj = defaultdict(list)

    for ticket in tickets:
        adj[ticket[0]].append(ticket[1])

    for key in adj.keys():
        adj[key].sort(reverse=True)

    q = ['ICN']
    while q:
        tmp = q[-1]

        if not adj[tmp]:
            answer.append(q.pop())
        else:
            q.append(adj[tmp].pop())
    answer.reverse()
    return answer





from collections import deque

def solution(tickets):
    '''
    출처 : https://programmers.co.kr/learn/courses/30/lessons/43164
    문제 우형 : DFS/BFS
    - 테스트 케이스 1번이 안넘어감
    '''
    # BFS 구현을 위해 큐를 선언합니다.
    q = deque()

    # 방문 여부를 확인할 수 있는 리스트를 선언합니다.
    is_visited = [False] * len(tickets)

    # 티켓의 가장 처음 값을 큐에 추가합니다. 경로가 2개 이상이라면 알파벳 순서가 앞서는 경로를 추가합니다.
    breaker = False
    for z in range(len(tickets)):
        x, y = tickets[z]
        if len(q) == 0 and x == 'ICN':
            q.append([x, y])
        elif len(q) == 1 and x == 'ICN':
            for j in range(len(y)):
                if q[0][1][j] > y[j]:
                    q[0] = [x, y]
                    break

    for i in range(len(tickets)):
        if tickets[i] == q[0]:
            is_visited[i] = True
            break

    # 비행 경로를 담을 리스트를 선언하고 출발지를 추가합니다.
    path = [q[0][0]]
    idx = 1

    while q:
        # print(q)
        x, y = q.popleft()
        path.append(y)
        # Y(목적지)에 대응되는 tickets의 출발지가 있다면 임시 리스트에 추가합니다.
        temp = []
        for i in range(len(tickets)):
            if tickets[i][0] == y and not is_visited[i]:
                temp.append(tickets[i])
        # print(y)
        # print(temp)
        # print()

        # print(temp)
        if len(temp) != 0 and len(path) != len(tickets):
            z = 0
            for _ in range(len(temp)):
                count = 0
                for j in range(len(tickets)):
                    if temp[z][1] == tickets[j][0]:
                        count += 1
                if count == 0:
                    del temp[z]
                else:
                    z += 1

        # print(temp)

        if len(temp) != 0:
            temp.sort(key=lambda x: x[1])
            q.append(temp[0])
            for i in range(len(is_visited)):
                if temp[0] == tickets[i]:
                    is_visited[i] = True
                    break
        # print(q)
        # print()
    return path