from collections import defaultdict

def solution(X, Y):
    dic = defaultdict(int)
    twin = []
    sub_x, sub_y = str(X), str(Y)

    for y in sub_y:
        dic[y] += 1
    
    for x in sub_x:
        if dic[x]:
            dic[x] -= 1
            twin.append(x)
    
    if len(twin) == 0:
        return "-1"
    
    twin.sort(key=lambda x:-int(x))
    ans = ''.join(twin)
    if ans[0] == '0':
        return '0'
    return ans
        
