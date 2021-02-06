n, k = map(int, input().split())
count = 0

money = []
for i in range(n):
  money.append(int(input()))

# 큰 단위의 화폐부터 차례대로 확인
money.sort(reverse=True)
for i in money:
  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
  count += k // i
  k %= i
print(count)