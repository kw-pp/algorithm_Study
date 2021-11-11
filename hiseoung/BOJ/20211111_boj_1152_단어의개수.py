import sys

def solution1152():
    '''
    출처 : https://www.acmicpc.net/problem/1152
    분류 : 문자열
    시간복잡도 : O(1)? O(n)?
    '''

    sent = sys.stdin.readline().strip().split()
    return len(sent)


print(solution1152())