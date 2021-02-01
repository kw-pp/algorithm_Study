from itertools import combinations

N, M = map(int, input().split())
list1 = [int(x) for x in input().split()]
list2 = list(combinations(list1,3))

sum_list = []
count = 0

for i in range(len(list2)):
    count = list2[i][0] + list2[i][1] + list2[i][2]
    sum_list.append(count)

sum_list.sort()

big = 0
for i in sum_list:
    if i <= M:
        big = i

print(big)
