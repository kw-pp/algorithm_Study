A,B,C = map(int, input().split())

# b = list(format(B, 'b'))
# result = 1
# for i in range(len(b)):
#     if b[i] == '1' and 2 <= B:
#         result *= (A ** (2**i)) % C

# print(result % C)

def Mod(Z,X):

    if X == 1:
        return Z % C
    else:
        result = Mod(Z, X // 2)
        if X % 2 ==0:
            return result * result % C
        else:
            return result * result * Z % C

print(Mod(A, B))



