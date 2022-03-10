sent = input()
result = sent
key = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0

for i in key:
    dummy = '0' * len(i)
    if result.count(i):
        count += result.count(i)
        result = result.replace(i, dummy)


print(count + len(result.replace('0', '')))