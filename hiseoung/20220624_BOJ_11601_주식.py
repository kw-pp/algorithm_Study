import sys
# 1 2 3 4 5 6 7 1 2 5 1 2 4
T = int(sys.stdin.readline())
for _ in range(T):
    # 사용자 값 입력
    N = int(sys.stdin.readline())
    stock = list(map(int, sys.stdin.readline().split()))
    reversed_stock = sorted(stock)
    is_visited = [0 for _ in range(10001)]
    for i in stock:
        is_visited[i] += 1

    val = reversed_stock.pop()
    profit = 0

    for i in range(N):
        if stock[i] < val:
            profit += (val - stock[i])
            is_visited[stock[i]] -= 1
        elif stock[i] == val:
            is_visited[stock[i]] -= 1
            for i in range(len(reversed_stock)-1, -1, -1):
                if is_visited[reversed_stock[-1]] == 0:
                    reversed_stock.pop()
                else:
                    val = reversed_stock.pop()
                    break

    print(profit)