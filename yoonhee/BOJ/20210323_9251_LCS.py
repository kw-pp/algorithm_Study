def lcs(x,y):
    prev = [0]*len(a)
    for i,r in enumerate(a):
        currnet = []
        for j,c in enumerate(b):
            if r == c:
                e = prev[j-1] + if i*j > 0 else 1
                else:
                    e = max(prev[j] if i > 0 else 0, current[-1] if j > 0 else 0)

                current.append(e)
            prev = current
    return current[-1]
