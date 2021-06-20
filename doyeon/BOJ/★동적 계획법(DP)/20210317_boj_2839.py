n = int(input())

# bag = 0
# if(n==4 or n==7):
#   bag = -1
# elif (n % 5 == 1 or n % 5 == 3):
#   bag = n//5 + 1
# elif (n % 5 == 2 or n % 5 == 4):
#   bag = n//5 + 2
# else:
#   bag = n//5
# print(bag)

count5 = n // 5
count3 = (n % 5) // 3
left = (n%5) %3

while True:
  if left == 0:
    print(count5+count3)
    break
  else:
    count5 -= 1
    count3 = (n - count5*5) //3
    left = (n - count5*5) % 3
  if count5<0:
    print(-1)
    break