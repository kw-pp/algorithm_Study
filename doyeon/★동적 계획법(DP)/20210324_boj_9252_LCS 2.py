import sys 
S1 = sys.stdin.readline().strip().upper() 
S2 = sys.stdin.readline().strip().upper() 
len1 = len(S1) 
len2 = len(S2) 
matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)] 
for i in range(1, len1 + 1): 
    for j in range(1, len2 + 1): 
        if S1[i - 1] == S2[j - 1]: 
            matrix[i][j] = matrix[i - 1][j - 1] + 1 
        else: 
            matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1]) 
index = matrix[-1][-1]
print(index)

# Create a character array to store the lcs string
lcs = [""] * index

# Start from the right-most-bottom-most corner and
# one by one store characters in lcs[]
i=len1; j=len2;
while i>0 and j>0:
  if S1[i-1] == S2[j-1]:
    lcs[index-1] = S1[i-1]
    i-=1
    j-=1
    index-=1
  # If not same, then find the larger of two and
  # go in the direction of larger value
  elif matrix[i-1][j] > matrix[i][j-1]:
    i-=1
  else:
    j-=1
print("".join(lcs))