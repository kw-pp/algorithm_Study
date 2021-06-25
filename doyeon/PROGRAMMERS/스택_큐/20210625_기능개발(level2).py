# Deque 사용
from collections import deque

def solution(progresses, speeds):
    answer = []
    
    # 작업의 진도와 개발 속도를 deque로 만듦
    dq1 = deque(progresses)
    dq2 = deque(speeds)
    
    # 날마다 개발 속도만큼 작업의 진도를 증가시켜 100이 되었을 때, deque에서 제거하고 기록
    while(dq1):
        release = 0
        
        for i in range(len(dq2)):
            dq1[i] += dq2[i]
        
        while 1:
            if dq1 and dq1[0] >= 100:
                release += 1
                dq1.popleft()
                dq2.popleft()
            else:
                break
        
        if release:
            answer.append(release)
            
    return answer

# Deque 사용X
def solution(progresses, speeds):
    answer = []
    N = len(progresses)
    p = 0 # 포인터
    while N!=p:
        tmp = 0
        for i in range(p, N):
            progresses[i] += speeds[i]
            
        if progresses[p] >= 100:
            for i in range(p, N):
                if progresses[i] >= 100:
                    tmp += 1
                else:
                    break
                    
            answer.append(tmp)
            p+=tmp
        
    return answer