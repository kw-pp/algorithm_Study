import sys

num = int(sys.stdin.readline())
li = []

for i in range(num):
    sent = sys.stdin.readline().strip()

    if sent == 'pop':
        try:
            print(li.pop())
        except IndexError:
            print(-1)
    elif sent == 'size':
        print(len(li))
    elif sent == 'empty':
        if li:
            print(0)
        else:
            print(1)
    elif sent == 'top':
        try:
            print(li[-1])
        except IndexError:
            print(-1)
    else:
        li.append(sent.split()[1])
