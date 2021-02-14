string = input()
count0 = 0
count1 = 0

if string[0] == '0':
    count0 += 1
else:
    count1 += 1

for i in range(len(string)-1):
    if string[i] != string[i+1]:
        if string[i+1] == '0':
            count1+=1
        else:
            count0 += 1
print(min(count0,count1))