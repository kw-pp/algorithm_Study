"""
num = int(input())
tmp = 0

dt = input().split()
for i in range(0, len(dt)):
    dt[i] = int(dt[i])
dt_max = dt
dt_min = dt
    
min = dt_min[0]
for i in range(0, num-1):
    if min > dt_min[i+1]:
        min = dt_min[i+1]
        
print(min, end=(' '))

max = dt_max[0]
for i in range(0, num-1):
    if max < dt_min[i+1]:
        max = dt_min[i+1]
        
print(max, end=(''))
