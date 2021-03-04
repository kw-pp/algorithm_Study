n = int(input())
a = list(map(int, input().split()))
x = int(input())
a.sort()
s = 0
e = 1
count = 0

while True:
    if s == len(a) - 1:
        break
    Sum = a[s] + a[e]
    if Sum == x:
        count += 1
        s += 1
        e = s + 1
    elif Sum < x:
        if e == len(a) - 1:
            s += 1
            e = s + 1
        else:
            e += 1
    elif Sum > x:
        s += 1
        e = s+1

print(count)
