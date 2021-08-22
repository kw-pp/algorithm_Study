import heapq


def solution(n, edge):
    '''
    출처 : https://programmers.co.kr/learn/courses/30/lessons/49189
    문제 유형 : 그래프
    - 문제를 풀어가는 방법이 다양하게 있을 것 같다.
    - 다익스트라 알고리즘이 생각나서 이를 이용해 문제를 풀이했다.
    - 시간복잡도 : O(E * logV)
    '''
    
    # 간선 정보를 입력받을 2차원 리스트를 선언합니다.
    graph = [[] for _ in range(n+1)]
    
    # 연결되어 있는 모든 노드 사이의 Edge값에 1을 추가합니다.
    for x, y in edge:
        graph[x].append((y, 1))
        graph[y].append((x, 1))
    
    # 시작 노드와 나머지 노드들 사이의 최단거리 정보를 담을 1차원 리스트의 값을 무한대의 값으로 초기화해 선언합니다.
    distance = [float('inf')] * (n + 1)
    
    # 문제에서 명시된 시작노드 번호를 변수에 담아줍니다.
    start = 1

    # 진행 경로에서 그 다음의 최단경로 값을 넣고 뺄 수 있도록 우선순위 큐를 선언합니다.
    q = []
    
    # 시작노드 값을 우선순위 큐에 넣습니다.
    heapq.heappush(q, (0, start))
    
    # 최단경로 테이블의 시작노드 값을 0으로 초기화합니다.
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        for i in graph[now]:
            # 진행 노드의 값에 현재 연결된 노드의 edge값을 더해 다음 노드로의 거리를 구합니다.
            cost = dist + i[1]
            
            # 계산한 거리 값이 최단거리 테이블 상의 값보다 작다면 해당 값으로 수정합니다.
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    del distance[0]
    Max = max(distance)
    return distance.count(Max)
