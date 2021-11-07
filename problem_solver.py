# Fibonacci Sequence
a, b = 0, 1
for c in range(0,20):  
  print(a)
  a, b = b, a + b

#    KENTUCKY FRIED 
for num in range(1, 50):
  if num % 5 == 0 and num % 3 == 0:        #  (% == 0) = if remainder is 0 
    print('Kentucky Fried')
  elif num % 5 == 0:
    print('Kentucky')
  elif num % 3 == 0:
    print('Fried')
  else:
    print(num)

#      Bubble sort - list sort

user = input('Enter numbers: ')     
user = list(map(int, user))            #     takes user input, converts it to a list
print('\n',user,'\n')

lenght = len(user) -1
for k in range(0, lenght):
  for i in range(0, lenght):
    if user[i] > user[i+1]:
      user[i], user[i+1] = user[i+1], user[i]
print(user)
