T = int(input())

result = []

for i in range(T):

    breaker = False
    func = list(input())
    num = int(input())
    d = input().strip('[]').split(',')

    if num == 0:
        d=[]
    else:
        for z in range(len(d)):
            d[z] = int(d[z])
    is_reversed = False

    for j in func:
        try:
            if j == 'R':
                is_reversed = not is_reversed
            elif j == 'D' and not is_reversed:
                if len(d) == 0:
                    result.append('error')
                    breaker = True
                    break
                else:
                    d.pop(0)
            elif j == 'D' and is_reversed:
                if len(d) == 0:
                    result.append('error')
                    breaker = True
                    break
                else:
                    d.pop(-1)
        except:
            result.append('error')
            breaker=True
            break

    if breaker:
        continue
    if is_reversed:
        d.reverse()
        result.append(d)
    else:
        result.append(d)

for i in result:
    print(str(i).replace(' ', ''))



