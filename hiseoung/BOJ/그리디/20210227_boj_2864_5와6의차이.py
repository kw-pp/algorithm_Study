import sys

num_A, num_B = sys.stdin.readline().split()

max_A = int(num_A.replace('5', '6'))
max_B = int(num_B.replace('5', '6'))

min_A = int(num_A.replace('6', '5'))
min_B = int(num_B.replace('6', '5'))

print(min_A + min_B, max_A + max_B, sep=' ')


