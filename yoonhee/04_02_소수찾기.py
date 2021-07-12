import itertools

def prime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return False
        else:
            return True

    else:
        return False
    
def solution(numbers):
    res = set()
    for i in range(1, len(numbers) + 1):
        a = list(itertools.permutations(numbers, i))
        res.update(int(''.join(b)) for b in a)
    
    cnt = 0
    for r in res:
        if prime(r):
            cnt += 1
            print(r)
            
    return cnt
