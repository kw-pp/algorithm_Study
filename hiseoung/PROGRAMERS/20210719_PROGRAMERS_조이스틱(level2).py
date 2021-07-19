def solution(name):
    idx = len(name)
    init = idx * 'A'

    count = 0
    index = 0
    right = 1
    left = 1

    for i in range(len(name)):
        if name[i] == init[i]:
            continue
        else:
            count += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
            count += 1

    for i in range(1, len(name)):
        if name[index + i] == "A":
            right += 1
        else:
            break
    for i in range(1, len(name)):
        if name[index - i] == "A":
            left += 1
        else:
            break

    if right > left:
        count += left
        index -= left
    else:
        count += right
        index += right

    return count - 2