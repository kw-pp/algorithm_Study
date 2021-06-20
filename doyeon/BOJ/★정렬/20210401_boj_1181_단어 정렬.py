import sys
input = sys.stdin.readline
n = int(input())
li = []
for _ in range(n):
  word = input().rstrip()
  word_count = len(word)
  li.append((word, word_count))

# 중복 삭제
li = list(set(li))

# 단어 숫자 정렬 > 단어 알파벳 정렬
li.sort(key = lambda word: (word[1], word[0]))

for i in li:
  print(i[0])