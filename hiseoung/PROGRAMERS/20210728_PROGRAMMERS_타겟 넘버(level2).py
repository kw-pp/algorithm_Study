from collections import deque

def solution(numbers, target):
    '''
    출처 : https://programmers.co.kr/learn/courses/30/lessons/43165
    문제 유형 : DFS & BFS
    - DFS는 스택을 활용, BFS는 큐를 활용한 탐색 방법
    '''

    q = deque()
    li = [1, -1]
    for i in li:
        q.append(i * numbers[0])

    for idx in range(1, len(numbers)):
        for _ in range(len(q)):
            x = q.popleft()
            for i in li:
                q.append(x + (i * numbers[idx]))

    return q.count(target)
