from collections import defaultdict

name = input()
ans = ''
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
tmp = 0

dic = defaultdict(int)
for c in name:
    dic[c] += 1

#palindrome check
if len(name) % 2 == 0: #글자수가 짝수인 경우
    val = dic.values()
    for x in val:
        if x % 2 == 1:
            ans = "I'm Sorry Hansoo"
            break

else: #글자수가 홀수인 경우
    val = dic.items()
    cnt = 0
    for k, v in val:
        if v % 2 == 1 and cnt == 0:
            cnt += 1
            tmp = k
        elif v % 2 == 1 and cnt > 0:
            ans = "I'm Sorry Hansoo"
            break

#팰린드롬일때, 알파벳 개수를 돌면서 추출하기
if len(ans) == 0:
    for x in alphabet:
        if dic[x]:
            ans += x * int(dic[x] // 2)
    ans2 = ans[::-1]
    if tmp: #홀수일경우
        ans += tmp
    ans += ans2
print(ans)
