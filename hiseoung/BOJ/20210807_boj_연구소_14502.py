import sys
from collections import deque
from itertools import permutations
import copy
import time


N, M = map(int, sys.stdin.readline().split())
virus = []
Candidate = []

for i in range(N):
    virus.append(list(map(int, sys.stdin.readline().split())))

start = time.time()
for i in range(len(virus)):
    for j in range(len(virus[i])):
        if virus[i][j] == 1 or virus[i][j] == 2:
            for x, y in (1, 0), (0, 1), (-1, 0), (0, -1):
                if 0 <= i + x < N and 0 <= j + y < M and virus[i+x][j+y] == 0:
                    Candidate.append((i+x, j+y))

q = deque(list(permutations(Candidate, 3)))
Max = float('-inf')

while q:
    virus_temp = copy.deepcopy(virus)
    temp = q.popleft()
    for x, y in temp:
        virus_temp[x][y] = 1
    q2 = deque()
    for i in range(len(virus_temp)):
        for j in range(len(virus_temp[i])):
            if virus_temp[i][j] == 2:
                q2.append((i, j))
    while q2:
        for _ in range(len(q2)):
            a, b = q2.popleft()
            for x, y in (1, 0), (0, 1), (-1, 0), (0, -1):
                if 0 <= a + x < N and 0 <= b + y < M and virus_temp[a + x][b + y] == 0:
                    virus_temp[a+x][b+y] = 2
                    q2.append((a+x, b+y))

    Num = 0
    for i in virus_temp:
        Num += i.count(0)
    if Max < Num:
        Max = Num

print(Max)
print(time.time()-start)

