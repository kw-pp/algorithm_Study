data = input()
a = []
value = 0
for i in data:
    if i.isalpha():
        a.append(i)
    else:
        value += int(i)
a.sort()
if value != 0:
    a.append(str(value))
print(''.join(a))