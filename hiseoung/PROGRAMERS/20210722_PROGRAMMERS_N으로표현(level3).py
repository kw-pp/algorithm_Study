def solution(N, number):
    answer = -1
    dp = []

    for i in range(1, 9):

        temp = set()
        temp.add(int(str(N) * i))

        for j in range(0, i - 1):
            for x in dp[j]:
                for y in dp[-j - 1]:
                    temp.add(x - y)
                    temp.add(x + y)
                    temp.add(x * y)
                    if y != 0:
                        temp.add(x // y)
        if number in temp:
            answer = i
            break
        dp.append(temp)

    return answer