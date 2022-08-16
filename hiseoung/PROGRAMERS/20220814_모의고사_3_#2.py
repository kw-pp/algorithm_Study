# score : 64.7
import sys
import re

sys.setrecursionlimit(10 ** 9)
burger = '1231'

def get_burger(string, answer):
    for _ in re.finditer(burger, string):
        answer += 1

    new_string = string.replace(burger, '')

    if string == new_string:
        return answer
    else:
        return get_burger(new_string, answer)

def solution(ingredient):
    return get_burger(''.join(map(str, ingredient)), 0)