def solution(name):
    name = list(name)
    answer = 0
    i = 0
    
    while True:
        answer += min(ord(name[i])-ord('A'), ord('Z')-ord(name[i])+1)
        name[i] = 'A'
        
        if name.count('A') == len(name) : return answer
        
        # 왼쪽과 오른쪽 중, 바꿔야 할 문자가 더 가까이 위치한 곳을 찾아 이동
        left, right = 1,1
        for l in range(1,len(name)):
            if name[i-l] == 'A': left += 1
            else: break
        
        for r in range(1,len(name)):
            if name[i+r] == 'A': right += 1
            else: break
        
        # 왼쪽과 오른쪽 모두 이동 거리가 같을 경우, 오른쪽으로 이동해야 한다.
        if left < right:
            answer += left
            i -= left
        else:
            answer += right
            i += right
            
    return answer