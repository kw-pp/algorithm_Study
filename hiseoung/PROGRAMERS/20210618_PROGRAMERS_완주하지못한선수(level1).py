def solution(participant, completion):
    # 참가자와 완주자가 리스트 형태로 주어짐
    # 먼저 maraton이라는 딕셔너리리를 선언
    # answer는 완주하지 못한 선수이름을 저장하기 위한 변수

    maraton = {}
    answer = 0

    for i in participant:

        # 참가자 리스트안의 값을 순회?하면서 해당 값이 딕셔너리에 존재하는 key인지 확인
        # 이미 존재하는 key라면 count를 증가시킴(동명이인 판별 목적)
        # 그게 아니라면 value에 1을 저장
        if maraton.get(i) != None:
            maraton[i] += 1
        else:
            maraton[i] = 1


    for j in completion:
        # 완주자 리스트 값이 maraton 딕셔너리에 존재한다면 -1을 해서 0으로 변경
        maraton[j] -= 1

    for k, v in maraton.items():
        # value값이 0이 아닌 maraton key는 1값을 갖고 있음, 0이 아니라면 그 값이 완주하지 못한 선수

        if v != 0:
            answer = k
            break

    return answer


# 다른 사람이 푼 풀이를 확인하니 collection라이브러리의 count함수를 활용해서
# 집합 자료형의 차집합처럼 계산하는 방법이 있음 보기에 깔끔한 듯, 아래 답글 보니까 속도도 더 빠른 것 같기도하고