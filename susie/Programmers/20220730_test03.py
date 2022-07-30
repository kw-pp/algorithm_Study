from collections import deque

def solution(order):
    answer = 0
    belt = deque([x for x in range(1, len(order)+1)]) #컨테이너 벨트는 queue
    assist = [0] #보조 컨테이너는 스택
    order = deque(order)

    while order:
        if len(belt) == 0 and order[0] != assist[-1]:
            break
        
        # 물류 순서 만족 조건
        if order[0] == assist[-1]:
            order.popleft()
            assist.pop()
            answer += 1
        
        if len(order) == 0:
            break

        if belt and order[0] != belt[0]:
            assist.append(belt.popleft())
        elif belt and order[0] == belt[0]:
            order.popleft()
            belt.pop()
            answer += 1
        else:
            continue
            
    return answer
