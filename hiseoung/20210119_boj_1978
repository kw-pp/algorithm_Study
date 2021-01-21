a, b = map(int, input().split())

def prime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

for i in range(a, b+1):
    if i == 1:
        continue
    if prime(i):
        print(i)
