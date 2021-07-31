def solution(numbers, target):
    li = [0]

    for i in numbers:
        temp = []

        for j in li:
            temp.append(j + i)
            temp.append(j - i)

        li = temp

    return li.count(target)

