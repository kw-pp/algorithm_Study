from itertools import permutations # 순열

def solution(n):
    a = set()
    # 가능한 모든 경우의 수 (순열) => set 사용해서 중복 제거
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    # set에서 0과 1 제거
    a -= set(range(0, 2))
    # 에라토스테네스의 체 사용하여 어떤 수의 배수인거 제거
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)