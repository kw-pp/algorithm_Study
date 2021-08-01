from collections import deque

def solution(begin, target, words):
    '''
    출처 : https://programmers.co.kr/learn/courses/30/lessons/43163
    문제 유형 : DFS/BFS
    '''

    answer = 0

    # target값으로 변환할 수 없는 경우를 처음에 고려해줍니다.
    if target not in words:
        return 0

    # BFS 구현을 위해 큐를 선언합니다.
    q = deque()

    # 큐에 초기값을 추가합니다.
    q.append(begin)

    # 조건이 만족되었을 때 반복문을 빠져나오기 위한 제어 변수를 선언합니다.
    breaker = False

    while q:
        if breaker:
            break

        # 큐의 길이 만큼 반복문을 돌리고 해당 반복문이 끝날 때 진행 단계(answer)값을 추가합니다.
        for _ in range(len(q)):
            x = q.popleft()

            # target 값과 같다면 반복문을 빠져나옵니다.
            if x == target:
                breaker = True
                break

            for y in words:
                # 주어진 단어 x와 words 안에 있는 단어 사이에 서로 다른 문자의 개수를 체크해줄 변수를 선언합니다.
                count = 0
                for z in range(len(y)):
                    # 서로 다른 단어의 개수가 1개 이상이라면 조건을 만족하지 않으므로 반복문을 빠져나옵니다.
                    if count > 1:
                        break
                    if x[z] != y[z]:
                        count += 1
                # 서로 다른 단어의 개수가 하나라면 큐에 추가합니다.
                if count == 1:
                    q.append(y)
        answer += 1
    return answer - 1

begin = 'hit'
target = 'cog'
words = ['cog', 'log', 'lot', 'dog', 'dot', 'hot']

print(solution(begin, target, words))