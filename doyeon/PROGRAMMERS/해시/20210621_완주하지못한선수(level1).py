def solution(participant, completion):
    maraton = {}
    answer = ''
    
    # 참가자 리스트를 순회하면서 maraton 딕셔너리에 key:value 값으로 추가해주기
    # 동명이인이 있으면 같은 이름의 key를 찾아서 +1 해주고,
    # 없으면 key, value=1추가
    for i in participant:
        if i in maraton:
            maraton[i] += 1
        else:
            maraton[i] = 1
    
    # 완주자 리스트 값이 maraton 딕셔너리에 존재한다면 -1
    for j in completion:
        maraton[j] -= 1
    
    # value가 0이 아니면 완주자가 아니다.
    for k, v in maraton.items():
        if v!=0:
            answer = k
            break
            
    return answer