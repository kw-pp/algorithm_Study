N = int(input())
words_list = []
count = 0

for i in range(N):
    words = input()

    for j in range(len(words)):
        if j == 0:
            words_list.append(words[j])
        else:
            if words[j] != words[j-1] and words[j] in words_list:
                words_list = []
                break
            else:
                words_list.append(words[j])

    if len(words_list) != 0:
         count += 1
    else:
        continue

    words_list = []

print(count)
