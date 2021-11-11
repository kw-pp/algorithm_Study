import sys
from collections import deque

dfsList = []
def solution1260():
    '''
    출처 : https://www.acmicpc.net/problem/11404
    분류 : DFS / BFS
    시간복잡도 :
    '''

    n, m, idx = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]

    for i in range(m):
        k, v = map(int, sys.stdin.readline().split())
        graph[k].append(v)
        graph[v].append(k)

    is_visited = [False for _ in range(n + 1)]
    is_visited[idx] = True
    dfs(graph, idx, is_visited)
    for i in dfsList:
        print(i, end=' ')
    print()
    is_visited = [False for _ in range(n + 1)]
    bfs(graph, idx, is_visited)



def dfs(graph, start, is_visited):
    global dfsList

    if len(graph) - 1 == len(dfsList):
        return dfsList
    else:
        dfsList.append(start)

    graph[start].sort()
    for i in graph[start]:
        if is_visited[i] is False:

            is_visited[i] = True
            dfs(graph, i, is_visited)


def bfs(graph, start, is_visited):
    answer = []

    q = deque()
    q.append(start)
    is_visited[start] = True

    while q:
        k = q.popleft()
        answer.append(k)

        graph[k].sort()
        for i in graph[k]:
            if is_visited[i] is False:
                is_visited[i] = True
                q.append(i)

    for i in answer:
        print(i, end=' ')
    return answer


solution1260()

