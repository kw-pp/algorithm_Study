def solution(number, k):
  stack = []
  for i in number:
    # stack의 마지막 값보다 넣으려고 하는 값이 클 때
    while stack and i>stack[-1]:
      # 삭제할 수 있는 값이 아직 있으면 stack에서 pop하고 삭제할 수 있는 값 하나 감소
      if k>0:
        stack.pop()
        k -= 1
      # 삭제할 수 있는 값 더 이상 없으면 while문 종료
      else:
        break
    # stack의 마지막 값이 넣으려고 하는 값 보다 크다면 그냥 넣어주기
    stack.append(i)

  # number문자열 끝까지 다 순회했는데 아직 삭제해야 할 갯수가 더 남아있으면 삭제해야 할 만큼 갯수만큼 stack의 제일 마지막 부분에서 pop
  if k>0:
    for i in range(k):
      stack.pop()
  # stack의 요소들 문자열로 합쳐서 반환
  answer = "".join(stack)
  return answer