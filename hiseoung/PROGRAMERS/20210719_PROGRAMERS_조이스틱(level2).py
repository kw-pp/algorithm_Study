def solution(name):
    idx = len(name)
    init = None
    for i in range(idx):
        if init == None:
            init = 'A'
        else:
            init += 'A'

    count = 0
    for i in range(len(name)):
        if name[i] == init[i]:
            continue
        else:
            count += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
            count += 1
    return count - 1