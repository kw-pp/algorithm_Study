def dfs(count):
    global Max
    if count == len(number) - k:
        temp = ''.join(li)
        if Max < int(temp):
            Max = int(temp)
        else:
            return

    for i in range(len(number) - k):
        if not is_visited[count]:
            li.append(i)
            is_visited[count] = True
            dfs(count+1)
            is_visited[count] = False
            li.pop()
        else:
            continue

number = "1231234"
k = 3
number = list(number)
count = 0
is_visited = [0] * (len(number)-k)
li = []
Max = float('-inf')
dfs(0)
