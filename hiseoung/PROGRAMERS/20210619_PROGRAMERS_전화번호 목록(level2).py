# 전화번호 목록 문제는 저번에 백준에서 한번 풀었던 문제임
# 처음에는 트라이 알고리즘을 이용해서 해결
# 두번쨰는 파이썬 내장함수 startswith()이 있다는 걸 확인했었음
def solution(phone_book):
    # 먼저 문자열 길이 순으로 정렬
    phone_book.sort()
    # zip함수 이용해서 길이 비교
    for a, b in zip(phone_book, phone_book[1:]):
        if b.startswith(a):
            return False
    return True

# 처음에는 for문 두번 돌리면서 특정 값에 대한 모든 값들 비교함 --> 시간초과
# 이해가 안가는 건 인접한 값들에 대해서만 비교를 하는건데 이게 왜 통과가 되는건지..
# startswith()을 사용하지 않고 딕셔너리(해시)를 이용해 푸는게 가능함1

def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer

# 숫자 STRING --> 정렬하면 알파벳 순(자릿수) / 시작하는 문자가 정렬의 키