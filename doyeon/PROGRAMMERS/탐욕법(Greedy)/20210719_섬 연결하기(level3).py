def solution(n, costs):
    costs.sort(key=lambda x:x[2]) # cost 기준으로 오름차순 정렬
    routes = set([costs[0][0], costs[0][1]]) # set 자료구조에 출발, 도착 처음 지점
    answer = costs[0][2]
    
    while n != len(routes):
        for i, v in enumerate(costs[1:]):
            # 출발, 도착 지점이 둘 다 있으면 넘어감
            if v[0] in routes and v[1] in routes:
                continue
            # 하나만 있으면 섬 연결
            if v[0] in routes or v[1] in routes:
                routes.update([v[0], v[1]])
                answer += v[2]
                # costs 원래 리스트 값을 -1로 바꾸어주어 다시 해당 값을 사용하지 않게 함
                costs[i+1] = [-1, -1, -1]
                break
        
    return answer