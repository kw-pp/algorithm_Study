def solution(array, commands):
    answer = []
    for i,j,k in commands:
        temp = array[i-1:j]
        temp.sort()
        answer.append(temp[k-1])
    return answer