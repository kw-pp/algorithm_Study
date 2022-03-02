import sys


def get_count(time):
    if time == 0:
        return 1
    elif time < 0:
        return 0

    if time >= 300:
        count[0] += 1
        return get_count(time - 300)
    elif time >= 60:
        count[1] += 1
        return get_count(time - 60)
    else:
        count[2] += 1
        return get_count(time - 10)


# 주어진 버튼 -> 300초, 60초, 10초
# 주어진 버튼으로 맞출 수 없으면 -1 출력

process_T = int(sys.stdin.readline().rstrip())
count = [0 for _ in range(3)]
answer = get_count(process_T)

if answer:
    print(f'{count[0]} {count[1]} {count[2]}')
else:
    print(-1)


