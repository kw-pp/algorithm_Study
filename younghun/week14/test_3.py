def solution(distance, scope, times):
    watchers = []

    for i in range(len(scope)):
        scope[i].sort()
        watchers.append([scope[i], times[i]])

    watchers.sort(key=lambda x : (x[0][0], x[0][1]))

    for watcher in watchers:
        danger = [1, watcher[1][0]]

        while watcher[0][1] >= danger[0]:
            if watcher[0][0] <= danger[1] and watcher[0][0] >= danger[0]:
                return watcher[0][0]
            elif watcher[0][0] <= danger[0] and watcher[0][1] >= danger[1]:
                return danger[0]
            elif watcher[0][1] <= danger[1]:
                return danger[0]

            for j in range(2):
                danger[j] += sum(watcher[1])
    return distance
