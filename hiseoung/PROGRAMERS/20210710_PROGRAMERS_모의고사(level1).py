# https://kokooroom.tistory.com/3 문제 정리중!

def solution(answers):
    a = [1, 2, 3, 4, 5] * 2001
    b = [2, 1, 2, 3, 2, 4, 2, 5] * 2001
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 2001

    count = [0, 0, 0]
    answer = []
    li = []

    for i in range(len(answers)):
        if a[i] == answers[i]:
            count[0] += 1
        if b[i] == answers[i]:
            count[1] += 1
        if c[i] == answers[i]:
            count[2] += 1

    for i in enumerate(count):
        li.append(i)

    li.sort(key=lambda x: x[1], reverse=True)
    for i in range(3):
        answer.append(li[i][0] + 1)
        if i == 2:
            break
        if li[i][1] != li[i + 1][1]:
            break

    answer.sort()
    return answer