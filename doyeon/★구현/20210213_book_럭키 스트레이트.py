n = input()
half1 = 0
half2 = 0
for i in range(len(n)//2):
    half1+=int(n[i])
for i in range(len(n)//2,len(n)):
    half2+=int(n[i])
if half1 == half2:
    print('LUCKY')
else:
    print('READY')