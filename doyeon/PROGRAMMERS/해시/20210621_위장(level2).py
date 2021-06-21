def solution(clothes):
    # dict를 만들어서 의상이 해당하는 종류(key)에 1씩 더하기
    hash_map = {}
    for i in clothes:
        if i[1] in hash_map:
            hash_map[i[1]]+=1
        else:
            hash_map[i[1]] = 1
    
    # 의상을 고를 경우의 수를 곱해줌
    # 1을 더해주는 경우는 안 고를 경우
    answer = 1
    for i in hash_map.values():
        answer *= (i+1)
    
    # 모두 안 입은 경우 1을 빼줌
    return answer-1