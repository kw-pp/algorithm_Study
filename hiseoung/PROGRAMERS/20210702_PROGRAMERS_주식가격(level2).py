def solution(prices):
    answer = [0] * len(prices)
    l = len(prices)

    for i in range(l - 1):
        for j in range(i, l - 1):

            if prices[i] > prices[j]:
                break
            else:
                answer[i] += 1

    return answer