N = int(input())
result = 0

# 1부터 N까지 숫자 
for i in range(1, N+1):
  # 각 자리수를 A 리스트에 넣기
  A = list(map(int, str(i)))
  # 숫자 + 각 자리수 합
  result = i + sum(A)
  # 생성자가 있을 경우 숫자 출력
  if result == N:
    print(i)
    break
  # 생성자가 없을 경우 0 출력
  if i == N:
    print(0)