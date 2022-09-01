import sys


n, m = map(int, sys.stdin.readline().split())

moneys = [int(sys.stdin.readline()) for _ in range(n)]


def simulate(k, money_list):  # M번의 인출 횟수 내에 N일 동안 생활이 가능한 지 시뮬레이션.
    if max(money_list) > k:
        return False
    pocket = k
    cnt = 1
    for money in money_list:
        if pocket < money:
            pocket = k
            cnt += 1
        pocket -= money
    if cnt > m:
        return False
    return True


def binary_search(money_list):  # k의 최솟값을 찾기 위한 이분탐색.
    start = min(money_list)
    end = sum(money_list)
    target = end

    while start <= end:
        mid = (start + end) // 2

        if simulate(mid, money_list):
            end = mid - 1
            target = mid  # 현재 값보다 작은 값을 탐색할 때만 target에 저장.
        else:
            start = mid + 1
    return target


print(binary_search(moneys))

