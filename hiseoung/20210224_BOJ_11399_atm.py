T = int(input())
a = list(map(int, input().split()))

c1 = 0
c2 = 0
c3 = 0

a.sort(reverse=True)
for i in range(len(a)):
    c1 = a.pop()
    c2 += c1
    c3 += c2
print(c3)
