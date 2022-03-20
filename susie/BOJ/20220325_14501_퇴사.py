N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = 0

def solution(T, P):
    global answer

    if T < N:
        solution(T + arr[T][0], P + arr[T][1])
        solution(T + 1, P)
    elif T == N:
        answer = max(answer, P)

solution(0, 0)
print(answer)
