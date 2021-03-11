N = int(input())

val = list(map(int, input().split()))
cal = list(map(int, input().split()))
is_visited = [True] * 4
for i in range(len(cal)):
    if cal[i]:
        is_visited[i] = False
count = 0
seq = []
result = 0
Max = float('-INF')
Min = float('INF')
cont = []
def calc(count):
    global Max, Min, result
    if count == N-1:
        result = 0
        for i in range(N-1):
            #덧셈 계산
            if seq[i] == 0:
                if i == 0:
                    result = val[i] + val[i+1]
                else:
                    result += val[i+1]
            #뺄셈 계산
            elif seq[i] == 1:
                if i == 0:
                    result = val[i] - val[i+1]
                else:
                    result -= val[i+1]
            #곱셈 계산
            elif seq[i] == 2:
                if i == 0:
                    result = val[i] * val[i+1]
                else:
                    result *= val[i+1]
            #나눗셈 계산
            elif seq[i] == 3:
                if i == 0:
                    result = val[i] // val[i+1]
                else:
                    if result < 0:
                        result = -1 * result
                        result //= val[i+1]
                        result = -1 * result
                    else:
                        result //= val[i+1]
        return result

    else:
        for i in range(4):
            if not is_visited[i]:
                seq.append(i)
                cal[i] -= 1
                if cal[i] == 0:
                    is_visited[i] = True
                result = calc(count+1)
                is_visited[i] = False
                cal[i] += 1
                seq.pop()
                if type(result) == int:
                    if result > Max:
                        Max = result
                    if result < Min:
                        Min = result


calc(count)
print(Max)
print(Min)



