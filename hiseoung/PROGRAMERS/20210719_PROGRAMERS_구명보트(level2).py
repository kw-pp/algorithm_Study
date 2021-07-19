def solution(people, limit):
    j = 0
    answer = 0
    people.sort()
    for i in range(len(people)):
        if j == len(people):
            break
        if j < len(people) - 1 and people[j] + people[j+1] <= limit:
            answer += 1
            j += 2
        else:
            answer += 1
            j += 1
    return answer