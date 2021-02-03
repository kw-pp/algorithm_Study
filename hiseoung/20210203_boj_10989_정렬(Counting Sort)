import sys
#input 대신 사용 시간이 덜 걸림
num = int(sys.stdin.readline())
#값의 최대범위가 10000까지이므로 반복횟수를 줄이기 위해 미리 범위 고정
a = 10001 * [0]
#해당 위치에 있는 숫자를 count
for i in range(num):
    a[int(sys.stdin.readline())] += 1
#count숫자만큼 값을 출력
for i in range(1, 10001):
    if a[i] != 0:
        for j in range(a[i]):
            sys.stdout.write("{}\n".format(i))
