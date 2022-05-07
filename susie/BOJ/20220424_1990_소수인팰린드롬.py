a, b = map(int, input().split())
a = min(a, 9999999)
b = min(b, 9999999)

def is_prime(n):
  if n == 1:
    return False
  else:
    for i in range(2, int(n**0.5)+1):
      if n % i == 0:
        return False
    return True

def is_palin(n):
  x = str(n)
  if len(x) == 1:
    return True
  if len(x) % 2 == 1:
    for i in range(len(x)-1, len(x)//2, -1):
      if x[i] != x[(len(x)-1) - i]:
        return False
    return True
  else:
    for i in range(len(x)-1, len(x)//2 - 1, -1):
      if x[i] != x[(len(x)-1) - i]:
        return False
    return True
  
for x in range(a, b+1):
  if is_palin(x) == True and is_prime(x) == True:
    print(x)
print(-1)
