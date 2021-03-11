def dgit(num):
    a = map(int, list(str(num)))
    return (num+sum(a))

tmp = set([])

for x in range(1, 10000):
    tmp.add(dgit(x))

tmp1 = set(range(1,10001))
tmp2 = sorted(list(tmp1-tmp))
for i in range(len(tmp2)):
    print(tmp2[i])
