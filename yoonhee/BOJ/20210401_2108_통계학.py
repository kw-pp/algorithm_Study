import sys
import collections

input = sys.stdin.readline

# 수의 개수
N = int(input())

# 정수 입력
num_list = [int(input()) for _ in range(N)]
num_list = sorted(num_list)

# 평균
def mean(num_list):
    return round(sum(num_list)/N)

# 중앙값
def median(num_list):
    if N == 1 : return num_list[0] # 주의 N = 1인 경우, 계산 X 
    elif N %2 != 0:
        return num_list[int(N/2)]
    else:
        return (num_list[int(N/2-1)] + int(num_list[int(N/2)]))/ 2

# 최빈값
def mode(num_list):
    dic_num_list = collections.Counter(num_list)
    m = dic_num_list.most_common(2)

    if N == 1: return num_list[0] # 주의 N = 1인 경우, 계산 X 
    if m[0][1] == m[1][1]: return m[1][0]
    else: return m[0][0]
        
# range
def min_max(num_list):
    return num_list[-1] - num_list[0]

print(mean(num_list))
print(median(num_list))
print(mode(num_list))
print(min_max(num_list))



