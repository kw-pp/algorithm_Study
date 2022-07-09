import sys

n, m = map(int, sys.stdin.readline().split())
answers = []
book = []
book_dict = {}

for index in range(n):
    book.append(sys.stdin.readline()[:-1])
    book_dict[book[index]] = index+1

quizzes = [sys.stdin.readline()[:-1] for _ in range(m)]

for quiz in quizzes:
    if quiz.isdigit():
        answers.append(book[int(quiz)-1])
    else:
        answers.append(book_dict[quiz])

for answer in answers:
    print(answer)
