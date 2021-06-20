n = int(input())
people = list(map(int, input().split()))
people.sort()
group = 0
j = 0
for i in people:
    j+=1
    if i <= j:
        group+=1
        j = 0
print(group)