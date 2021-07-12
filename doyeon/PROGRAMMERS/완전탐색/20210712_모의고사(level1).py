def solution(answers):
    answer = []
    m1 = [1, 2, 3, 4, 5]
    m2 = [2, 1, 2, 3, 2, 4, 2, 5]
    m3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    result = [0] * 3

    for index, ans in enumerate(answers):
        if ans == m1[index % len(m1)]:
            result[0] += 1
        if ans == m2[index % len(m2)]:
            result[1] += 1
        if ans == m3[index % len(m3)]:
            result[2] += 1

    max_grade = max(result)
    for i, j in enumerate(result):
        if max_grade == j:
            answer.append(i + 1)

    return answer