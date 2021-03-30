import sys
input = sys.stdin.readline

def knap_sack(N, K):
    dp = {0: 0}
    for _ in range(N):
        W, V = map(int, input().split())
        temp = {}
        for k,v in dp.items():
            # 기존 item의 무게 (k) 와 새로운 item의 무게(W)의 합이 전체 무게(K)보다 작거나 같은 경우
            # 그리고, ? 
            if k + W <= K and v + V > dp.get(k+W,0): # get(key가 없는경우, 'default'값 반환)
                temp[k + W] = v + V

        dp.update(temp)
        print(temp)
    print(dp)
        
    return max(dp.values())


N, K = map(int, input().split())
print(knap_sack(N, K))

