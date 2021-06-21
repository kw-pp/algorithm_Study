# hash 안 쓰고
def solution(phone_book):
    # 먼저 문자열 길이 순으로 정렬
    phone_book.sort()
    # zip함수 이용해서 바로 앞에 있는 문자열로 시작하는지 확인
    for a, b in zip(phone_book, phone_book[1:]):
        if b.startswith(a):
            return False
    return True

# hash 사용
def solution(phone_book):
    answer = True
    hash_map = {}
    
    # 등장한 숫자들을 count 딕셔너리로 만듦
    for phone_number in phone_book:
        hash_map[phone_number] = 1
        
    # 다시 숫자들을 꺼낸뒤
    for phone_number in phone_book:
        temp = ""
        for number in phone_number: #숫자 하나씩 뜯어보기
            temp += number
            #딕셔너리 키로 같은게 있지만! 전체 숫자는 다른 경우!
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer