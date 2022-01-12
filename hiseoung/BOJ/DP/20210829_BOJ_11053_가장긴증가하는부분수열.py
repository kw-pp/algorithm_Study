import sys


def solution(n, arr):
    '''
    출처 :  https://www.acmicpc.net/problem/11053
    문제 유형 : 다이나믹 프로그래밍(DP)
    - sort로 해결 X -> 수열내 위치가 변화하면 안되서 적합하지 않음
    '''

    table = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                table[i] = max(table[i], table[j]+1)

    return max(table)


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

print(solution(n, arr))