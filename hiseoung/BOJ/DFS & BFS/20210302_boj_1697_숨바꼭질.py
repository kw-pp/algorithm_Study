from collections import deque


def func(a):
    count = 0
    q = deque([[a, count]])

    while q:

        a = q.popleft()
        e = a[0]
        count = a[1]
        if not c[e]:
            c[e] = True
            if e == k:
                return count
            count += 1
            if (e * 2) <= 100000:
                q.append([e * 2, count])

            if (e + 1) <= 100000:
                q.append([e + 1, count])

            if (e - 1) >= 0:
                q.append([e - 1, count])

    return count


n, k = map(int, input().split())
c = [False] * 100001
print(func(n))
