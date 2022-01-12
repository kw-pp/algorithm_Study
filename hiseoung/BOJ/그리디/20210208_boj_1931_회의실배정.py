T = int(input())
a = []
for i in range(T):
    a.append(list(map(int, (input().split()))))

#다차원 리스트의 정렬 방법!
a.sort(key = lambda x: (x[1], x[0]))

cnt = 1
end = a[0][1]

for i in range(1, T):
    if a[i][0] >= end:
        cnt += 1
        end = a[i][1]

print(cnt)
