def hanoi(num, a, b, c):
    if num == 1:
        print(a, b)
        return

    hanoi(num-1, a, c, b)
    print(a, b)
    hanoi(num-1, c, b, a)

N = int(input())
print((2**N)-1)
hanoi(N, 1, 3, 2)
