import sys

def get_revenue(key, revenue):
    global max_value
    if key == n:
        if max_value < revenue:
            max_value = revenue
        return
    if key > n:
        return
    get_revenue(key + plan[key][0], revenue + plan[key][1])
    get_revenue(key + 1, revenue)


n = int(sys.stdin.readline())
plan = []
for i in range(n):
    plan.append(list(map(int, sys.stdin.readline().split())))
max_value = float('-inf')
get_revenue(0, 0)
print(max_value)

