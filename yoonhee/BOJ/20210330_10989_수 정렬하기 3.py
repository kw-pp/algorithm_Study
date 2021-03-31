# 시간 복잡도 O(n^2) : 중첩 반복문 2개
# 완전 정렬되어있으면 O(n)
import sys
input = sys.stdin.readline
'''
sys.setrecursionlimit(10000)

num = int(input())
num_list = list(int(sys.stdin.readline()) for _ in range(num))


def bubblesort(num_list):
    for i in range(num-1):
        swap = False
        for j in range(num -i -1):
            if num_list[j] > num_list[j+1]:
               num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
               swap = True


        if swap == False:
            return num_list


print(bubblesort(num_list))
'''







N = int(input())
c=[0] * 10000

for _ in range(N):
    c[int(input())-1] += 1

for i in range(len(c)):
    if c[i] > 0:
        for _ in range(c[i]):
            print(i+1)
    
        
'''

c = [0] * 10000
n = int(sys.stdin.readline())
for _ in range(n):
    c[int(sys.stdin.readline())-1] += 1
print(c)
for i in range(10000):
    [print(i+1) for _ in range(c[i])]

    '''
