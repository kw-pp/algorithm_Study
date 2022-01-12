from collections import deque
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
mat = []

for i in range(m):
    mat.append(list(map(int, sys.stdin.readline().split())))

# BFS를 위한 deque선언
queue = deque()

# 연결되어 있는 노드를 집합에 추가해서 집합의 길이를 출력
li = set([])
i = 0

# 1번 노드와 연결되어있는 모든 값들을 큐에 넣어줌
for _ in range(len(mat)):
    if mat[i][0] == 1:
        queue.append(mat[i][1])
        del mat[i]
        continue
    elif mat[i][1] == 1:
        queue.append(mat[i][0])
        del mat[i]
        continue
    else:
        i += 1

# 큐에 남아있는 값이 없을 때까지 반복
while queue:
    a = queue.popleft()
    li.add(a)
    j = 0

    while True:
        if j == len(mat):
            break

        if mat[j][0] == a:
            queue.append(mat[j][1])
            del mat[j]
        elif mat[j][1] == a:
            queue.append(mat[j][0])
            del mat[j]
        else:
            j += 1

print(len(li))
