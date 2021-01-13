# N개의 정수가 주어질때, 최솟값과 최댓값을 구한다.
num = int(input()) #다른 언어일때는 입력받는 수의 개수를 입력해야 하기 때문에. python은 안쓴다.
L = list(map(int, input().split()))

print(min(L), end=' ')
print(max(L))
