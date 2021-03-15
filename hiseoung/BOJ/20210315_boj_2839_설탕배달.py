import sys
n = int(sys.stdin.readline())
count = 0
d = [0] * 5001
Target = False
a = n

def dp(n, count):
    global a, Target
    if n == 0:
        Target = True
        return count
    if n < 3:
        count += 1
        return float('inf')
    count += 1
    if d[n] != 0:
        return d[n]
    else:
        d[n] = min(dp(n-5, count), dp(n-3, count))
        if not Target and n == a:
            return -1
        else:
            return d[n]

print(dp(n,count))




