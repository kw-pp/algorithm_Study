
def solution(n, results):
    graph = [[float('inf')] * (n+1) for _ in range(n+1)]

    for x, y in results:
        graph[x][y] = 1
        graph[y][x] = -1

    for x in range(1, n+1):
        for y in range(1, n+1):
            if x == y:
                graph[x][y] = 0


    for k in range(1, n+1):
       for x in range(1, n+1):
           for y in range(1, n+1):
               if graph[x][k] == 1 and graph[k][y] == 1 and graph[x][y] != 0:
                   graph[x][y] = 1
               elif graph[x][k] == -1 and graph[k][y] == -1 and graph[x][y] != 0:
                   graph[x][y] = -1

    count = 0
    for i in range(1, n+1):
        check = 0
        for j in range(1, n+1):
            if graph[i][j] == float('inf'):
                check = 1
                break
        if not check:
            count += 1
    return count






n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

print(solution(n, results))