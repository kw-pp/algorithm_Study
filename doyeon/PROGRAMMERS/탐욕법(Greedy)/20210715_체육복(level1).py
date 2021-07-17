def solution(n, lost, reserve):
    stu = [1]* (n+2)
    for i in lost:
        stu[i] -= 1
    for i in reserve:
        stu[i] += 1
    
    for i in range(1,len(stu)-1):
        if stu[i] == 0:
            if stu[i-1]==2:
                stu[i-1]=1
                stu[i]+=1
            elif stu[i+1]==2:
                stu[i+1]=1
                stu[i]+=1
    return sum(i >= 1 for i in stu)-2