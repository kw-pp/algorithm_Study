import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

li = []
for i in range(m):
    li.append(list(map(int, sys.stdin.readline().split())))

check_list = [[0] * (n+1) for _ in range(n+1)]

for x in range(1, n+1):
    q = deque()
    count = 1
    is_visited = [False] * (n+1)

    for i in range(m):
        if li[i][0] == x:
            q.append(li[i][1])
            is_visited[li[i][1]] = True
            check_list[x][li[i][1]] = count
        if li[i][1] == x:
            q.append(li[i][0])
            is_visited[li[i][0]] = True
            check_list[x][li[i][0]] = count
    breaker = False
    while q:

        check = 0
        for i in range(len(is_visited)):
            if is_visited[i]:
                check += 1
        if check == n:
            break

        start = q.popleft()
        count += 1

        for i in range(m):
            for _ in range(len(q)):
                count += 1
                if li[i][0] == start:
                    q.append(li[i][1])
                    is_visited[li[i][1]] = True
                    check_list[x][li[i][1]] = count
                if li[i][1] == start:
                    q.append(li[i][0])
                    is_visited[li[i][0]] = True
                    check_list[x][li[i][0]] = count

Min = float('inf')
person = 0
for i in range(1, len(check_list)-1):
    a = sum(check_list[i])
    if Min < a:
        Min = a
        person = i
    elif Min == a:
        if person > i:
            person = i

print(person + 1)



