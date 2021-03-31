import sys
n = int(sys.stdin.readline())
word = set([])

for i in range(n):
    word.add(sys.stdin.readline().strip())

word = list(word)
word.sort()
word.sort(key = lambda x:len(x))

for i in word:
    print(i)
