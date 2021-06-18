def solution(participant, completion):
    maraton = {}
    answer = 0

    for i in participant:
        if maraton.get(i) != None:
            maraton[i] += 1
        else:
            maraton[i] = 1

    for j in completion:
        maraton[j] -= 1

    for k, v in maraton.items():
        if v != 0:
            answer = k
            break
    return answer