def solution(genres, plays):
    import operator
    table1 = {}
    table2 = {}
    answer = []

    for i in range(len(genres)):
        if table1.get(genres[i]) != None:
            temp = table1.get(genres[i])
            temp[i] = plays[i]
        else:
            table1[genres[i]] = {i: plays[i]}

        if table2.get(genres[i]) != None:
            table2[genres[i]] += plays[i]
        else:
            table2[genres[i]] = plays[i]

    table_sorted = sorted(table2.items(), key=operator.itemgetter(1), reverse=True)

    for i in range(len(table_sorted)):
        k = table_sorted[i][0]
        temp = sorted(table1.get(k).items(), key=operator.itemgetter(1), reverse=True)

        if len(temp) == 1:
            answer.append(temp[0][0])
        else:
            for j in range(2):
                answer.append(temp[j][0])
    return answer


genres = ["classic", "pop", "classic", "classic", "pop", "classic"]
plays = [500, 600, 150, 800, 2500, 800]

print(solution(genres, plays))

