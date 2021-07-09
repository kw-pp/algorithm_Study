def solution(citations):
    citations.sort()
    answer = 0
    for i in range(len(citations)):
        count = 0
        for j in range(len(citations)):
            if citations[j] >= i+1:
                count += 1
        if i+1 == count:
            answer = count
    return answer