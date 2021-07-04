# 처음에 문자열 그대로 비교했지만 테스트케이스 못넘김
# 찾아봤더니 key값에 주어진 수를 세번 반복 후 이걸 기준으로 정렬하면 pass
def solution(numbers):
    temp = list(map(str, numbers))
    temp.sort(key = lambda x: x*3, reverse = True)
    return str(int(''.join(temp)))