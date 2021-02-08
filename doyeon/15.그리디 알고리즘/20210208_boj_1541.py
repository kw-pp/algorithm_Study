a = input().split('-')
result = 0

# (실패) 반례 : 4-09
# eval은 0으로 시작하는 숫자에서 에러
# if a[0]!='':
#   result = eval(str(a[0]))
# for i in range(1, len(a)):
#   result -= eval(a[i])
# print(result)

# 성공
for i in a[0].split('+'): 
  result += int(i) 
for i in a[1:]: 
  for j in i.split('+'): 
    result -= int(j)
print(result)