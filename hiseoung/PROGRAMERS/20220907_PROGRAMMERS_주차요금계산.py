from datetime import datetime

def solution(fees, records):
    # 정답 리스트
    answer = []

    # 문자열로 구성된 값들을 리스트로 분리
    table = [info.split() for info in records]

    # 자동차 정보를 담아줄 dict 선언 및 정렬
    car_info = {info.split()[1]: [] for info in records}
    for i in table:
        car_info[i[1]].append([i[0], i[2]])
    car_info = sorted(car_info.items(), key=lambda item: int(item[0]))

    # 자동차 별 주차 요금 계산
    for car, info in car_info:
        N = len(info)
        count = 0
        for i in range(0, N, 2):
            # 마지막 출차 기록이 안 남아 있는 경우
            if i + 1 == N:
                start = datetime.strptime(info[i][0], '%H:%M')
                end = datetime.strptime('23:59', '%H:%M')
                result = end - start
                count += result.seconds // 60
            else:
                start = datetime.strptime(info[i][0], '%H:%M')
                end = datetime.strptime(info[i + 1][0], '%H:%M')
                result = end - start
                count += result.seconds // 60
        if count <= fees[0]:
            answer.append(fees[1])
        else:
            fee = fees[1]
            count -= fees[0]
            fee += (count // fees[2]) * fees[3]
            if count % fees[2] != 0:
                fee += fees[3]
            answer.append(fee)

    return answer