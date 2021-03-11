n = int(input())
seat = input()
a = []
i = 0
count = 0

while True:
    if i > len(seat)-1:
        break
    if seat[i] == 'S':
        a.append(seat[i])
        i += 1
    else:
        a.append(seat[i:i+2])
        count += 1
        i += 2

c = (len(seat)+1) - count
if c > n:
    print(n)
else:
    print(c)
