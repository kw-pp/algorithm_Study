N = int(input())

cons_list = []
for i in range(1, N+1):
    dig = str(i)
    cons = i
    num = cons + sum(map(int,dig))

    if num == N:
        cons_list.append(i)

if len(cons_list) == 0:
    print(0)
else:
    print(cons_list[0])
