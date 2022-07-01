import sys
from itertools import permutations

input = sys.stdin.readline

name = list(input().strip())
val_list = list(permutations(name, len(name)))
candidate = set()
for val in val_list:
    if val == tuple(reversed(val)):
        temp = ''.join(val)
        candidate.add(temp)


print(sorted(list(candidate))[0]) if not candidate else print("I'm Sorry Hansoo")





