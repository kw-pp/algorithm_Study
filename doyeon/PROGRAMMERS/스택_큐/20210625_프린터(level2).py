from collections import deque
 
def solution(priorities, location):
    answer = 0
    
    dq = deque()
    for i, p in enumerate(priorities):
        dq.append((i, p))
    
    # 중요도 높은 순으로 정렬
    priorities.sort(reverse=True)
    prioPointer = 0
    
    while 1:
        # 중요도가 제일 높다면 출력하고, 아니라면 다시 deque에 저장
        now = dq.popleft()
        
        if now[1] == priorities[prioPointer]:
            prioPointer += 1
            answer += 1
            if now[0] == location:
                break
        else:
            dq.append(now)
            
    return answer