def solution(answers):
    first = [1,2,3,4,5] 
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    fc = sc = tc = 0 # count
    for i in range(len(answers)): 
        if first[i%(len(first))] == answers[i]: fc+=1 
            # i(순서의 답) 과 정답패턴(fir,sec,thr) 이 같으면
            # first[i%(len(first))]는 만약 순서가 정답 패턴의 길이를 넘어섰을 경우 다시 처음부터 
        if second[i%(len(second))] == answers[i]: sc+=1
        if third[i%(len(third))] == answers[i]: tc+=1
    MAX = max(fc, sc, tc)
    answer = []
    if MAX == fc: answer.append(1) # 최댓값 리턴 
    if MAX == sc: answer.append(2)
    if MAX == tc: answer.append(3)
    return answer
