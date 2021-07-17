def solution(brown, yellow):
    # 약수찾기
    for a in range(1, int(yellow ** 0.5) + 1):
    
        if yellow % a == 0:
        # a와 짝이 되는 yellow의 약수
            b = yellow // a
            # 카펫의 가로, 세로길이인 [b + 2, a + 2]를 반환
            if 2 * a + 2 * b + 4 == brown:
                return [b + 2, a + 2]