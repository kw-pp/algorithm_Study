import sys

n = int(sys.stdin.readline())
sequence = list(enumerate(map(int, (sys.stdin.readline().split()))))
answer = [0] * n  # NGE 넣을 배열.
stack = []

for i in range(n):

    while stack:  # 넣으려는 원소가 더 크면 반복.
        if sequence[i][1] <= stack[-1][1]:  # 넣으려는 원소가 stack에 있는 원소보다 작으면
            stack.append(sequence[i])  # 그냥 넣는다.
            break
        else:  # 넣으려는게 더 크면
            item = stack.pop()  # 기존에 있는 원소를 stack에서 빼고
            answer[item[0]] = sequence[i][1]  # NGE 값을 넣으려는 수로 세팅.

    if not stack:  # stack이 비었고
        if i == n-1:  # 마지막 원소라면 -1로 세팅
            answer[sequence[i][0]] = -1
        else:  # 그외엔 해당 숫자 stack에 넣어줌.
            stack.append(sequence[i])
if stack:  # 남은 원소들은 NGE를 구할 수 없는 원소들.
    for i in stack:
        answer[i[0]] = -1

for i in answer:
    print(i, end=" ")
