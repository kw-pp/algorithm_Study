import sys
input = sys.stdin.readline


def dfs(x: int, y: int, count: int, val: str) -> None:
    if count > 6:
        answer.add(val)
        return
    for a, b in (0, 1), (1, 0), (-1, 0), (0, -1):
        if 0 <= x+a < 5 and 0 <= y+b < 5:
            val += str(table[y][x])
            count += 1
            dfs(x+a, y+b, count, val)
            val = val[:-1]
            count -= 1


table = [list(map(int, input().split())) for _ in range(5)]
answer = set()

for i in range(5):
    for j in range(5):
        dfs(i, j, 1, '')

print(len(answer))