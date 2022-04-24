import sys

def move_dice(x, y, dir, idx):
    '''
    :param x: 현재 테이블 내에서 주사위의 x 좌표 값
    :param y: 현재 테이블 내에서 주사위의 y 좌표 값
    :param dir: 이동 방향 : 1(동), 2(서), 3(남), 4(북)
    :param idx: 현재 테이블과 맞닿아 있는 주사위 배열의 index
    :return: 주사위 이동 후 x, y 좌표 값, 문제에서 요구하는 주사위 상단의 값 k
    '''
    if dir == 1:
        # y 좌표 값 이동
        x = x + 1
        for i in range(2):

        # 이동 후 좌표 값이 영역 내의 범위 해당하는지 체크
        if 0 <= x < N:
            if table[y][x] == 0:







# N, M : 테이블 범위, x, y : 주사위 시작점 좌표, K : 명령의 개수
N, M, x, y, K = map(int, sys.stdin.readline().split())

# table 정보 입력
table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 이동 명령 1 : 동쪽, 2 : 서쪽, 3 : 북쪽, 4 : 남쪽
command = list(map(int, sys.stdin.readline().split()))

# 주사위 정보 초기화
dice = [0] * 6

# 테이블과 주사위가 맞닿아 있는 면을 체크하기 위한 배열
is_contacted = [False] * 6

# 시작 지점 초기화
is_contacted[0] = True

# 명령의 개수만큼 주사위 이동
for dir in command:
    x, y, k = move_dice(x, y, dir, 0)
    if k:
        print(k)




