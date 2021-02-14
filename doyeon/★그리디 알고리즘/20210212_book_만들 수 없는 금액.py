n = int(input())
nums = list(map(int, input().split()))
nums.sort()
target = 1
for i in nums:
    # 만들 수 엇ㅂ는 금액을 찾았을 때 반복 종료
    if target < i:
        break
    target += i
print(target)