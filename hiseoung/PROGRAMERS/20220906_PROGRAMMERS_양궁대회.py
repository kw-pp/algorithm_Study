from copy import deepcopy

_max = float('-inf')
answer = list()


def dfs(k, m, lion, apeach, is_visited):
    global _max, answer
    # 종료 조건 : 모든 과녘을 순회한 경우
    if m > 10:
        l_score, a_score = 0, 0
        for i in range(11):
            # 둘 다 과녘에 명중하지우못한 경우
            if lion[i] == 0 and apeach[i] == 0:
                continue
            # 라이언이 더 많이 맞춘 경우, 라이언 점수를 늘려준다.
            elif lion[i] > apeach[i]:
                l_score += 10 - i
            # 그 외의 경우, 어피치 점수를 늘려준다.
            else:
                a_score += 10 - i
        # 점수 계산 : 라이언 점수가 더 크고, 점수 차가 이전의 최댓값보다 더 큰 경우
        if l_score > a_score and _max < l_score - a_score:
            _max = l_score - a_score
            answer = list()  # 이전 값 초기화
            answer.append(deepcopy(lion))
        # 점수 계산 : 점 수 차가 이전 최댓값과 동일한 경우
        elif l_score > a_score and _max == l_score - a_score:
            answer.append(deepcopy(lion))
        return

    # 방문 처리가 되어 있지 않은 과녘만 탐색
    if not is_visited[m]:
        # 과녘에 들어갈 수 있는 최대 화살은 어피치 점수보다 하나 큰 경우까지이므로 해당 범위까지 탐색
        for j in range(apeach[m] + 2):
            if j <= k and lion[m] + j <= apeach[m] + 1:
                lion[m] += j
                is_visited[m] = True
                dfs(k - j, m + 1, lion, apeach, is_visited)
                lion[m] -= j
                is_visited[m] = False

def solution(n, info):
    global answer
    lion = [0 for _ in range(11)]
    is_visited = [False for _ in range(11)]

    dfs(n, 0, lion, info, is_visited)

    if answer:
        answer.sort(key=lambda x:(x[10], x[9], x[8], x[7], x[6], x[5], x[4], x[3], x[2], x[1], x[0]))
        return answer[-1]
    else:
        return [-1]