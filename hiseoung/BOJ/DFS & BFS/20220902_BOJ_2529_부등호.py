import sys
input = sys.stdin.readline

k = int(input())
signs = input().strip().split()
is_visited = [False for _ in range(10)]
_max = float('-inf')
_min = float('inf')
answer = []

def dfs(k):
    global _max, _min
    # 탈출 조건 : 현재 부등호 개수보다 배열 요소가 하나 더 많은 경우
    if k == len(signs):
        val = int(''.join(answer))
        _max = max(_max, val)
        _min = min(_min, val)
        return
    for i in range(10):
        if signs[k] == '<':
            if int(answer[-1]) < i and not is_visited[i]:
                is_visited[i] = True
                answer.append(str(i))
                dfs(k+1)
                is_visited[i] = False
                answer.pop()
        elif signs[k] == '>':
            if int(answer[-1]) > i and not is_visited[i]:
                is_visited[i] = True
                answer.append(str(i))
                dfs(k+1)
                is_visited[i] = False
                answer.pop()


for i in range(10):
    is_visited[i] = True
    answer.append(str(i))
    dfs(0)
    is_visited[i] = False
    answer.pop()


print(_max) if k + 1 == len([*str(_max)]) else print('0' + str(_max))
print(_min) if k + 1 == len([*str(_min)]) else print('0' + str(_min))