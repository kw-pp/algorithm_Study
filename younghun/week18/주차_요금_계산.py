from collections import defaultdict
from datetime import datetime
from math import ceil


def solution(fees, records):
    answer = []
    cars = defaultdict(list)

    for record in records:  # {차량번호 : 입출차 시간} 형태로 딕셔너리를 만듬
        data = record.split()
        cars[data[1]].append(datetime.strptime(data[0], "%H:%M"))

    for key in cars.keys():  # 입차 출차 쌍이 안맞으면 "23:59 출차" 추가
        if len(cars[key]) % 2 != 0:
            cars[key].append(datetime.strptime("23:59", "%H:%M"))

    for key in sorted(cars.keys()):
        total_time = 0

        for i in range(0, len(cars[key]) - 1, 2):  # 총 시간 계산
            delta = cars[key][i + 1] - cars[key][i]
            total_time += delta.seconds // 60

        if total_time <= fees[0]:  # 기본요금만 내는 경우
            answer.append(fees[1])
            continue

        answer.append(
            fees[1] + ceil((total_time - fees[0]) / fees[2]) * fees[3]
        )  # 요금계산
    return answer
