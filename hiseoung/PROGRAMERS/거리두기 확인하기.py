from collections import deque

def bfs(table):
    table = [list(row) for row in table]
    candidates = []
    flag = 1

    for i in range(5):
        for j in range(5):
            if table[i][j] == 'P':
                candidates.append((i, j))

    for row in candidates:
        if not flag:
            break
        q = deque([(row[0], row[1])])
        is_visited = [[False] * 5 for _ in range(5)]
        is_visited[row[0]][row[1]] = True

        for _ in range(2):
            for _ in range(len(q)):
                x, y = q.popleft()
                for a, b in (1, 0), (0, 1), (-1, 0), (0, -1):
                    nx = x + a
                    ny = y + b
                    if 0 <= nx < 5 and 0 <= ny < 5 and not is_visited[nx][ny] and table[nx][ny] != 'X':
                        if table[nx][ny] == 'O':
                            q.append((nx, ny))
                            is_visited[nx][ny] = True
                        elif table[nx][ny] == 'P':
                            flag = 0
    return flag

def solution(places):
    answer = []
    for table in places:
        answer.append(bfs(table))
    return answer