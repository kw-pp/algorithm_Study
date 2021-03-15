n = int(input())

#양수 리스트 초기화하기
pn=[]
#음수 리스트 초기화하기
nn=[]
#나머지 수 리스트 초기화하기
en=[]
#리스트에 숫자 집어넣기
for i in range(n):
  number=int(input())
  #number가 1보다 크면 양수리스트에 추가하기
  if number>1:
    pn.append(number)
  #0보다 작으면 음수리스트에 추가하기
  elif number<=0:
    nn.append(number)
  else:
    en.append(number)

#양수리스트 큰순으로 정렬하기
pn.sort(reverse=True)
#음수리스트 작은순으로 정렬하기
nn.sort()  

answer = 0
# negative 2개씩 묶어서 더하기
for i in range(0, len(pn), 2):
  if i+1 < len(pn):
    answer += pn[i] * pn[i+1]
  else:
    answer += pn[i]
  
# positive 2개씩 묶어서 더하기
for i in range(0, len(nn), 2):
  if i+1 < len(nn):
    answer += nn[i] * nn[i+1]
  else:
    answer += nn[i]

answer += sum(en)

print(answer)