import random

guess = number = None
correct = incorrect = 0
result = []
msg = ''

while 1:
   number = random.randint(1, 10)
   guess = input('Guess a number from 1 to 10. Press -1 to exit:\n')
   
   try:
      guess = int(guess)

   except:
      print('You have made an invalid choice. \n')
      continue

   if guess > 10:
      print('You have made an invalid choice. \n')
      continue

   elif guess == -1 :
      msg = 'You have chosen to exit'
      break

   elif guess == number :
      print('your guess was absolutely right\n')
      correct += 1
      result.append([guess, number])

   else :
       print('Keep Trying. The number was ', number)
       incorrect += 1
       result.append([guess, number])

print(msg)
print('Here are your results')

for i in range(len(result)):
   print('Number = ', result[i][0], '\t', 'Guess = ', result[i][1] )
   
print('*********************')
print(f"you made {correct} correct guesses while {incorrect} were incorrect")

