from collections import deque


def solution(numbers, target):
    '''
    출처 : https://programmers.co.kr/learn/courses/30/lessons/43165
    문제 유형 : DFS & BFS
    새롭게 알게 된 내용
    - DFS는 스택을 활용, BFS는 큐를 활용한 탐생 방법
    '''

    li = [0]

    for i in numbers:
        temp = []

        for j in li:
            temp.append(j + i)
            temp.append(j - i)

        li = temp

    return li.count(target)

